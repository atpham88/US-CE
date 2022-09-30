#Michael Craig
#October 4, 2016
#Process CE results by: 1) save new builds, 2) add new builds to gen fleet, 
#3) determine which units retire due to economics

import copy, os, random, pandas as pd, numpy as np
from CreateFleetForCELoop import *
from GAMSAuxFuncs import *

########### STORE BUILD DECISIONS FROM CAPACITY EXPANSION ######################
#Inputs: running list of CE builds (2d list), CE model output as GAMS object, 
#curr CE year
#Outputs: new gen builds by technology (list of tuples of (techtype, # builds))
def saveCEBuilds(capacExpModel,resultsDir,currYear):
    newGenerators = extract1dVarResultsFromGAMSModel(capacExpModel,'vN')
    newStoECap = extract1dVarResultsFromGAMSModel(capacExpModel,'vEneBuiltSto')
    newStoPCap = extract1dVarResultsFromGAMSModel(capacExpModel,'vPowBuiltSto')
    newLines = extract1dVarResultsFromGAMSModel(capacExpModel,'vLinecapacnew')   
    print('Investments in ' + str(currYear))
    for n,d in zip(['vN','vEneBuiltSto','vPowBuiltSto','vLinecapacnew'],[newGenerators,newStoECap,newStoPCap,newLines]):
        pd.Series(d).to_csv(os.path.join(resultsDir,n+str(currYear)+'.csv'))
    return newGenerators,newStoECap,newStoPCap,newLines
                
########### ADD CAPACITY EXPANSION BUILD DECISIONS TO FLEET ####################
#Adds generators to fleet
def addNewGensToFleet(genFleet,newGenerators,newStoECap,newStoPCap,newTechs,currYear):
    for tech,newBuilds in newGenerators.items():
        if newBuilds>0: 
            techRow = newTechs.loc[newTechs['GAMS Symbol']==tech].copy()
            #Add new info to tech row   
            techRow['Unit ID'],techRow['YearAddedCE'] = '1',currYear
            techRow['On Line Year'],techRow['Retired'] = currYear,False
            #Add rows to genFleet by building full units then the remaining partial unit
            if techRow['PlantType'].values[0] != 'Hydrogen':
                #Add rows for each full build
                while newBuilds > 1: 
                    genFleet = addNewTechRowToFleet(genFleet,techRow)    
                    newBuilds -= 1
                #Add row for partial build
                techRow['Capacity (MW)'] *= newBuilds
                techRow['Nameplate Energy Capacity (MWh)'] *= newBuilds
                genFleet = addNewTechRowToFleet(genFleet,techRow)
            else:
                #Add seasonal storage (hydrogen) by evenly dividing added E & P capacity among new units (E capacity is separate variable)
                numNewH2Facilities = int(np.ceil(newBuilds))
                for newH2Facility in range(numNewH2Facilities):
                    techRow['Nameplate Energy Capacity (MWh)'] = newStoECap[tech]/numNewH2Facilities*1000 #1000 to go from GWh to MWh
                    techRow['Capacity (MW)'] = newStoPCap[tech]/numNewH2Facilities*1000 #1000 to go from GW to MW
                    genFleet = addNewTechRowToFleet(genFleet,techRow)
    genFleet.reset_index(inplace=True,drop=True)
    return genFleet

def addNewTechRowToFleet(genFleet,techRow):
    techRow['ORIS Plant Code'] = int(genFleet['ORIS Plant Code'].max())+1
    techRow['GAMS Symbol'] = techRow['ORIS Plant Code'].astype(str) + "+" + techRow['Unit ID'].astype(str)
    genFleet = pd.concat([genFleet,techRow])
    return genFleet

########### ADD NEW LINE CAPACITIES TO LINE LIMITS #############################
def addNewLineCapToLimits(lineLimits, newLines, gwToMW = 1000):
    for line,newCapacity in newLines.items():
        lineLimits.loc[lineLimits['GAMS Symbol']==line,'TotalCapacity'] += newCapacity*gwToMW #CE solves for GW; scale to MW
    return lineLimits









