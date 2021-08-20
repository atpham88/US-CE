#Michael Craig
#October 4, 2016
#Functions for adding sets to GAMS database. Used for CE & UC models.

from GAMSAuxFuncs import *

########### ADD GENERATOR SETS #################################################
#Add gen sets & subsets
def addGeneratorSets(db,genFleet):
    genSet = addSet(db,genFleet['GAMS Symbol'].tolist(),'egu') 
    windGenSet = addSet(db,genFleet['GAMS Symbol'].loc[genFleet['FuelType']=='Wind'].tolist(),'windegu') 
    solarGenSet = addSet(db,genFleet['GAMS Symbol'].loc[genFleet['FuelType']=='Solar'].tolist(),'solaregu') 
    return genSet

def addStoGenSets(db,genFleet):
    stoSymbols = genFleet['GAMS Symbol'].loc[genFleet['FuelType']=='Energy Storage'].tolist()
    stoGenSet = addSet(db,stoSymbols,'storageegu') 
    return stoGenSet,stoSymbols

def addStorageSubsets(db,genFleet):
    storage = genFleet.loc[genFleet['FuelType']=='Energy Storage']
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] < 30*24)].tolist(),'ststorageegu') 
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] >= 30*24)].tolist(),'ltstorageegu') 

########### ADD HOUR SETS ######################################################
#Add all hours
def addHourSet(db,hours):
    hourSymbols = [createHourSymbol(hour) for hour in hours]
    hourSet = addSet(db,hourSymbols,'h')
    return hourSet,hourSymbols

#Define season subsets of hours
#Inputs: GAMS db, dict of (season:rep hrs)
def addHourSubsets(db,blockHours):
    for season in blockHours:
        seasonHourSymbols = [createHourSymbol(hour) for hour in blockHours[season]]
        addSet(db,seasonHourSymbols,createHourSubsetName(season))

def createHourSubsetName(subsetPrefix):
    return 'block' + str(subsetPrefix) + 'h'

#Define peak demand hour subset
def addPeakHourSubset(db,peakDemandHour):
    addSet(db,[createHourSymbol(peakDemandHour)],'peakh')

########### ADD NEW TECH SETS ##################################################
#Inputs: GAMS db, new techs (2d list)
def addNewTechsSets(db,newTechsCE,incDACS):
    techSet = addSet(db,newTechsCE['GAMS Symbol'].tolist(),'tech') 
    thermalSet = addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage']=='thermal'].tolist(),'thermaltech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Nuclear'].tolist(), 'nucleartech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Combined Cycle'].tolist(), 'CCtech')
    CCSSet = addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'CCS')].tolist(), 'CCStech')
    reSet = addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage']=='renewable'].tolist(),'renewtech') 
    addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType']=='Wind'].tolist(),'windtech')
    addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType']=='Solar'].tolist(),'solartech')
    addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Battery'].tolist(), 'batterytech')
    addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Hydrogen'].tolist(), 'hydrogentech')
    storage = newTechsCE.loc[newTechsCE['ThermalOrRenewableOrStorage']=='storage']
    stoSymbols = storage['GAMS Symbol'].tolist()
    stoSet = addSet(db,stoSymbols,'storagetech')
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] < 30*24)].tolist(),'ststoragetech') 
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] >= 30*24)].tolist(),'ltstoragetech')
    dacsSet = addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType']=='DAC'].tolist(),'dacstech')
    return techSet,reSet,stoSet,stoSymbols,thermalSet,dacsSet,CCSSet

########### GENERIC FUNCTION TO ADD SET TO DATABASE ############################
#Adds set to GAMS db
def addSet(db,setSymbols,setName,setDim=1,setDescription=''):
    addedSet = db.add_set(setName, setDim, setDescription) 
    for symbol in setSymbols: addedSet.add_record(symbol) 
    return addedSet
