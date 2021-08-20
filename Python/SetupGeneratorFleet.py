#Michael Craig, 7 July 2020

import csv, os, copy, operator, random, pandas as pd, numpy as np
from AuxFuncs import *

def setupGeneratorFleet(statesForAnalysis,powerSystemsForAnalysis,
        startYear,fuelPrices,compressFleet,regElig,regCostFrac,stoEff,stoMinSOC):
    #Import NEEDS (base fleet) and strip down to 1 fuel
    genFleet = pd.read_excel(os.path.join('Data','needs_v6_06-30-2020.xlsx'),sheet_name='NEEDS v6_active',header=0)
    genFleet['FuelType'] = genFleet['Modeled Fuels'].str.split(',', expand=True)[0]
    #Import and extract data from EIA 860
    genFleet = addEIA860Data(genFleet,statesForAnalysis,powerSystemsForAnalysis)
    #Add parameters
    genFleet.loc[genFleet['FuelType']=='Energy Storage','Efficiency'] = stoEff
    genFleet.loc[genFleet['FuelType']=='Energy Storage','Minimum Energy Capacity (MWh)'] = stoMinSOC
    genFleet = addFuelPrices(genFleet,startYear,fuelPrices)
    genFleet = addEmissionsRates(genFleet) 
    if compressFleet == True: genFleet = performFleetCompression(genFleet)
    genFleet = addUnitCommitmentParameters(genFleet,'PhorumUCParameters.csv') 
    genFleet = addUnitCommitmentParameters(genFleet,'StorageUCParameters.csv')
    genFleet = addRandomOpCostAdder(genFleet)
    genFleet = addVOMandFOM(genFleet) 
    genFleet = calcOpCost(genFleet)
    genFleet = addRegResCostAndElig(genFleet,regElig,regCostFrac)
    genFleet = addReserveEligibility(genFleet)
    #Add retirement tracking columns
    for c in ['YearAddedCE','Retired','YearRetiredByCE','YearRetiredByAge']: genFleet[c]=False
    #Add unique code used as GAMS symbol
    genFleet['GAMS Symbol'] = genFleet['ORIS Plant Code'].astype(str) + "+" + genFleet['Unit ID']
    # genFleet.to_csv(r'C:\Users\atpha\Documents\Postdocs\Projects\NETs\Model\Python\Data\genFleet.txt',header=True, index=False)
    return genFleet

################################################################################
def addEIA860Data(genFleet,statesForAnalysis,powerSystemsForAnalysis,missingStoDuration=4):
    gens,plants,storage = importEIA860()
    genFleet = genFleet.merge(plants[['Plant Code','Latitude','Longitude']],left_on='ORIS Plant Code',right_on='Plant Code',how='left')
    genFleet = genFleet.merge(storage[['Plant Code','Nameplate Energy Capacity (MWh)','Maximum Charge Rate (MW)','Maximum Discharge Rate (MW)']],left_on='ORIS Plant Code',right_on='Plant Code',how='left')
    #Isolate area of interest
    genFleet = genFleet.loc[genFleet['State Name'].isin(statesForAnalysis)]
    genFleet = genFleet.loc[genFleet['Region Name'].str.contains('|'.join(powerSystemsForAnalysis))]
    genFleet.reset_index(inplace=True,drop=True)
    #Fill in missing storage parameters
    stoRowsMissingMatch = genFleet.loc[(genFleet['FuelType']=='Energy Storage') & (genFleet['Nameplate Energy Capacity (MWh)'].isnull())]
    genFleet.loc[stoRowsMissingMatch.index,'Nameplate Energy Capacity (MWh)'] = genFleet['Capacity (MW)'] * missingStoDuration
    genFleet.loc[stoRowsMissingMatch.index,'Maximum Charge Rate (MW)'] = genFleet['Capacity (MW)']
    genFleet.loc[stoRowsMissingMatch.index,'Maximum Discharge Rate (MW)'] = genFleet['Capacity (MW)']
    return genFleet

def importEIA860():
    dir860 = os.path.join('Data','EIA860')
    gens860 = pd.read_excel(os.path.join(dir860,'3_1_Generator_Y2018.xlsx'),sheet_name='Operable',header=1)
    sto860 = pd.read_excel(os.path.join(dir860,'3_4_Energy_Storage_Y2018.xlsx'),sheet_name='Operable',header=1)
    plants860 = pd.read_excel(os.path.join(dir860,'2___Plant_Y2018.xlsx'),sheet_name='Plant',header=1)
    # genFleet = gens860.merge(plants860[['Plant Code','Latitude','Longitude','Balancing Authority Code']],on='Plant Code',how='left')
    # genFleet = genFleet.merge(sto860[['Plant Code','Generator ID','Nameplate Energy Capacity (MWh)','Maximum Charge Rate (MW)','Maximum Discharge Rate (MW)']],on=['Plant Code','Generator ID'],how='left')
    return gens860,plants860,sto860
################################################################################

################################################################################
#COMPRESS FLEET BY COMBINING SMALL UNITS
def performFleetCompression(genFleet):
    maxSizeToCombine,maxCombinedSize,firstYr,lastYr,stepYr = 75,300,1975,2026,10
    rowsToDrop,rowsToAdd = list(),list()
    for fuel in ['Landfill Gas','Distillate Fuel Oil','MSW','Natural Gas','Biomass','Non-Fossil Waste','Fossil Waste','Residual Fuel Oil']:
        fuelRows = genFleet.loc[(genFleet['FuelType']==fuel) & (genFleet['Capacity (MW)']<maxSizeToCombine) & (genFleet['PlantType']!='Combined Cycle')]
        yearIntervals = [yr for yr in range(firstYr,lastYr,stepYr)]
        for endingYear in yearIntervals:
            beginningYear = 0 if endingYear == firstYr else endingYear-stepYr
            fuelRowsYears = fuelRows.loc[(fuelRows['On Line Year']>beginningYear) & (fuelRows['On Line Year']<=endingYear)]
            if fuelRowsYears.shape[0]>1: 
                runningCombinedSize,rowsToCombine = 0,list()
                for index, row in fuelRowsYears.iterrows():
                    if (runningCombinedSize + row['Capacity (MW)'] > maxCombinedSize):
                        newRow,idxsToDrop = aggregateRows(genFleet,rowsToCombine)
                        rowsToAdd.append(newRow),rowsToDrop.extend(idxsToDrop)
                        runningCombinedSize,rowsToCombine = row['Capacity (MW)'],[row]
                    else:
                        runningCombinedSize += row['Capacity (MW)']
                        rowsToCombine.append(row)
                if len(rowsToCombine)>1: 
                    newRow,idxsToDrop = aggregateRows(genFleet,rowsToCombine)
                    rowsToAdd.append(newRow),rowsToDrop.extend(idxsToDrop)    
    genFleet.drop(index=rowsToDrop,inplace=True)
    genFleet = genFleet.append(pd.DataFrame(rowsToAdd))
    genFleet.reset_index(drop=True,inplace=True)
    return genFleet
                
def aggregateRows(genFleet,rowsToCombine):
    rowsToCombine = pd.DataFrame(rowsToCombine)
    capacWts = rowsToCombine['Capacity (MW)']/rowsToCombine['Capacity (MW)'].sum()
    newRow = rowsToCombine.iloc[0].copy()
    newRow['Capacity (MW)'] = rowsToCombine['Capacity (MW)'].sum()
    newRow['On Line Year'] = rowsToCombine['On Line Year'].median()
    for p in ['CO2EmRate(lb/MMBtu)','Heat Rate (Btu/kWh)']: #'NOxEmRate(lb/MMBtu)','SO2EmRate(lb/MMBtu)'
        newRow[p] = (rowsToCombine[p]*capacWts).sum()
    newRow['Unit ID'] = newRow['Unit ID']+'COMBINED'
    return newRow,rowsToCombine.index
################################################################################

################################################################################
#ADD VARIABLE AND FIXED O&M COSTS
#Based on plant type
def addVOMandFOM(genFleet):
    vomData = pd.read_csv(os.path.join('Data','VOMValues.csv'),index_col=0)
    genFleet = genFleet.merge(vomData[['FOM(2012$/MW/yr)','VOM(2012$/MWh)']],left_on='PlantType',right_index=True,how='left')
    genFleet['VOM(2012$/MWh)'] = convertCostToTgtYr('vom',genFleet['VOM(2012$/MWh)'])
    genFleet['FOM(2012$/MW/yr)'] = convertCostToTgtYr('fom',genFleet['FOM(2012$/MW/yr)'])
    return genFleet
################################################################################

################################################################################
#ADD UNIT COMMITMENT PARAMETERS
#Based on fuel and plant type; data from PHORUM
def addUnitCommitmentParameters(genFleet,fname):
    ucData = readCSVto2dList(os.path.join('Data',fname))
    for ucHeader in ['MinDownTime(hrs)','RampRate(MW/hr)','StartCost($)','MinLoad(MWh)']:
        if ucHeader not in genFleet.columns: #only initialize once
            genFleet[ucHeader] = genFleet['Capacity (MW)'] if (ucHeader in ['RampRate(MW/hr)','MinLoad(MWh)']) else 0
        phorumParamName = mapHeadersToPhorumParamNames()[ucHeader]
        for index,row in genFleet.iterrows():
            (fuel,plantType,size) = (row['FuelType'],row['PlantType'],float(row['Capacity (MW)']))
            phorumValue = getMatchingPhorumValue(ucData,fuel,plantType,size,phorumParamName)
            if phorumValue is not None: #input files don't have all plant types
                valToAdd = phorumValue if ucHeader == 'MinDownTime(hrs)' else phorumValue*size
                if ucHeader == 'StartCost($)': valToAdd = convertCostToTgtYr('startup',valToAdd)
                genFleet.loc[index,ucHeader]=valToAdd
    return genFleet

def getMatchingPhorumValue(ucData,fuel,plantType,size,paramName):
    if plantType == 'Fuel Cell': plantType = 'Combustion Turbine'
    fuel = mapFuels()[fuel]
    phorumPropertyNameCol = ucData[0].index('PropertyName')
    phorumFuelCol = ucData[0].index('Fuel')
    phorumPlantTypeCol = ucData[0].index('PlantType')
    phorumLowerSizeCol = ucData[0].index('LowerPlantSizeLimit')
    phorumUpperSizeCol = ucData[0].index('UpperPlantSizeLimit')
    phorumValueCol = ucData[0].index('PropertyValue')
    phorumProperties = [row[phorumPropertyNameCol] for row in ucData[1:]]
    phorumFuels = [row[phorumFuelCol] for row in ucData[1:]]
    phorumPlantTypes = [row[phorumPlantTypeCol] for row in ucData[1:]]
    phorumLowerSizes = [int(row[phorumLowerSizeCol]) for row in ucData[1:]]
    phorumUpperSizes = [int(row[phorumUpperSizeCol]) for row in ucData[1:]]
    phorumValues = [float(row[phorumValueCol]) for row in ucData[1:]]
    for idx in range(len(phorumProperties)):
        if (phorumProperties[idx] == paramName and phorumFuels[idx] == fuel and 
            (phorumPlantTypes[idx] in plantType or phorumPlantTypes[idx] == 'All') and 
            (phorumLowerSizes[idx] <= size and phorumUpperSizes[idx] > size)):
            return float(phorumValues[idx])

#Return dictionary of fleet fuel : UC fuel
def mapFuels():
    return {'Bituminous': 'Coal', 'Petroleum Coke': 'Pet. Coke',
        'Subbituminous': 'Coal', 'Lignite': 'Coal', 'Natural Gas': 'NaturalGas',
        'Distillate Fuel Oil': 'Oil', 'Hydro': 'Hydro', 'Landfill Gas': 'LF Gas',
        'Biomass': 'Biomass', 'Solar': 'Solar', 'Non-Fossil Waste': 'Non-Fossil',
        'MSW': 'MSW', 'Pumped Storage': 'Hydro', 'Residual Fuel Oil': 'Oil',
        'Wind': 'Wind', 'Nuclear Fuel': 'Nuclear', 'Coal': 'Coal','Energy Storage':'Storage',
        'Hydrogen':'Storage','Storage':'Storage'}
    #EIA860 fuels
    # fleetFuelToPhorumFuelMap = {'BIT':'Coal','PC':'Pet. Coke','SGC':'Coal',
    #         'SUB':'Coal','LIG':'Coal','RC':'Coal','NG':'NaturalGas','OG':'NaturalGas',
    #         'BFG':'NaturalGas','DFO':'Oil','RFO':'Oil','KER':'Oil','BLQ':'Oil',
    #         'WAT':'Hydro','LFG':'LF Gas','OBG':'LF Gas','WH':'NaturalGas','PUR':'NaturalGas',
    #         'AB':'Biomass','WDS':'Biomass','SUN':'Solar','Non-Fossil Waste':'Non-Fossil',
    #         'MSW':'MSW','WND':'Wind','NUC':'Nuclear','MWH':'MWH'}

def mapHeadersToPhorumParamNames():
    return {'MinDownTime(hrs)':'Min Down Time','RampRate(MW/hr)':'Ramp Rate',
            'StartCost($)':'Start Cost','MinLoad(MWh)':'Min Stable Level'}
################################################################################

################################################################################
#ADD FUEL PRICES
def addFuelPrices(genFleet,currYear,fuelPrices):
    fuelPrices = fuelPrices.loc[currYear] if currYear in fuelPrices.index else fuelPrices.iloc[-1]
    fuelPrices = convertCostToTgtYr('fuel',fuelPrices)
    prices = fuelPrices.to_dict()
    fuelMap = mapFuelsToAEOPrices()
    genFleet['FuelPrice($/MMBtu)'] = [prices[fuelMap[f]] if (f in fuelMap and fuelMap[f] in prices) else (prices[f] if f in prices else 0) for f in genFleet['FuelType']]
    return genFleet

def mapFuelsToAEOPrices():
    return {'Bituminous': 'Steam Coal', 'Petroleum Coke': 'Steam Coal','Coal':'Steam Coal',
        'Subbituminous': 'Steam Coal', 'Lignite': 'Steam Coal','Nuclear Fuel': 'Uranium'}
################################################################################

################################################################################
#ADD RANDOM OP COST ADDER TO FLEET IN NEW COLUMN
#Add to all fuel types. Use value of 0.05 - makes up ~0.03% on average of fleet. 
#Max addition to op cost of gen in fleet is 0.19%.  
def addRandomOpCostAdder(genFleet,ocAdderMin=0,ocAdderMax=0): #ocAdderMax=0.05
    random.seed()
    genFleet['RandOpCostAdder($/MWh)'] = pd.Series(np.random.uniform(ocAdderMin,ocAdderMax,genFleet.shape[0]))
    return genFleet
################################################################################

################################################################################
def calcOpCost(genFleet):
    genFleet['OpCost($/MWh)'] = genFleet['FuelPrice($/MMBtu)']*genFleet['Heat Rate (Btu/kWh)']/1000+genFleet['VOM(2012$/MWh)']+genFleet['RandOpCostAdder($/MWh)']
    return genFleet
################################################################################

################################################################################
#ADD REG OFFER COST AND ELIGIBILITY
def addRegResCostAndElig(genFleet,regElig,regCostFrac):
    genFleet['RegOfferElig'] = 0
    genFleet.loc[genFleet['PlantType'].str.contains('|'.join(regElig)),'RegOfferElig'] = 1
    genFleet['RegOfferCost($/MW)'] = regCostFrac*genFleet['OpCost($/MWh)']*genFleet['RegOfferElig']
    return genFleet
################################################################################

################################################################################
def addReserveEligibility(genFleet):
    ineligibleFuelTypes = ['Wind','Solar']
    genFleet['FlexOfferElig'],genFleet['ContOfferElig'] = 1,1
    genFleet.loc[genFleet['FuelType'].str.contains('|'.join(ineligibleFuelTypes)),'FlexOfferElig'] = 0
    genFleet.loc[genFleet['FuelType'].str.contains('|'.join(ineligibleFuelTypes)),'ContOfferElig'] = 0
    return genFleet
################################################################################
    
################################################################################
def addEmissionsRates(genFleet):
    emissionRates = pd.read_excel(os.path.join('Data','co2_vol_mass_updated.xls'),sheet_name='Sheet1',index_col=0,skiprows=2,usecols='A,F')
    emissionRates = emissionRates[emissionRates.columns[0]] #convert to Series
    fuelMap = fuelMapEmissions()
    genFleet['CO2EmRate(lb/MMBtu)'] = [emissionRates[fuelMap[f]] if (f in fuelMap and fuelMap[f] in emissionRates) else (emissionRates[f] if f in emissionRates else 0) for f in genFleet['FuelType']]
    return genFleet

def fuelMapEmissions():
    return {'MSW':'Municiple Solid Waste','Biomass':'Municiple Solid Waste','Landfill Gas':'Natural Gas',
            'Distillate Fuel Oil':'Other petroleum & miscellaneous','Residual Fuel Oil':'Other petroleum & miscellaneous',
            'Waste Coal':'Bituminous','Fossil Waste':'Other petroleum & miscellaneous','Non-Fossil Waste':'Other petroleum & miscellaneous',
            'Petroleum Coke':'Petroleum coke'}
################################################################################

######################## OLD CODE ##############################################
################################################################################
#ADD EMISSION RATES FROM EGRID TO GENERATOR FLEET
#Adds eGRID emissions rates to generator fleet
#IN: generator fleet (2d list), states for analysis (1d list)
def addEmissionsRatesOLD(baseGenFleet,statesForAnalysis,runLoc):
    (egridBoiler,egridPlant) = importeGridData(statesForAnalysis,runLoc)
    emsHeadersToAdd=["NOxEmRate(lb/MMBtu)","SO2EmRate(lb/MMBtu)",
                  "CO2EmRate(lb/MMBtu)"]
    addHeaders(baseGenFleet,emsHeadersToAdd)    
    addEmissionsRatesValues(baseGenFleet,egridBoiler,egridPlant)
    fillMissingEmissionsRates(baseGenFleet,emsHeadersToAdd) 

#Fills missing generator em rates w/ average for gens w/ same fuel and plant type.
#IN: generator fleet (2d list), emissions headers to add (1d list)
def fillMissingEmissionsRates(baseGenFleet,emsHeadersToAdd):
    #Get headers and columns
    headersToColsMapBase = mapHeadersToCols(baseGenFleet)
    plantTypeCol = headersToColsMapBase['PlantType']
    fuelTypeCol = headersToColsMapBase['FuelType']
    noxCol = headersToColsMapBase[emsHeadersToAdd[0]]
    so2Col = headersToColsMapBase[emsHeadersToAdd[1]]
    co2Col = headersToColsMapBase[emsHeadersToAdd[2]]
    #Find and fill missing emissions rates values
    for idx in range(1,len(baseGenFleet)):
        if baseGenFleet[idx][noxCol]=='NA':
            (plantType,fuelType) = (baseGenFleet[idx][plantTypeCol],
                                    baseGenFleet[idx][fuelTypeCol])
            [nox,so2,co2] = getEmsRatesOfMatchingFuelAndPlantType(baseGenFleet,plantType,
                                                                  fuelType,emsHeadersToAdd)
            [avgnox,avgso2,avgco2] = [avgListVals(nox),avgListVals(so2),avgListVals(co2)]
            baseGenFleet[idx][noxCol]=avgnox
            baseGenFleet[idx][so2Col]=avgso2
            baseGenFleet[idx][co2Col]=avgco2   

#Gets emissions rates of generators w/ given plant & fuel type
#IN: generator fleet (2d list), plant and fuel type (str), em rate headers (1d list)
#OUT: NOx, SO2 and CO2 emissions rates (1d lists)
def getEmsRatesOfMatchingFuelAndPlantType(baseGenFleet,plantType,fuelType,emsHeadersToAdd):
    #Get headers
    headersToColsMapBase = mapHeadersToCols(baseGenFleet)
    noxCol = headersToColsMapBase[emsHeadersToAdd[0]]
    so2Col = headersToColsMapBase[emsHeadersToAdd[1]]
    co2Col = headersToColsMapBase[emsHeadersToAdd[2]]
    #Get cols w/ matching fuel & plant type
    matchingRowIdxs = getMatchingRowsFuelAndPlantType(baseGenFleet,plantType,fuelType,
                                                      noxCol)
    #If can't find on fuel & plant type, try just fuel type
    if matchingRowIdxs==[]:
        matchingRowIdxs = getMatchingRowsFuelType(baseGenFleet,fuelType,noxCol)
    #If still can't get emissions rate, then ues other plant & fuel type:
    #LFG - NGCT, MSW - biomass, gas & oil O/G Steam - gas O/G Steam, Non-fossil waste - 
    if matchingRowIdxs==[] and fuelType=='Landfill Gas':
        matchingRowIdxs = getMatchingRowsFuelAndPlantType(baseGenFleet,'Combustion Turbine',
                                                          'Natural Gas',noxCol)
    elif matchingRowIdxs==[] and fuelType=='MSW':
        matchingRowIdxs = getMatchingRowsFuelAndPlantType(baseGenFleet,'Biomass',
                                                          'Biomass',noxCol)
    elif matchingRowIdxs==[] and fuelType=='Natural Gas& Distillate Fuel Oil& Residual Fuel Oil':
        matchingRowIdxs = getMatchingRowsFuelAndPlantType(baseGenFleet,'O/G Steam',
                                                          'Natural Gas',noxCol)
    elif matchingRowIdxs==[] and fuelType=='Non-Fossil Waste':
        matchingRowIdxs = getMatchingRowsFuelAndPlantType(baseGenFleet,'Biomass',
                                                          'Biomass',noxCol)
    #Get emissions rates of matching rows
    [nox,so2,co2] = [[],[],[]]
    for rowIdx in matchingRowIdxs:
        row = baseGenFleet[rowIdx]
        nox.append(row[noxCol])
        so2.append(row[so2Col])
        co2.append(row[co2Col])
    return [nox,so2,co2]

#Gets row indexes in generator fleet of generators that match given plant & fuel type,
#filtering out units w/ no emissions rate data.
#IN: generator fleet (2d list), plant and fuel type (str), col w/ nox ems rate (int)
#OUT: row indices of matching plant & fuel type (1d list)
def getMatchingRowsFuelAndPlantType(baseGenFleet,plantType,fuelType,noxCol):
    headersToColsMapBase = mapHeadersToCols(baseGenFleet)
    plantTypeCol = headersToColsMapBase['PlantType']
    fuelTypeCol = headersToColsMapBase['FuelType']
    matchingRowIdxs = []
    for idx in range(len(baseGenFleet)):
        row = baseGenFleet[idx]
        if row[plantTypeCol]==plantType and row[fuelTypeCol]==fuelType:
            if row[noxCol] != 'NA': #make sure has data!
                matchingRowIdxs.append(idx)
    return matchingRowIdxs

#Gets row indexes in generator fleet of gens w/ same fuel type, filtering
#out units w/ no emissions rate data.
#IN: generator fleet (2d list), fuel type (str), col w/ nox ems rate (int)
#OUT: row indices of matching fuel type (1d list)
def getMatchingRowsFuelType(baseGenFleet,fuelType,noxCol):
    headersToColsMapBase = mapHeadersToCols(baseGenFleet)
    fuelTypeCol = headersToColsMapBase['FuelType']
    matchingRowIdxs = []
    for idx in range(len(baseGenFleet)):
        row = baseGenFleet[idx]
        if row[fuelTypeCol]==fuelType:
            if row[noxCol] != 'NA': #make sure has data!
                matchingRowIdxs.append(idx)
    return matchingRowIdxs

#Add eGRID emissions rates values to fleet, either using boiler specific 
#data for coal & o/g steam units or plant level average data. Adds
#ems rate in order of nox, so2, and co2, as set by ems headers in addEmissionsRates.
#IN: generator fleet (2d list), eGRID boiler and plant data (2d lists)
def addEmissionsRatesValues(baseFleet,egridBoiler,egridPlant):
    headersToColsMapBase = mapHeadersToCols(baseFleet)
    headersToColsMapEgridBlr = mapHeadersToCols(egridBoiler)
    headersToColsMapEgridPlnt = mapHeadersToCols(egridPlant)
    basePlantTypeCol = headersToColsMapBase['PlantType']
    noEmissionPlantTypes = ['hydro','solar pv','wind','geothermal',
                            'solar thermal','pumped storage','nuclear']
    for idx in range(1,len(baseFleet)):
        plantType = baseFleet[idx][basePlantTypeCol].lower()
        if plantType == 'coal steam':  
            [nox,so2,co2] = getBlrEmRates(baseFleet,idx,egridBoiler)
        elif plantType == 'o/g steam':
            [nox,so2,co2] = getBlrEmRates(baseFleet,idx,egridBoiler)
            if nox == 'NA': #just test on nox, but all would be na
                [nox,so2,co2] = getPlantEmRates(baseFleet,idx,egridPlant)
        elif plantType in noEmissionPlantTypes:
            [nox,so2,co2] = [0,0,0]
        else:
            [nox,so2,co2] = getPlantEmRates(baseFleet,idx,egridPlant)
        #Some plants have no emissions info, so end up w/ zero emission values - 
        #fill in 'NA' if so.
        if [nox,so2,co2] == [0,0,0] and plantType not in noEmissionPlantTypes:
            [nox,so2,co2]=['NA','NA','NA']
        baseFleet[idx].extend([nox,so2,co2])

#Look for boiler-level match of given gen in gen fleet to eGRID data, and return emissions 
#rates if find match.
#IN: gen fleet (2d list), idx for row in gen fleet (int), boiler data (2d list)
#OUT: boiler-level nox, so2 & co2 ems rates (1d list)
def getBlrEmRates(baseFleet,idx,egridBoiler):
    #Setup necessary data
    headersToColsMapBase = mapHeadersToCols(baseFleet)
    headersToColsMapEgridBlr = mapHeadersToCols(egridBoiler)
    (baseOrisCol,baseUnitCol) = (headersToColsMapBase["ORIS Plant Code"],
                                 headersToColsMapBase["Unit ID"])
    (egridOrisCol,egridBlrCol) = (headersToColsMapEgridBlr["DOE/EIA ORIS plant or facility code"],
                                  headersToColsMapEgridBlr["Boiler ID"])
    (egridBlrORISIDs,egridBlrIDs) = (colTo1dList(egridBoiler,egridOrisCol),
                                   colTo1dList(egridBoiler,egridBlrCol))    
    #eGrid ORIS IDs are given w/ .0 @ end (e.g., 5834.0). So convert to int and back to str.
    removeTrailingDecimalFromEgridORIS(egridBlrORISIDs)
    #Do mapping
    (baseOrisID,baseUnitID) = (baseFleet[idx][baseOrisCol],baseFleet[idx][baseUnitCol])
    try:
        egridBlrRow = search2Lists(egridBlrORISIDs, egridBlrIDs, baseOrisID, baseUnitID)
        [nox,so2,co2] = calculateEmissionsRatesBlr(egridBoiler,egridBlrRow)
    except:
        # print('No matching boiler for: ORIS' + str(baseOrisID) + ' Blr' + str(baseUnitID))
        [nox,so2,co2] = ['NA','NA','NA']
    return [nox,so2,co2]

#Looks for plant-level match of given unit in gen fleet to eGRID plant data,
#and returns plant-level ems rate of matching plant if found.
#IN: gen fleet (2d list), idx for row in gen fleet (int), plant data (2d list)
#OUT: plant-level nox, so2 & co2 ems rate (1d list)
def getPlantEmRates(baseFleet,idx,egridPlant):
    #Setup necessary data
    headersToColsMapBase = mapHeadersToCols(baseFleet)
    headersToColsMapEgridPlnt = mapHeadersToCols(egridPlant)
    baseOrisCol = headersToColsMapBase["ORIS Plant Code"]
    egridOrisCol = headersToColsMapEgridPlnt["DOE/EIA ORIS plant or facility code"]
    egridORISIDs = colTo1dList(egridPlant,egridOrisCol)   
    #eGrid ORIS IDs are given w/ .0 @ end (e.g., 5834.0). So convert to int and back to str.
    # removeTrailingDecimalFromEgridORIS(egridORISIDs)
    #Do mapping
    baseOrisID = baseFleet[idx][baseOrisCol]
    try:
        egridPlantRow = egridORISIDs.index(baseOrisID)
        [nox,so2,co2] = calculateEmissionsRatesPlnt(egridPlant,egridPlantRow)
    except:
        # print('No matching plant for: ORIS' + str(baseOrisID))
        [nox,so2,co2] = ['NA','NA','NA']
    return [nox,so2,co2]
    
#Gets boiler-level emissions rates.
#IN: eGRID boiler data (2d list), row in boiler data (int)
#OUT: boiler-level emissions rates [lb/mmbtu] (1d list)
def calculateEmissionsRatesBlr(egridBoiler,egridBoilerRow):
    scaleTonsToLbs = 2000
    #Define headers
    htInputHeader = 'Boiler unadjusted annual best heat input (MMBtu)'
    noxHeader = 'Boiler unadjusted annual best NOx emissions (tons)'
    so2Header = 'Boiler unadjusted annual best SO2 emissions (tons)'
    co2Header = 'Boiler unadjusted annual best CO2 emissions (tons)'
    #Calculate values
    headersToColsMap = mapHeadersToCols(egridBoiler)
    (htinputCol,noxCol,so2Col,co2Col) = (headersToColsMap[htInputHeader],
                                        headersToColsMap[noxHeader],
                                        headersToColsMap[so2Header],
                                        headersToColsMap[co2Header])
    blrData = egridBoiler[egridBoilerRow]
    (htInput,noxEms,so2Ems,co2Ems) = (blrData[htinputCol],blrData[noxCol],
                                      blrData[so2Col],blrData[co2Col])
    #Str nums have commas in them - use helper function to turn into numbers 
    (htInput,noxEms,so2Ems,co2Ems) = (toNum(htInput),toNum(noxEms),toNum(so2Ems),
                                      toNum(co2Ems))
    (noxEmsRate,so2EmsRate,co2EmsRate) = (noxEms/htInput*scaleTonsToLbs, 
                                          so2Ems/htInput*scaleTonsToLbs,
                                          co2Ems/htInput*scaleTonsToLbs)
    return [noxEmsRate,so2EmsRate,co2EmsRate]

#Gets plant-level ems rates.
#IN: eGRID plant data (2d list), row in plant data (int)
#OUT: plant-level nox, so2 and co2 ems rates [lb/mmbtu] (1d list)
def calculateEmissionsRatesPlnt(egridPlant,egridPlantRow):
    #Define headers
    noxEmsRateHeader = 'Plant annual NOx input emission rate (lb/MMBtu)'
    so2EmsRateHeader = 'Plant annual SO2 input emission rate (lb/MMBtu)'
    co2EmsRateHeader = 'Plant annual CO2 input emission rate (lb/MMBtu)'
    #Get values
    headersToColsMap = mapHeadersToCols(egridPlant)
    (noxCol,so2Col,co2Col) = (headersToColsMap[noxEmsRateHeader],
                              headersToColsMap[so2EmsRateHeader],
                              headersToColsMap[co2EmsRateHeader])
    plantData = egridPlant[egridPlantRow]
    (noxEmsRate,so2EmsRate,co2EmsRate) = [plantData[noxCol],plantData[so2Col],plantData[co2Col]]
    #Ems rate nums have commas - use helper func to turn into numbers
    (noxEmsRate,so2EmsRate,co2EmsRate) = (toNum(noxEmsRate),
                                          toNum(so2EmsRate),
                                          toNum(co2EmsRate))
    return [noxEmsRate,so2EmsRate,co2EmsRate]
################################################################################

################################################################################
def stripDownGenFleet(genFleet,greenField):
    rows = list()
    for ft in ['Natural Gas','Wind','Solar']:
        gens = genFleet.loc[genFleet['FuelType'] == ft]
        if ft == 'Natural Gas': 
            gens.iloc[0]['OpCost($/MWh)'] = 9999
        rows.append(gens.iloc[0])
    genFleet = pd.DataFrame(rows)
    genFleet['Capacity (MW)'] = 0.1
    return genFleet
################################################################################

################################################################################
#IMPORT DATA
#Import base generator fleet from NEEDS
#OUT: gen fleet (2d list)
def importNEEDSFleet(runLoc):
    if runLoc == 'pc': dirName = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\Databases\\NEEDS'  
    else: dirName = 'Data' 
    fileName = 'needs_v515_nocommas.csv'
    fullFileName = os.path.join(dirName,fileName)
    return readCSVto2dList(fullFileName)

def importTestFleet(runLoc):
    if runLoc == 'pc': dirName = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\Databases\\CETestFleet'
    else: dirName = ''
    fileName = 'testFleetTiny.csv'
    fullFileName = os.path.join(dirName,fileName)
    return readCSVto2dList(fullFileName)    

#Import eGRID boiler and plant level data, then isolate plants and boilers in state
#IN: states for analysis (1d list)
#OUT: eGRID boiler and plant data (2d lists)
def importeGridData(statesForAnalysis,runLoc):
    if runLoc == 'pc': dirName = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\Databases\\eGRID2015'
    else: dirName = os.path.join('Data','eGRID2015')
    egridBoiler = importeGridBoilerData(dirName)
    egridPlant = importeGridPlantData(dirName)
    egridStateColName = 'Plant state abbreviation'
    statesForAnalysisAbbrev = getStateAbbrevs(statesForAnalysis)
    isolateGensInStates(egridBoiler,statesForAnalysisAbbrev,egridStateColName)
    isolateGensInStates(egridPlant,statesForAnalysisAbbrev,egridStateColName)
    return (egridBoiler,egridPlant)

#Import eGRID boiler data and remove extra headers
#IN: directory w/ egrid data (str)
#OUT: boiler data (2d list)
def importeGridBoilerData(dirName):
    fileName = 'egrid2012_data_boiler.csv'
    fullFileName = os.path.join(dirName,fileName)
    boilerData = readCSVto2dList(fullFileName)
    boilerDataSlim = elimExtraneousHeaderInfo(boilerData,'eGRID2012 file boiler sequence number')
    return boilerDataSlim

#Import eGRID plant data and remove extra headers
#IN: directory w/ egrid data (str)
#OUT: plant data (2d list)
def importeGridPlantData(dirName):
    fileName = 'egrid2012_data_plant.csv'
    fullFileName = os.path.join(dirName,fileName)
    plantData = readCSVto2dList(fullFileName)
    plantDataSlim = elimExtraneousHeaderInfo(plantData,'eGRID2012 file plant sequence number')
    return plantDataSlim

#Eliminates first several rows in egrid CSV that has no useful info
#IN: eGRID fleet (2d list), value in col 0 in first row w/ valid data that want
#to save (str)
#OUT: eGRID fleet (2d list)
def elimExtraneousHeaderInfo(egridFleet,valueInFirstValidRow):
    for idx in range(len(egridFleet)):
        if egridFleet[idx][0]==valueInFirstValidRow:
            egridFleetSlim = copy.deepcopy(egridFleet[idx:])
    return egridFleetSlim

#Removes retired units from fleet based on input year
#IN: gen fleet (2d list), year below which retired units should be removed
#from fleet (int)
def removeRetiredUnits(baseGenFleet,retirementYearScreen):
    colName = "Retirement Year"
    colNum = baseGenFleet[0].index(colName)
    rowsToRemove= []
    for rowIdx in range(1,len(baseGenFleet)):
        retireYear = baseGenFleet[rowIdx][colNum]
        if int(retireYear)<retirementYearScreen: rowsToRemove.append(rowIdx)
    if rowsToRemove != []: removeRows(baseGenFleet,rowsToRemove)

#Isolates fleet to generators in states of interest
#IN: gen fleet (2d list), states for analyiss (1d list), col name w/ state data
#(str)
#OUT: gen fleet (2d list)
def isolateGensInStates(baseGenFleet,statesForAnalysis,colName):
    rowsToRemove = identifyRowsToRemove(baseGenFleet,statesForAnalysis,
                                        colName)
    removeRows(baseGenFleet,rowsToRemove)
    return baseGenFleet

#Isolates fleet to generators in power system of interest
#IN: gen fleet (2d list), power sys for analyiss (1d list)
#OUT: gen fleet (2d list)
def isolateGensInPowerSystem(baseGenFleet,powerSystemsForAnalysis):
    colName = "Region Name"
    rowsToRemove = identifyRowsToRemove(baseGenFleet,powerSystemsForAnalysis,
                                        colName)
    removeRows(baseGenFleet,rowsToRemove)
    return baseGenFleet
################################################################################


################################################################################
#GENERAL UTILITY FUNCTIONS
#Get abbreviations (which eGRID uses but NEEDS does not)
#IN: states for analysis (1d list)
#OUT: map of states names to state abbreviations (dict)
def getStateAbbrevs(statesForAnalysis): 
    stateAbbreviations = {'Virginia':'VA','North Carolina':'NC','South Carolina':'SC',
                         'Georgia':'GA','Mississippi':'MS','Alabama':'AL','Louisiana':'LA',
                         'Missouri':'MO','Arkansas':'AR','Illinois':'IL',
                         'Kentucky':'KY','Tennessee':'TN','Texas':'TX'}
    statesForAnalysisAbbrev = []
    for state in statesForAnalysis:
        statesForAnalysisAbbrev.append(stateAbbreviations[state])
    return statesForAnalysisAbbrev

#Returns a list of rows to remove for values in a given column that don't 
#equal any value in valuesToKeep.
#IN: any 2d list, values in specified column to keep (1d list), col name (str)
#OUT: row indices to remove (1d list)
def identifyRowsToRemove(list2d,valuesToKeep,colName):
    headersToColsMap = mapHeadersToCols(list2d)
    colNumber = headersToColsMap[colName]
    rowsToRemove=[]
    for row in range(1,len(list2d)):
        if list2d[row][colNumber] not in valuesToKeep:
            rowsToRemove.append(row)
    return rowsToRemove

#IN: data (2d list), row idx to remove (1d list)
def removeRows(baseGenFleet,rowsToRemove):
    for row in reversed(rowsToRemove):
        baseGenFleet.pop(row)

#Returns a dictionary mapping headers to column numbers
#IN: fleet (2d list)
#OUT: map of header name to header # (dict)
def mapHeadersToCols(fleet):
    headers = fleet[0]
    headersToColsMap = dict()
    for colNum in range(len(headers)):
        header = headers[colNum]
        headersToColsMap[header] = colNum
    return headersToColsMap

#IN: data (2d list), headers to add to first row of data (1d list)
def addHeaders(fleet,listOfHeaders):
    for header in listOfHeaders:
        fleet[0].append(header)

#Returns average of values in input 1d list
def avgListVals(listOfVals):
    (total,count) = (0,0)
    for val in listOfVals:
        total += float(val)
        count += 1
    return total/count

#Removes '.0' from end of ORIS IDs in eGRID
def removeTrailingDecimalFromEgridORIS(egridORISIDs):
    for idx in range(1,len(egridORISIDs)):
        egridORISIDs[idx] = egridORISIDs[idx][:-2]

#Converts a string w/ commas in it to a float
def toNum(s):
    numSegments = s.split(',')
    result = ""
    for segment in numSegments:
        result += segment
    return float(result)

#Return row idx (or False) where list1=data1 and list2=data2
def search2Lists(list1,list2,data1,data2):
    if (data1 not in list1) or (data2 not in list2):
            return False
    for idx in range(len(list1)):
        if list1[idx] == data1 and list2[idx] == data2:
            return idx
    return False
    
#Convert specified column in 2d list to a 1-d list
def colTo1dList(data,colNum):
    listWithColData = []
    for dataRow in data:
        listWithColData.append(dataRow[colNum])
    return listWithColData
################################################################################