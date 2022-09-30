#Michael Craig
#October 4, 2016
#Function imports data for new technologies eligible for construction in capacity expansion model

import os, pandas as pd
from SetupGeneratorFleet import *

def getNewTechs(regElig,regCostFrac,currYear,stoInCE,seasStoInCE,fuelPrices,yearIncDACS,
                incNuc,transRegions,contFlexInelig,onlyNSPSUnits=True,allowCoalWithoutCCS=False,
                firstYearForCCS=2030,newPlantDataDir=os.path.join('Data','NewPlantData')):
    if currYear > 2050: currYear = 2050
    #Read in new techs and add parameters
    newTechsCE = pd.read_excel(os.path.join(newPlantDataDir,'NewTechFramework.xlsx'))
    newTechsCE = extractATBDataForCurrentYear(newTechsCE,newPlantDataDir,currYear)
    newTechsCE = addUnitCommitmentParameters(newTechsCE,'PhorumUCParameters.csv') 
    newTechsCE = addUnitCommitmentParameters(newTechsCE,'StorageUCParameters.csv')
    newTechsCE = addFuelPrices(newTechsCE,currYear,fuelPrices)
    if currYear >= yearIncDACS: newTechsCE = addDACS(newTechsCE,fuelPrices,currYear)
    newTechsCE = addRandomOpCostAdder(newTechsCE)
    newTechsCE = calcOpCost(newTechsCE)
    newTechsCE = addRegResCostAndElig(newTechsCE,regElig,regCostFrac)
    newTechsCE = addReserveEligibility(newTechsCE,contFlexInelig)
    #Discount costs
    for c,l in zip(['CAPEX(2012$/MW)','FOM(2012$/MW/yr)'],['occ','fom']): newTechsCE[c] = convertCostToTgtYr(l,newTechsCE[c])
    #Filter plants
    if allowCoalWithoutCCS == False: newTechsCE = newTechsCE.loc[newTechsCE['PlantType'] != 'Coal Steam']
    if onlyNSPSUnits: newTechsCE = newTechsCE.loc[newTechsCE['NSPSCompliant'] == 'Yes']
    if not stoInCE: newTechsCE = newTechsCE.loc[newTechsCE['FuelType'] != 'Energy Storage']
    if not seasStoInCE: newTechsCE = newTechsCE.loc[newTechsCE['PlantType'] != 'Hydrogen']
    if not incNuc: newTechsCE = newTechsCE.loc[newTechsCE['PlantType'] != 'Nuclear']
    if currYear < firstYearForCCS: newTechsCE = newTechsCE.loc[~newTechsCE['PlantType'].str.contains('CCS')]
    #Assign tech options to each region
    newTechsCE = repeatNonRETechOptionsForEachRegion(newTechsCE,transRegions)
    newTechsCE.reset_index(inplace=True,drop=True)
    return newTechsCE

def extractATBDataForCurrentYear(newTechsCE,newPlantDataDir,currYear,scenario='Moderate'):
    #Create mapping from our technologies to names in ATB
    ptToATBTechAlias = {'Solar PV':'Utility PV','Wind':'Land-Based Wind','Battery Storage':'Utility-Scale Battery Storage','Nuclear':'Nuclear',
                    'Coal Steam CCS':'Coal','Combined Cycle':'Natural Gas','Combined Cycle CCS':'Natural Gas','Combustion Turbine':'Natural Gas'}
    feToATBTechDetail = {'Solar PV':'Class5','Wind':'Class5','Battery Storage':'4Hr Battery Storage','Nuclear':'Nuclear',
                    'Coal Steam CCS':'CCS90AvgCF','Combined Cycle':'CCAvgCF','Combined Cycle CCS':'CCCCSAvgCF','Combustion Turbine':'CTAvgCF'}
    ptToATBHRs = {'Coal Steam CCS':'Coal-90%-CCS','Combined Cycle':'NG F-Frame CC','Combined Cycle CCS':'NG F-Frame CC 90% CCS','Combustion Turbine':'NG F-Frame CT','Nuclear':'Nuclear - AP1000'}

    #Import ATB
    atb = pd.read_csv(os.path.join(newPlantDataDir,'ATBe.csv'),index_col=0,header=0)
    hrs = pd.read_csv(os.path.join(newPlantDataDir,'ATBHeatRatesJuly2022Edition.csv'),index_col=0,skiprows=1,header=0) #MMBtu/MWh

    #Filter ATB rows
    atb = atb.loc[atb['core_metric_variable']==currYear]
    atb = atb.loc[atb['core_metric_case']=='Market'] 
    atb = atb.loc[atb['scenario']==scenario]
    hrs = hrs.loc[hrs['scenario']==scenario]
    hrs = hrs[str(currYear)]

    #Add values for each plant type
    for pt in newTechsCE['PlantType']:
        if pt in ptToATBTechAlias:
            #Get rows for tech type
            techRows = atb.loc[atb['technology_alias']==ptToATBTechAlias[pt]]
            techRows = techRows.loc[techRows['techdetail']==feToATBTechDetail[pt]]

            #Extract parameters (use .iloc[0] because of redundancies in data that do not change values of our parameters of interest)
            cap = techRows.loc[techRows['core_metric_parameter']=='CAPEX']['value'].iloc[0] #$/kW
            fom = techRows.loc[techRows['core_metric_parameter']=='Fixed O&M']['value'].iloc[0] #$/kW-yr
            vom = techRows.loc[techRows['core_metric_parameter']=='Variable O&M']['value'].iloc[0] if 'Variable O&M' in techRows['core_metric_parameter'].unique() else 0 #$/MWh

            #Get heat rate from separate file
            hr = hrs[ptToATBHRs[pt]] if pt in ptToATBHRs else 0

            #Add parameters
            newTechsCE.loc[newTechsCE['PlantType']==pt,'CAPEX(2012$/MW)'] = cap*1000 #$/kW to $/MW
            newTechsCE.loc[newTechsCE['PlantType']==pt,'FOM(2012$/MW/yr)'] = fom*1000 #$/kW-yr to $/MW-yr
            newTechsCE.loc[newTechsCE['PlantType']==pt,'VOM(2012$/MWh)'] = vom #already in $/MWh
            newTechsCE.loc[newTechsCE['PlantType']==pt,'Heat Rate (Btu/kWh)'] = hr*1000
    return newTechsCE

#Add DACS parameters to new techs. DACS gen & capac values are negative in optim, so 
#all cost values (op, fom, cap) are negative (so that gen or cap * cost = positive) and emission rate is 
#positive (so that gen * ER = negative). Data based on Keith's Joule paper.
def addDACS(newTechsCE,fuelPrices,currYear):
    dacsCap = -500
    #CO2 ems removal rate NET of emissions from NG for heat. 
    #Keith: 1 t CO2 removal requires 366 kWh e [burned 5.25 GJ NG is also captured; not included in 1 t co2]
    #1 t co2/366 kwh * 2000 lb/t * 1000 kwh/mwh * mwh/3.412 mmbtu = 1601.5 lb CO2/MMBtu
    #If include heat, 1 t co2/(366 kwh + 5.25gj * .277 mwh/gj * 1000 kwh/mwh) = 1 t co2/1820.25 kwh
    #               1 t co2/1820.25 kwh * 2000lb/t * 1000kwh/mwh * mwh/3.412 mmbtu = 322 lb co2/mmbtu
    #Realmonte: 1 t CO2 removed per 500 kWh e (given as 1.8 GJ electricity, 1 GJ = 0.27778 MWh) (also 8.1 GJ heat)
    #1 t co2/1.8 gj * gj/.277 mwh * mwh/1000 kwh * 2000 lb/t * 1000 kwh/mwh * mwh/3.412 mmbtu = 1172.3 lb co2/mmbtu
    dacsNetEmsRate = 322 #lb CO2/MMBtu ; 1601.5 for keith, 1172.3 for realmonte, 322 for keith w/ NG heat
    dacsHR = 3412 #btu/kWh; just conversion factor
    #Set op costs as VOM because HR is not an accurate value
    vom = 26/366*1000 #$/MWh; Keith gives $26/t CO2; instead use $26/366 kWh
    fuelPrices = fuelPrices.loc[currYear] if currYear in fuelPrices.index else fuelPrices.iloc[-1]
    fuelPrices = convertCostToTgtYr('fuel',fuelPrices)
    ngPrice = fuelPrices['Natural Gas']   
    natGasCost = ngPrice * 5.25/366 * 1000 * 0.947 #$/MWh; 5.25 GJ NG/366 kwh given in Keith; * ng price ($/mmbtu) * conversions
    totalOpCost = natGasCost + vom
    capCost = 779.5*1e6/40.945 #2086000000/40.945 # 779.5*1e6/40.945 #$779.5M buys 0.98Mt co2/yr; @ 366kwh/1 t co2, that is 0.98*366*1e6/8760 = 40.945 MW
    #Add row to new techs df
    newRow = {'PlantType':['DAC'],'DataSource':['handCalc'],'FuelType':['DAC'],'Capacity (MW)':[dacsCap],
        'Heat Rate (Btu/kWh)':[dacsHR],'CAPEX(2012$/MW)':[-capCost],'FOM(2012$/MW/yr)':[0],'VOM(2012$/MWh)':[-totalOpCost],
        'NSPSCompliant':['Yes'],'CO2EmRate(lb/MMBtu)':[dacsNetEmsRate],'Lifetime(years)':[30],
        'FuelPrice($/MMBtu)':[0],'RampRate(MW/hr)':[abs(dacsCap)],'MinLoad(MWh)':[0],'MinDownTime(hrs)':[0],'StartCost($)':[0]}
    newTechsCE = pd.concat([newTechsCE,pd.DataFrame(newRow)])
    newTechsCE.reset_index(drop=True,inplace=True)
    print('made UC params [0] instead of 0')
    print(newTechsCE.iloc[-1])
    return newTechsCE

#For each non-wind & non-solar tech option, repeat per region. (New W&S use lat/long coords later.)
def repeatNonRETechOptionsForEachRegion(newTechsCE,transRegions):
    newTechsRE = newTechsCE.loc[newTechsCE['PlantType'].isin(['Wind','Solar PV'])].copy()
    newTechsNotRE = newTechsCE.loc[~newTechsCE.index.isin(newTechsRE.index)].copy()
    l = [newTechsRE]
    for r in transRegions:
        regionTechs = newTechsNotRE.loc[~newTechsNotRE['PlantType'].isin(['Wind','Solar PV'])].copy()
        regionTechs['region'] = r
        l.append(regionTechs)
    return pd.concat(l)

########## OLD ######################
#Account for ITC in RE cap costs
#http://programs.dsireusa.org/system/program/detail/658
def modRECapCostForITC(newTechsCE,currYear):
    if currYear > 2050: currYear = 2050
    windItc,windItcYear = .21,2020 #wind ITC expires at 2020; .21 is average of 2016-2019 ITCs
    solarItcInit,solarItcIndef, solarItcYear = .3,.1,2020 #solar ITC doesn't expire, but goes from .3 to .1
    if currYear <= windItcYear: modRECost(newTechsCE,windItc,'Wind')
    if currYear <= solarItcYear: modRECost(newTechsCE,solarItcInit,'Solar PV')
    else: modRECost(newTechsCE,solarItcIndef,'Solar PV')
    
def modRECost(newTechsCE,itc,plantType):
    ptCol = newTechsCE[0].index('PlantType')
    capexCol = newTechsCE[0].index('CAPEX(2012$/MW)')
    ptRow = [row[0] for row in newTechsCE].index(plantType)
    newTechsCE[ptRow][capexCol] *= (1-itc)
