#Michael Craig
#October 4, 2016
#Functions for adding parameters to GAMS database. Used for CE & UC models.

import copy, math, pandas as pd, numpy as np
from GAMSAuxFuncs import *
from GAMSAddSetToDatabaseFuncs import createHourSubsetName
from WriteTimeDependentConstraints import createInitSOCName

################################################################################
##################### CE & UC PARAMETERS #######################################
################################################################################
##### ADD HOURLY DEMAND PARAMETERS (GWh)
def addDemandParam(db,demandCE,hourSet,hourSymbols,demandShifter,demandShiftingBlock,mwToGW):
    demandDict = getParamIndexedByHourDict(demandCE,hourSymbols,1/mwToGW)
    add1dParam(db,demandDict,hourSet,hourSymbols,'pDemand')
    add0dParam(db,'pDemandShifter',demandShifter)
    add0dParam(db, 'pDemandShiftingBlock', demandShiftingBlock)

##### ADD EXISTING OR NEW GENERATOR PARAMETERS (scalars account for unit conversions)
def addGenParams(db,df,genSet,mwToGW,lbToShortTon,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    #Heat rate (MMBtu/GWh)
    add1dParam(db,getParamDict(df,'Heat Rate (Btu/kWh)'),genSet,df['GAMS Symbol'],'pHr' + techLbl)
    #Emissions rate (short ton/MMBtu)
    add1dParam(db,getParamDict(df,'CO2EmRate(lb/MMBtu)',1/lbToShortTon),genSet,df['GAMS Symbol'],'pCO2emrate' + techLbl)
    #Ramp rate (GW/hr)
    add1dParam(db,getParamDict(df,'RampRate(MW/hr)',1/mwToGW),genSet,df['GAMS Symbol'],'pRamprate' + techLbl)
    #Op cost (thousand$/GWh)
    add1dParam(db,getParamDict(df,'OpCost($/MWh)'),genSet,df['GAMS Symbol'],'pOpcost' + techLbl)
    #Capacity (GW)
    add1dParam(db,getParamDict(df,'Capacity (MW)',1/mwToGW),genSet,df['GAMS Symbol'],'pCapac' + techLbl)

##### ADD EXISTING OR NEW STORAGE PARAMETERS (scalars account for unit conversions)
def addStorageParams(db,df,stoSet,stoSymbols,mwToGW,stoMkts,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    df = df.loc[df['GAMS Symbol'].isin(stoSymbols)]
    #Efficiency (fraction)
    add1dParam(db,getParamDict(df,'Efficiency'),stoSet,df['GAMS Symbol'],'pEfficiency' + techLbl)

    #For existing generators
    if not newTechs:
        #Charge capacity (GW) for existing storage or **TO IMPLEMENT** ratio of discharge to charge (fraction) for new storage
        add1dParam(db,getParamDict(df,'Maximum Charge Rate (MW)',1/mwToGW),stoSet,df['GAMS Symbol'],'pCapaccharge' + techLbl)
        #Max SOC (GWh)
        add1dParam(db,getParamDict(df,'Nameplate Energy Capacity (MWh)',1/mwToGW),stoSet,df['GAMS Symbol'],'pMaxsoc' + techLbl)
        #Min SOC (GWh)
        add1dParam(db,getParamDict(df,'Minimum Energy Capacity (MWh)'),stoSet,df['GAMS Symbol'],'pMinsoc' + techLbl)
    #Whether storage can provide energy in energy market
    if not newTechs: add0dParam(db,'pStoinenergymarket',1 if 'energy' in stoMkts else 0)

##### ADD EXISTING OR NEW GENERATOR UNIT COMMITMENT PARAMETERS (scalars account for unit conversions)
def addGenUCParams(db,df,genSet,mwToGW,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    #Min load (GWh)
    add1dParam(db,getParamDict(df,'MinLoad(MWh)',1/mwToGW),genSet,df['GAMS Symbol'],'pMinload' + techLbl)  
    #Start up fixed cost (thousand$)
    add1dParam(db,getParamDict(df,'StartCost($)',1/1000),genSet,df['GAMS Symbol'],'pStartupfixedcost' + techLbl)
    #Min down time (hours)
    add1dParam(db,getParamDict(df,'MinDownTime(hrs)'),genSet,df['GAMS Symbol'],'pMindowntime' + techLbl)
    #Regulation offer cost (thousand$/GW)
    add1dParam(db,getParamDict(df,'RegOfferCost($/MW)'),genSet,df['GAMS Symbol'],'pRegoffercost' + techLbl)

##### ADD EXISTING RENEWABLE COMBINED MAXIMUM GENERATION VALUES
#Converts 1d list of param vals to hour-indexed dicts, then adds dicts to GAMS db
def addExistingRenewableMaxGenParams(db,hourSet,hourSymbols,hourlySolarGenCE,hourlyWindGenCE,mwToGW):    
    maxSolarGenDict = getParamIndexedByHourDict(hourlySolarGenCE,hourSymbols,1/mwToGW)
    add1dParam(db,maxSolarGenDict,hourSet,hourSymbols,'pMaxgensolar')
    maxWindGenDict = getParamIndexedByHourDict(hourlyWindGenCE,hourSymbols,1/mwToGW)
    add1dParam(db,maxWindGenDict,hourSet,hourSymbols,'pMaxgenwind')

###### ADD RESERVE PROVISION ELIGIBILITY (1 or 0 indicating can or can't provide reserve)
def addSpinReserveEligibility(db,df,genSet,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    add1dParam(db,getParamDict(df,'RegOfferElig'),genSet,df['GAMS Symbol'],'pRegeligible' + techLbl)
    add1dParam(db,getParamDict(df,'FlexOfferElig'),genSet,df['GAMS Symbol'],'pFlexeligible' + techLbl)
    add1dParam(db,getParamDict(df,'ContOfferElig'),genSet,df['GAMS Symbol'],'pConteligible' + techLbl)
################################################################################
################################################################################
################################################################################

################################################################################
##################### CAPACITY EXPANSION PARAMETERS ############################
################################################################################
##### ADD NEW TECH PARAMS FOR CE
def addTechCostParams(db,df,genSet,stoSet,mwToGW):
    #Fixed O&M (thousand$/GW/yr)
    add1dParam(db,getParamDict(df,'FOM(2012$/MW/yr)',mwToGW/1000),genSet,df['GAMS Symbol'],'pFom')
    #Overnight capital cost (thousand$/GW)
    add1dParam(db,getParamDict(df,'CAPEX(2012$/MW)',mwToGW/1000),genSet,df['GAMS Symbol'],'pOcc')
    #Lifetime (years)
    add1dParam(db,getParamDict(df,'Lifetime(years)'),genSet,df['GAMS Symbol'],'pLife')
    #Power & energy capital costs for storage (thousand$/GW & thousand$/GWh)
    sto = df.loc[df['ThermalOrRenewableOrStorage']=='storage']
    add1dParam(db,getParamDict(sto,'CAPEX(2012$/MW)',mwToGW/1000),stoSet,sto['GAMS Symbol'],'pPowOcc')
    add1dParam(db,getParamDict(sto,'ECAPEX(2012$/MWH)',mwToGW/1000),stoSet,sto['GAMS Symbol'],'pEneOcc')
    pPowH2Occ_temp = df.loc[df['PlantType'] == "Hydrogen", 'CAPEX(2012$/MW)']
    pEneH2Occ_temp = df.loc[df['PlantType'] == "Hydrogen", 'ECAPEX(2012$/MWH)']
    add0dParam(db, 'pPowH2Occ', pPowH2Occ_temp.mean())
    add0dParam(db, 'pEneH2Occ', pEneH2Occ_temp.mean())
    pPowBatOcc_temp = df.loc[df['PlantType'] == "Battery", 'CAPEX(2012$/MW)']
    pEneBatOcc_temp = df.loc[df['PlantType'] == "Battery", 'ECAPEX(2012$/MWH)']
    add0dParam(db, 'pPowBatOcc', pPowBatOcc_temp.mean())
    add0dParam(db, 'pEneBatOcc', pEneBatOcc_temp.mean())
    
##### ADD PLANNING RESERVE MARGIN FRACTION PARAMETER (GW)
def addPlanningReserveParam(db,planningReserve,mwToGW): 
    add0dParam(db,'pPlanningreserve',planningReserve/mwToGW)

##### ADD DISCOUNT RATE PARAMETER
def addDiscountRateParam(db,discountRate):
    add0dParam(db,'pR',discountRate)

##### INITIAL SOC IN FIRST BLOCK FOR STORAGE (GWh)
def addStoInitSOCCE(db,df,stoSet,stoSymbols,mwToGW,blocks,seasSto,initSOCFraction,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    df = df.loc[df['GAMS Symbol'].isin(stoSymbols)]
    if newTechs:
        # (pd.Series(df[param].values.astype(float)*scalar,index=df['GAMS Symbol']).to_dict())
        if seasSto:
            add1dParam(db,pd.Series(initSOCFraction,index=df['GAMS Symbol']).to_dict(),
                stoSet,df['GAMS Symbol'],createInitSOCName(blocks[0]) + techLbl)  
        else:
            [add1dParam(db,pd.Series(initSOCFraction,index=df['GAMS Symbol']).to_dict(),
                stoSet,df['GAMS Symbol'],createInitSOCName(bl) + techLbl) for bl in blocks]
    else:
        if seasSto:
            add1dParam(db,getParamDict(df,'Nameplate Energy Capacity (MWh)',1/mwToGW*initSOCFraction),stoSet,df['GAMS Symbol'],createInitSOCName(blocks[0]) + techLbl)  
        else:
            [add1dParam(db,getParamDict(df,'Nameplate Energy Capacity (MWh)',1/mwToGW*initSOCFraction),stoSet,df['GAMS Symbol'],createInitSOCName(bl) + techLbl) for bl in blocks]

##### ADD HOURLY CAPACITY FACTORS FOR NEW RENEWABLE TECHS
#For wind and solar CFs, creates dict of (hour,techSymbol):CF, then adds them to GAMS db
def addRenewTechCFParams(db,renewTechSet,hourSet,hourSymbols,newCFs):
    cfDict = dict()
    for renewTech in newCFs:
        for idx in range(len(hourSymbols)): cfDict[(renewTech,hourSymbols[idx])] = (newCFs[renewTech].values)[idx]
    add2dParam(db,cfDict,renewTechSet,hourSet,'pCf','')

##### ADD CO2 EMISSIONS CAP (short tons)
def addCO2Cap(db,co2Cap):
    add0dParam(db,'pCO2emcap',co2Cap)

##### ADD CE PARAMETERS FOR BLOCKS
def addSeasonDemandWeights(db,blockWeights):
    for bl in blockWeights:
        add0dParam(db,'pWeight' + createHourSubsetName(bl),blockWeights[bl])

def addBlockSOCScalars(db,scalars):
    for block in scalars:
        add0dParam(db,'pSOCScalar' + createHourSubsetName(block),scalars[block])

##### ADD LIMIT ON MAX NUMBER OF NEW BUILDS PER TECH (#)
def addMaxNewBuilds(db,df,thermalSet,stoTechSet,dacsSet,CCSSet,maxCapPerTech,mwToGW):

    #Wind & solar
    for pt in ['Wind','Solar']:
        genCaps = df.loc[df['FuelType']==pt.capitalize(),'Capacity (MW)']
        add0dParam(db,'pNMax'+pt.capitalize(),np.ceil(maxCapPerTech[pt]/genCaps.mean()))
    #Thermal
    pt = 'thermal'
    techs = df.loc[df['ThermalOrRenewableOrStorage']==pt]
    techs.index = techs['GAMS Symbol']
    maxBuilds = np.ceil(maxCapPerTech[pt.capitalize()]/techs['Capacity (MW)']).to_dict()
    add1dParam(db,maxBuilds,thermalSet,techs['GAMS Symbol'],'pNMax'+pt.capitalize())
    # Nuclear
    pt = 'Nuclear'
    genCaps = df.loc[df['PlantType']==pt.capitalize(),'Capacity (MW)']
    add0dParam(db, 'pNMaxNuclear', np.ceil(maxCapPerTech[pt]/genCaps.mean()))
    # CCS
    pt1 = 'Coal Steam CCS'
    pt2 = 'Combined Cycle CCS'
    pt = 'CCS'
    techs = df.loc[(df['PlantType'] == pt1) | (df['PlantType'] == pt2)]
    techs.index = techs['GAMS Symbol']
    maxBuilds = np.ceil(maxCapPerTech[pt] / techs['Capacity (MW)']).to_dict()
    add1dParam(db, maxBuilds, CCSSet, techs['GAMS Symbol'], 'pNMaxCCS')
    # CC
    pt = 'Combined Cycle'
    genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
    add0dParam(db, 'pNMaxCC', np.ceil(maxCapPerTech[pt] / genCaps.mean()))
    #DACS
    ft = 'DAC'
    techs = df.loc[df['FuelType']==ft]
    techs.index = techs['GAMS Symbol']
    maxBuilds = np.ceil(maxCapPerTech[ft.capitalize()]/techs['Capacity (MW)']).to_dict()
    add1dParam(db,maxBuilds,dacsSet,techs['GAMS Symbol'],'pNMaxDACS')
    #Storage. Use positive continuous variable for added power & energy separately,
    #so ignore capacity & set upper P & E bounds.
    # Hydrogen
    pt = 'Hydrogen'
    genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
    maxPCapH2 = np.ceil(maxCapPerTech[pt] / mwToGW)
    maxECapH2 = maxPCapH2 * 2880
    add0dParam(db, 'pPMaxH2Sto', maxPCapH2)
    add0dParam(db, 'pEMaxH2Sto', maxECapH2)

    # Battery
    pt = 'Battery'
    genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
    maxPCapBat = np.ceil(maxCapPerTech[pt] / mwToGW)
    maxECapBat = maxPCapBat * 4
    add0dParam(db, 'pPMaxBatSto', maxPCapBat)
    add0dParam(db, 'pEMaxBatSto', maxECapBat)

    maxPCapStorage = pd.Series({'GAMS Symbol': 0, 'Battery Storage': maxPCapBat, 'Hydrogen': maxPCapH2})
    maxECapStorage = pd.Series({'GAMS Symbol': 0, 'Battery Storage': maxECapBat, 'Hydrogen': maxECapH2})
    maxPCapStorage.to_csv('maxPCapStorage.txt')
    #eff_H2 = df.loc[df['PlantType'] == 'Hydrogen', 'Efficiency']
    #eff_Bat = df.loc[df['PlantType'] == 'Battery Storage', 'Efficiency']
    #add0dParam(db, 'pEfficiencyH2tech', eff_H2.mean())
    #add0dParam(db, 'pEfficiencyBattech', eff_Bat.mean())

    pt = 'storage'
    techs = df.loc[df['ThermalOrRenewableOrStorage']==pt]
    techs.index = techs['GAMS Symbol']
    maxPCap = pd.Series(maxCapPerTech[pt.capitalize()]/mwToGW,index=techs['GAMS Symbol'])
    maxPCap.to_csv('maxPCap.txt')
    #add1dParam(db,maxPCap.to_dict(),stoTechSet,techs['GAMS Symbol'],'pPMaxSto')
    maxECap = maxPCap*(techs['Nameplate Energy Capacity (MWh)']/techs['Capacity (MW)'])
    #add1dParam(db,maxECap,stoTechSet,techs['GAMS Symbol'],'pEMaxSto')
    add1dParam(db, maxPCapStorage.to_dict(), stoTechSet, techs['GAMS Symbol'], 'pPMaxSto')
    add1dParam(db, maxECapStorage.to_dict(), stoTechSet, techs['GAMS Symbol'], 'pEMaxSto')

##### ADD INITIAL COMMITMENT STATE FOR EXISTING GENS FOR EACH TIME BLOCK
def addInitialOnOffForEachBlock(db,onOffInitialEachPeriod,genSet):
    for block in onOffInitialEachPeriod:
        onOffBlockDict = onOffInitialEachPeriod[block]
        add1dParam(db,onOffBlockDict,genSet,[g for g in onOffBlockDict],'pOnoroffinit' + createHourSubsetName(block))

# ##### ADD FIRM FRACTION FOR EXISTING GENERATORS
# #Firm fraction goes towards meeting planning reserve margin
# def addExistingPlantFirmFractions(db,genFleet,genSet,genSymbols,firmCapacityCreditsExistingGens):
#     firmCreditDict = getFirmCreditExistingGenDict(genFleet,firmCapacityCreditsExistingGens)
#     (firmCreditName,firmCreditDescrip) = ('pFirmcapacfractionegu','firm capacity fraction')
#     firmCreditExistingGenParam = add1dParam(db,firmCreditDict,genSet,genSymbols,firmCreditName,firmCreditDescrip)

# #Returns dict of (genSymbol:capacCredit) based on plant type of each generator    
# def getFirmCreditExistingGenDict(genFleet,firmCapacityCreditsExistingGens):
#     plantTypeCol = genFleet[0].index('PlantType')
#     firmCapacityCreditsExistingGensDict = dict()
#     for row in genFleet[1:]:
#         capacCredit = firmCapacityCreditsExistingGens[row[plantTypeCol]]
#         firmCapacityCreditsExistingGensDict[createGenSymbol(row,genFleet[0])] = capacCredit
#     return firmCapacityCreditsExistingGensDict
    
# ##### ADD FIRM FRACTION FOR NEW TECHS
# #Determines firm fraction of new techs based on plant type
# def addTechFirmFractions(db,techSet,techSymbols,thermalTechSymbols,renewTechSymbols,newRECapacCredits):
#     techFirmFracDict = dict()
#     for thermalTech in thermalTechSymbols: techFirmFracDict[thermalTech] = 1
#     for renewTech in renewTechSymbols: techFirmFracDict[renewTech] = newRECapacCredits[renewTech]
#     (firmCreditName,firmCreditDescrip) = ('pFirmcapacfractiontech','firm capacity fraction for new techs')
#     firmCreditTechParam = add1dParam(db,techFirmFracDict,techSet,techSymbols,firmCreditName,firmCreditDescrip)
################################################################################
################################################################################
################################################################################

################################################################################
##################### UNIT COMMITMENT PARAMETERS ###############################
################################################################################
def addStorageInitSOC(db,initSOC,stoGenSet,mwToGW):
    add1dParam(db,(initSOC/mwToGW).to_dict(),stoGenSet,initSOC.index,'pInitsoc')

##### RESERVE PARAMETERS
def addReserveParameters(db,reserves,rrToRegTime,rrToFlexTime,rrToContTime,hourSet,hourSymbols,mwToGW):
    for p,v in zip(['pRampratetoregreservescalar','pRampratetoflexreservescalar','pRampratetocontreservescalar'],[rrToRegTime,rrToFlexTime,rrToContTime]):
        add0dParam(db,p,v)
    for p,c in zip(['pRegupreserves','pFlexreserves','pContreserves'],['RegUp','Flex','Cont']):
        resDict = getParamIndexedByHourDict(reserves[c].values,hourSymbols,1/mwToGW)
        add1dParam(db,resDict,hourSet,hourSymbols,p,'')

def addResIncParams(db,regUpInc,flexInc,renewTechSet,hourSet,hourSymbols):
    for p,df in zip(['pRegUpReqIncRE','pFlexReqIncRE'],[regUpInc,flexInc]):
        resDict = dict()
        for renewTech in df:
            for idx in range(len(hourSymbols)): resDict[(renewTech,hourSymbols[idx])] = (df[renewTech].values)[idx]
        add2dParam(db,resDict,renewTechSet,hourSet,p,'')
    
##### INITIAL CONDITIONS
#Always pass in energy values in MWh
def addEguInitialConditions(db,genSet,onOffInitial,genAboveMinInitial,mdtCarriedInitial,mwToGW):
    add1dParam(db,onOffInitial.to_dict(),genSet,onOffInitial.index,'pOnoroffinitial')
    add1dParam(db,mdtCarriedInitial.to_dict(),genSet,mdtCarriedInitial.index,'pMdtcarriedhours')
    add1dParam(db,(genAboveMinInitial/mwToGW).to_dict(),genSet,genAboveMinInitial.index,'pGenabovemininitial')

def getInitialCondsDict(fleetUC,initialCondValues,scalar):
    initCondsDict = dict()
    for rowNum in range(1,len(fleetUC)):
        initCondsDict[createGenSymbol(fleetUC[rowNum],fleetUC[0])] = initialCondValues[rowNum-1] / scalar
    return initCondsDict

##### COST OF NON-SERVED ENERGY (thousand$/GWh)
def addCostNonservedEnergy(db,cnse):
    add0dParam(db,'pCnse',cnse)

##### CO2 PRICE (thousand$/short ton)
def addCo2Price(db,co2Price):
    add0dParam(db,'pCO2Cost',co2Price/1000)
################################################################################
################################################################################
################################################################################

################################################################################
############ GENERIC FUNCTIONS TO ADD PARAMS TO GAMS DB ########################
################################################################################
def add0dParam(db,paramName,paramValue,paramDescrip=''):
    addedParam = db.add_parameter(paramName,0,paramDescrip)
    addedParam.add_record().value = paramValue

def add1dParam(db,paramDict,idxSet,setSymbols,paramName,paramDescrip=''):
    addedParam = db.add_parameter_dc(paramName,[idxSet],paramDescrip)
    for idx in setSymbols: addedParam.add_record(idx).value = paramDict[idx]

def add2dParam(db,param2dDict,idxSet1,idxSet2,paramName,paramDescrip):
    addedParam = db.add_parameter_dc(paramName,[idxSet1,idxSet2],paramDescrip)
    for k,v in iter(param2dDict.items()): addedParam.add_record(k).value = float(v)

def getParamDict(df,param,scalar=1):
    return (pd.Series(df[param].values.astype(float)*scalar,index=df['GAMS Symbol']).to_dict())

#Stores set of values into dictionary keyed by hour
#Inputs: set of param values (1d list), hour symbols (1d list), optional scalar
#Outputs: dictionary of (hour symbol:param val)
def getParamIndexedByHourDict(paramVals,hourSymbols,*scalar):
    paramIndexedByHourDict = dict()
    for idx in range(len(hourSymbols)): paramIndexedByHourDict[hourSymbols[idx]] = paramVals[idx]*scalar[0]
    return paramIndexedByHourDict
################################################################################
################################################################################
################################################################################

