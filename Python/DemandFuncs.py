#Michael Craig
#October 4, 2016
#Functions related to electricity demand profile

import operator, os, pandas as pd
from AuxFuncs import *

########### GET SCALED DEMAND BASED ON CURRENT YEAR ############################
#Inputs: initial demand values (1d list), annual demand growth (fraction), 
#year of initial demand values, current CE year
#Outputs: demand values in current CE year (1d list)
def scaleDemandForGrowthAndEE(baseDemand,annualDemandGrowth,demandYear,currYear, elect_demand):
    demandScalar = (1 + annualDemandGrowth)**(currYear - demandYear)
    filename = 'EFS_Load' + '.csv'
    demandDir = os.path.join('Data', 'ERCOTDemand')
    # Read into pd
    rawDemand = pd.read_csv(os.path.join(demandDir, filename), delimiter=',', index_col='hour')
    if elect_demand == 1:
        if currYear == 2020:
            demand = rawDemand['EFS2020']
        elif currYear == 2030:
            demand = rawDemand['EFS2030']
        elif currYear == 2040:
            demand = rawDemand['EFS2040']
        elif currYear == 2050:
            demand = rawDemand['EFS2050']
        demandWithGrowth = demand.values.tolist()
    elif elect_demand == 0:
        demandWithGrowth = [val*demandScalar for val in baseDemand]
    return demandWithGrowth

########### GET NET DEMAND AND REMOVE WIND & SOLAR FROM FLEET ##################
#Inputs: hourly demand values (1d list w/out header), wind and solar CFs (2d list),
#list of solar/wind IDs and their capacities in fleet (2d list), 
#current CE year, name of model (CE versus UC)
#Outputs: net demand (1d list w/out headers), hourly wind and solar gen (1d lists w/out headers)
def getNetDemand(hourlyDemand,windCFs,ewdIdAndCapac,solarCFs,solarFilenameAndCapac):
    hourlyWindGen = getHourlyGenProfile(windCFs,ewdIdAndCapac)
    hourlySolarGen = getHourlyGenProfile(solarCFs,solarFilenameAndCapac)
    netDemand = calcNetDemand(hourlyDemand,hourlyWindGen,hourlySolarGen)
    return (netDemand,hourlyWindGen,hourlySolarGen)

#Inputs: CFs (2d list w/ header), unit ids and capacities (2d list w/ header)
#Outputs: hourly generation values (1d list w/out header)
def getHourlyGenProfile(cfs,idAndCapacs):
    (idCol,capacCol) = (idAndCapacs[0].index('Id'),idAndCapacs[0].index('FleetCapacity')) 
    totalHourlyGen = []
    for idAndCapac in idAndCapacs[1:]:
        (unitID,capac) = (idAndCapac[idCol],idAndCapac[capacCol])
        cfRow = [row[1:] for row in cfs[1:] if row[0]==unitID]
        hourlyGen = [capac*cf for cf in cfRow[0]]
        if totalHourlyGen==[]: totalHourlyGen = hourlyGen
        else: 
            for hr in range(len(hourlyGen)): totalHourlyGen[hr] += hourlyGen[hr]
    return totalHourlyGen

#Inputs: hourly demand & wind & solar gen (1d lists w/out headers)
#Outputs: hourly net demand (1d list w/out headers)
def calcNetDemand(hourlyDemand,hourlyWindGen,hourlySolarGen):
    if len(hourlyWindGen)>0 and len(hourlySolarGen)>0:
        hourlyWindAndSolarGen = list(map(operator.add,hourlyWindGen,hourlySolarGen))
        return list(map(operator.sub,hourlyDemand,hourlyWindAndSolarGen))
    elif len(hourlyWindGen)>0:
        return list(map(operator.sub,hourlyDemand,hourlyWindGen))
    elif len(hourlySolarGen)>0:
        return list(map(operator.sub,hourlyDemand,hourlySolarGen))
    else:
        return hourlyDemand