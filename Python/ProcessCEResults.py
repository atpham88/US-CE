#Michael Craig
#October 4, 2016
#Process CE results by: 1) save new builds, 2) add new builds to gen fleet, 
#3) determine which units retire due to economics

import copy, os, random, pandas as pd
from CreateFleetForCELoop import *
from AuxFuncs import *
from GAMSAuxFuncs import *

########### STORE BUILD DECISIONS FROM CAPACITY EXPANSION ######################
#Inputs: running list of CE builds (2d list), CE model output as GAMS object, 
#curr CE year
#Outputs: new gen builds by technology (list of tuples of (techtype, # builds))
def saveCEBuilds(capacExpBuilds,ceStoEBuilds,capacExpModel,currYear):
    newGenerators = extract1dVarResultsFromGAMSModel(capacExpModel,'vN')
    newStoECap = extract1dVarResultsFromGAMSModel(capacExpModel,'vEneBuiltSto')
    add1dVarResultsTo2dList(newGenerators,capacExpBuilds,'UnitsAdded' + str(currYear))
    add1dVarResultsTo2dList(newStoECap,ceStoEBuilds,'EnergyCapacityAdded(GWh)' + str(currYear))
    return newGenerators,newStoECap

#Adds new column of results to a 2d list, maintaining even 2d list & backfilling
#empty cells if necessary for newly added rows.
#Inputs: results to add, 2d list to add results to in new col, header for new col
def add1dVarResultsTo2dList(varResults,list2d,newColHeader):
    list2d[0].append(newColHeader)
    newCol = list2d[0].index(newColHeader)
    if len(list2d)==1: #first time adding values to 2d list, so just headers
        for (symbol,value) in varResults: list2d.append([symbol,value])
    else:
        for row in list2d[1:]: row.append('') #make even 2d list
        rowLabels = [row[0] for row in list2d]
        for (symbol,value) in varResults:
            if symbol in rowLabels:
                symbolRow = rowLabels.index(symbol)
                list2d[symbolRow][newCol] = value
            else:
                list2d.append([symbol] + ['']*(newCol-1) + [value])
                
########### ADD CAPACITY EXPANSION BUILD DECISIONS TO FLEET ####################
#Inputs: gen fleet (2d list), list of new builds (list of tuples of (techtype,#builds)),
#new tech data (2d list), curr year of CE run, OPTIONAL dict of techtype:cell in which
#tech is added.
#Outputs: new gen fleet w/ new CE builds added
def addNewGensToFleet(genFleet,newGenerators,newStoECap,newTechsCE,currYear):
    genFleetWithCEResults = copy.deepcopy(genFleet)
    print('Number units added by CE in ' + str(currYear) + ':',newGenerators)
    genFleetWithCEResults = addGeneratorsToFleet(genFleetWithCEResults,newGenerators,newStoECap,newTechsCE,currYear)
    return genFleetWithCEResults

#Adds generators to fleet
def addGeneratorsToFleet(genFleet,newGenerators,newStoECap,newTechs,currYear,ocAdderMin=0,ocAdderMax=0.05):
    eCapDict = dict()
    for tech,cap in newStoECap: eCapDict[tech] = cap
    for (tech,newBuilds) in newGenerators:
        if newBuilds>0: 
            techRow = newTechs.loc[newTechs['GAMS Symbol']==tech].copy()
            #Add new info to tech row   
            techRow['Unit ID'],techRow['State Name'],techRow['YearAddedCE'] = '1','Texas',currYear
            techRow['On Line Year'],techRow['Retirement Year'],techRow['Retired'] = currYear,9999,False 
            if techRow['FuelType'].values[0] == 'Energy Storage': #if e sto, set energy nameplate capacity
                eCapAdded = eCapDict[tech]
                perUnitECap = eCapAdded/newBuilds*1000 #1000 to convert to MWh
                techRow['Nameplate Energy Capacity (MWh)'] = perUnitECap
            #Add rows for each full build
            while newBuilds > 1: 
                genFleet = addNewTechRowToFleet(genFleet,techRow)    
                newBuilds -= 1
            #Add row for partial build
            techRow['Capacity (MW)'] *= newBuilds
            techRow['Nameplate Energy Capacity (MWh)'] *= newBuilds
            genFleet = addNewTechRowToFleet(genFleet,techRow)
    genFleet.reset_index(inplace=True,drop=True)
    return genFleet

def addNewTechRowToFleet(genFleet,techRow):
    techRow['ORIS Plant Code'] = int(genFleet['ORIS Plant Code'].max())+1
    techRow['GAMS Symbol'] = techRow['ORIS Plant Code'].astype(str) + "+" + techRow['Unit ID'].astype(str)
    genFleet = pd.concat([genFleet,techRow])
    return genFleet

########### FIND AND MARK UNITS RETIRED BY CE ##################################
#Retire units based on generation. 
def selectAndMarkUnitsRetiredByCE(genFleet,retirementCFCutoff,ceModel,
        currYear,capacExpRetiredUnitsByCE,hoursForCE,capacExpRetiredUnitsByAge,
        netDemand,newCfs,ptEligForRetireByCF):
    genFleetUpdated = getOnlineGenFleet(genFleet,currYear)
    gen = getPriorGen(genFleet,hoursForCE,ceModel)
    peakNetDemand = getPeakNetDemand(netDemand,newCfs,genFleetUpdated,currYear)
    retiredUnitsByCE = selectRetiredUnitsByCE(retirementCFCutoff,gen,genFleetUpdated,
        hoursForCE,ptEligForRetireByCF,peakNetDemand)
    print('Num units that retire due to economics in ' + str(currYear) + ':' + str(len(retiredUnitsByCE)))
    print('Units that retire due to econ from CE in ' + str(currYear) + ':',retiredUnitsByCE)
    capacExpRetiredUnitsByCE.append(['UnitsRetiredByCE' + str(currYear)] + retiredUnitsByCE)
    #Mark retired units
    genFleet.loc[genFleet['GAMS Symbol'].isin(retiredUnitsByCE),'YearRetiredByCE'] = currYear
    genFleet.loc[genFleet['GAMS Symbol'].isin(retiredUnitsByCE),'Retired'] = True
    return genFleet

def getPriorGen(genFleet,hoursForCE,ceModel):
    gen = pd.DataFrame(index=genFleet['GAMS Symbol'],columns=[createHourSymbol(h) for h in hoursForCE]) #can also be pd.DataFrame()
    for rec in ceModel.out_db['vGen']: gen.loc[rec.key(0),rec.key(1)] = rec.level
    return gen

#Get peak net demand w/ new wind & solar built
def getPeakNetDemand(netDemand,newCfs,fleet,currYear):
    newRE = fleet.loc[(fleet['FuelType'].isin(['Wind','Solar'])) & (fleet['YearAddedCE']==currYear)]
    reCapacsByLoc = newRE.groupby('PlantType').sum()
    newREGen = newCfs * reCapacsByLoc['Capacity (MW)']
    return (netDemand - newREGen.sum(axis=1).values).max()
    
#Determines which units retire for economic reasons after CE run.
def selectRetiredUnitsByCE(retirementCFCutoff,gen,genFleet,hoursForCE,ptEligForRetireByCF,
        peakNetDemand):
    totalGen = gen.sum(axis=1)
    capacs = pd.Series((genFleet['Capacity (MW)']*len(hoursForCE)).values,index=genFleet['GAMS Symbol'])
    cfs = totalGen*1000/(capacs*len(hoursForCE))
    symbols = genFleet.loc[genFleet['PlantType'].isin(ptEligForRetireByCF)]['GAMS Symbol']
    cfsEligibleForRetirements = cfs[symbols]
    cfsSorted = cfsEligibleForRetirements.sort_values()
    cfsSorted = cfsSorted.loc[cfsSorted<retirementCFCutoff]
    nonRECapacity = genFleet.loc[~genFleet['FuelType'].isin(['Wind','Solar'])]['Capacity (MW)'].sum()
    capToDrop = nonRECapacity - peakNetDemand
    droppedCap,dropUnits = 0,list()
    if capToDrop > 0:
        for idx in cfsSorted.index:
            droppedCap += genFleet.loc[genFleet['GAMS Symbol']==idx,'Capacity (MW)'].values[0]
            if droppedCap > capToDrop: break
            else: dropUnits.append(idx)
    return dropUnits

########### SAVE CAPACITY EXPANSION RESULTS ####################################
#Write some results into CSV files
def writeCEInfoToCSVs(capacExpBuilds,capacExpRetiredUnitsByCE,capacExpRetiredUnitsByAge,resultsDir,currYear):
    write2dListToCSV(capacExpBuilds,os.path.join(resultsDir,'genAdditionsCE' + str(currYear) + '.csv'))
    write2dListToCSV(capacExpRetiredUnitsByCE,os.path.join(resultsDir,'genRetirementsEconCE' + str(currYear) + '.csv'))
    write2dListToCSV(capacExpRetiredUnitsByAge,os.path.join(resultsDir,'genRetirementsAgeCE' + str(currYear) + '.csv'))
