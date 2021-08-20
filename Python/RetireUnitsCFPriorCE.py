#Michael Craig
#Determine which coal plants should retire based on CF in PRIOR CE run. (May
#not retire after prior CE run to maintain planning margin.)

from ProcessCEResults import *
from CreateFleetForCELoop import getOnlineGenFleet

#Retire units based on CFs in prior CE run. Immediately after each CE run,
#also check for retirements but maintain ability for supply & demand balance
#so can pass generator fleet to operational model. Here, we retire those generators
#we would have retired if we did not maintain supply & demand balance capabilities. 
def retireUnitsCFPriorCE(genFleet,genFleetPriorCE,retirementCFCutoff,priorCapacExpModel,
            priorHoursCE,scaleMWtoGW,ptEligForRetireByCF,currYear,capacExpRetiredUnitsByCE):
    #Get which generators from last CE run are still online based on age of this year
    genFleetOnline = getOnlineGenFleet(genFleetPriorCE,currYear)
    genFleetOnline.to_csv('cd.csv') 
    #Update online fleet based on economic retirements in last CE run
    currentStatus = genFleet.loc[genFleet['GAMS Symbol'].isin(genFleetOnline['GAMS Symbol'])]
    # currentStatus.index = currentStatus['GAMS Symbol']
    currentStatus = currentStatus.loc[currentStatus['Retired'] == False]
    genFleetOnline = genFleetOnline.loc[genFleetOnline['GAMS Symbol'].isin(currentStatus['GAMS Symbol'])]
    #Get total generation from prior CE run
    gen = getPriorGen(genFleetOnline,priorHoursCE,priorCapacExpModel)
    #Retire units based on prior CE results
    unitsRetireCF = selectRetiredUnitsByCE(retirementCFCutoff,gen,genFleetOnline,
        priorHoursCE,ptEligForRetireByCF,0) #0 is peakNetDemand - allows all units to retire that should
    print('Num units that retire due to economics prior to CE in ' + str(currYear) + ':' + str(len(unitsRetireCF)))
    print('Units that retire due to econ from prior CE in ' + str(currYear) + ':',unitsRetireCF)
    capacExpRetiredUnitsByCE.append(['UnitsRetiredPriorToCE' + str(currYear)] + unitsRetireCF)
    #Mark retired units
    genFleet.loc[genFleet['GAMS Symbol'].isin(unitsRetireCF),'YearRetiredByCE'] = currYear
    genFleet.loc[genFleet['GAMS Symbol'].isin(unitsRetireCF),'Retired'] = True
    return unitsRetireCF,genFleet

