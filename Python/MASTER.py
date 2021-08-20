# Michael Craig

# TO DO (order of priority):
# Add time-varying limits on quantify of new techs to add
# Add contingency reserves into greenfield run
# Allow wind & solar to provide all reserves - add constriants to GAMS limiting their generation
    # in CESharedFeatures
# Finish moving away from lists
# Make solar reserve calculation efficient

import sys, os, csv, operator, copy, time, random, warnings, numpy as np, datetime as dt, pandas as pd
from os import path; from netCDF4 import Dataset; from gams import *
from AuxFuncs import *
from GAMSAuxFuncs import *
from SetupGeneratorFleet import *
from RemoveHydroFromFleetAndDemand import removeHydroFromFleetAndDemand
from ImportERCOTDemand import importHourlyERCOTDemand
from importHourlyEFSDemand import importHourlyEFSDemand
from UpdateFuelPriceFuncs import *
from DemandFuncs import *
from DemandFuncsCE import *
from SetInitCondsUC import *
from ImportNewTechs import getNewTechs
from RetireUnitsCFPriorCE import retireUnitsCFPriorCE
from CreateFleetForCELoop import *
from GetRenewableCFsMERRA import getREGen
from GetNewRenewableCFsMERRA import *
from AddWSSitesToNewTechs import addWSSitesToNewTechs
from ProcessCEResults import *
from ScaleRegResForAddedWind import scaleRegResForAddedWind
from CombinePlants import combineWindSolarStoPlants
from GAMSAddSetToDatabaseFuncs import *
from GAMSAddParamToDatabaseFuncs import *
from ConvertCO2CapToPrice import convertCo2CapToPrice
from SaveDispatchResults import saveDispatchResults, writeDispatchResults
from InitializeOnOffExistingGensCE import initializeOnOffExistingGens
from ReservesWWSIS import calcWWSISReserves
from GetIncResForAddedRE import getIncResForAddedRE
from SaveCEOperationalResults import saveCapacExpOperationalData
from SaveCEOperationalResults import saveSystemResults
from SaveCEOperationalResults import saveGeneratorResults
from ImportStorageParams import *
from WriteTimeDependentConstraints import writeTimeDependentConstraints
from WriteBuildVariable import writeBuildVariable
from CreateEmptyReserveDfs import createEmptyReserveDfs
from resultsanalysis_function_automated import results_summary


# SET OPTIONS
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

# SCALARS
mwToGW = 1000
lbToShortTon = 2000

# ###################################################################4############
# ##### UNIVERSAL PARAMETERS ####################################################
# ###############################################################################
def setKeyParameters():
    # ##################KEY PARAMETERS
    case_to_run = 1                     # == 1: reference case
                                        # == 2: limited nuclear
                                        # == 3: limited CCS and nuclear
                                        # == 4: limited hydrogen storage
    elect_demand = 1                    # == 1: electrification of demand
    run_on_gl = 2                       # == 1: running on GL supercomputing
                                        # == 2: running on personal laptop
    zeroSys = True                      # True if system is net-zero system
                                        # False if system is negative emission system
    planningDACs = 3                    # ==1: zeroSys no DAC, ==2: late DAC, ==3: early DAC

    greenField = False                  # whether to run greenField (set to True) or brownfield (False)
    includeRes = False                  # whether to include reserves in CE & dispatch models (if False, multiplies reserve timeseries by 0)
    useCO2Price = False                 # whether to calc & inc CO2 price in operations run
    co2Redux2050 = 1                    # 0.95  #fractional redux from current to 2050
    co2Ems2020 = 130594820              # -1e8  #2020 ED model results (tons)
    runCE, ceOps = True, 'ED'           # ops are 'ED' or 'UC' (econ disp or unit comm constraints)
    stoInCE, seasStoInCE = True, True   # whether to allow new storage,new seasonal storage in CE model
    runFirstYear = False                # whether to run first year of dispatch
    ucOrED = 'None'                     # STRING that is either: ED, UC, None
    reDownFactor = 4                    # downscaling factor for W&S new CFs; 1 means full resolution, 2 means half resolution, 3 is 1/3 resolution, etc

    numBlocks, daysPerBlock, daysPerPeak = 4, 5, 3                              # num rep time blocks, days per rep block, and days per peak block in CE
    fullYearCE = True if (numBlocks == 1 and daysPerBlock > 300) else False     # whether running full year in CE
    startYear, endYear, yearStepCE = 2020, 2051, 10                             # start & end year & time steps between CE runs

    if not zeroSys:
        negSys = True
    elif zeroSys:
        negSys = False

    if negSys and (planningDACs == 1): sys.exit("strict cap requires planningDACs = 2,3 only")

    incDACS, incNuc = True, True        # whether to include: DACS,nuclear
    if planningDACs == 1: incDACS = False
    elif planningDACs == 2 or planningDACs == 3: incDACS = True

    if planningDACs == 3: startYear, endYear, yearStepCE = 2020, 2051, 30

    demandShifter = 0                   # Percentage of hourly demand that can be shifted
    demandShiftingBlock = 4             # moving shifting demand window (hours)
    if co2Ems2020 < 0: incDACS = True   # make sure allow DACS if have neg ems cap

    maxCapPerTech0 = {'Wind': 2000 * reDownFactor, 'Solar': 17000 * reDownFactor, 'Thermal': 999999, 'Combined Cycle': 999999,
                     'Storage': 999999, 'Dac': -9999999, 'CCS': 999999, 'Nuclear': 999999, 'Battery': 999999, 'Hydrogen': 999999}

    if case_to_run == 1:
        maxCapPerTech = maxCapPerTech0  # max added MW per CE run (W&S by cell)
    elif case_to_run == 2:
        maxCapPerTech = {'Wind': 2000*reDownFactor, 'Solar': 17000*reDownFactor, 'Thermal': 999999, 'Combined Cycle': 999999,
                            'Storage': 999999, 'Dac': -9999999, 'CCS': 999999, 'Nuclear': 9000, 'Battery': 999999, 'Hydrogen': 999999}  # max added MW per CE run (W&S by cell)
    elif case_to_run == 3:
        maxCapPerTech = {'Wind': 2000 * reDownFactor, 'Solar': 17000 * reDownFactor, 'Thermal': 999999, 'Combined Cycle': 999999,
                         'Storage': 999999, 'Dac': -9999999, 'CCS': 1500, 'Nuclear': 9000, 'Battery': 999999, 'Hydrogen': 999999}
    elif case_to_run == 4:
        maxCapPerTech = {'Wind': 2000*reDownFactor, 'Solar': 17000*reDownFactor, 'Thermal': 999999, 'Combined Cycle': 999999,
                            'Storage': 999999, 'Dac': -9999999, 'CCS': 999999, 'Nuclear': 999999, 'Battery': 999999, 'Hydrogen': 2657}  # max added MW per CE run (W&S by cell)

    ################## GENERAL PARAMETERS
    demandYear = 2019 #year for demand data
    states,powerSystems = ['Texas'], ['ERC']            # states and power systems of analysis
    fuelPrices = importFuelPrices('Reference case')     # import fuel price time series
    compressFleet = True                                # whether to compress fleet

    # RENEWABLE CAPACITY FACTOR PARAMETERS
    tzAnalysis = 'CST'                                  # timezone of analysis

    # STORAGE PARAMETERS
    stoMkts = 'energy'                                  # energy,res,energyAndRes
    stoMinSOC, initSOCFraction = 0,0.2                  # min SOC, & initial SOC in each time block

    # CAPACITY EXPANSION PARAMETERS
    annualDemandGrowth = 0                              # fraction per year
    retireByAge = False                                 # whether to retire by age or not
    planningReserveMargin = 0.1375                      # fraction of peak demand; ERCOT targeted planning margin
    incITC = False                                      # include Investment Tax Credit or not
    retirementCFCutoff = .3                             # retire units w/ CF lower than given value
    discountRate = 0.07 #fraction    
    ptEligRetCF = ['Coal Steam']                        # which plant types retire based on capacity factor (economics)

    return (case_to_run, greenField, includeRes, useCO2Price, runCE, ceOps, stoInCE, seasStoInCE, ucOrED, numBlocks,
        daysPerBlock, daysPerPeak, fullYearCE, incDACS, incNuc,
        states, powerSystems, compressFleet, fuelPrices, co2Redux2050, co2Ems2020,
        startYear, endYear, yearStepCE, retirementCFCutoff, retireByAge, planningReserveMargin,
        discountRate, annualDemandGrowth, stoMkts, tzAnalysis, maxCapPerTech, runCE,
        runFirstYear, demandYear, ptEligRetCF, incITC, stoMinSOC, initSOCFraction, reDownFactor,
        demandShifter, demandShiftingBlock, run_on_gl, zeroSys, negSys, planningDACs, elect_demand)

def importFuelPrices(fuelPriceScenario):
    fuelPrices = pd.read_csv(os.path.join('Data', 'Energy_Prices_Electric_Power.csv'), skiprows=4, index_col=0)
    fuelPrices = fuelPrices[[col for col in fuelPrices if fuelPriceScenario in col]]
    fuelPrices.columns = [col.split(':')[0] for col in fuelPrices.columns]
    return fuelPrices    

# Define reserve parameters for UC & CE w/ UC constraints models
def defineReserveParameters(stoMkts):
    # Regulation eligibility
    regElig = ['Steam', 'Combined Cycle', 'Storage', 'Geothermal', 'Batteries', 'Flywheels']
    if 'res' not in stoMkts.lower(): regElig = [p for p in regElig if p not in ['Storage', 'Batteries', 'Flywheels']]

    # Regulation provision cost as fraction of operating cost
    regCostFrac = 0  # 0.1

    # Requirement parameters - based on WWSIS Phase 2
    regLoadFrac = .01                   # frac of hourly load in reg up & down
    contLoadFrac = .03                  # frac of hourly load in contingency
    regErrorPercentile = 40             # ptl of hourly W&S forecast errors for reg reserves; in WWSIS, 95th ptl of 10-m wind & 5-m solar forecast errors
    flexErrorPercentile = 70            # ptl of hourly W&S forecast errors used in flex reserves

    # Timeframes
    regReserveMinutes = 5               # reg res must be provided w/in 5 minutes
    flexReserveMinutes = 10             # spin reserves must be provided w/in 10 minutes
    contingencyReserveMinutes = 30      # contingency res must be provided w/in 30 minutes
    minutesPerHour = 60
    rampRateToRegReserveScalar = regReserveMinutes/minutesPerHour               # ramp rate in MW/hr
    rampRateToFlexReserveScalar = flexReserveMinutes/minutesPerHour             # ramp rate in MW/hr
    rampRateToContReserveScalar = contingencyReserveMinutes/minutesPerHour

    return (regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile,
        regElig, regCostFrac, rampRateToRegReserveScalar, rampRateToFlexReserveScalar,
        rampRateToContReserveScalar)

# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ##### MASTER FUNCTION #########################################################
# ###############################################################################
def masterFunction():
    # Import key parameters:
    (case_to_run, greenField, includeRes, useCO2Price, runCE, ceOps, stoInCE, seasStoInCE, ucOrED, numBlocks,
        daysPerBlock, daysPerPeak, fullYearCE, incDACS, incNuc,
        states, powerSystems, compressFleet, fuelPrices, co2Redux2050, co2Ems2020, startYear,
        endYear, yearStepCE, retirementCFCutoff, retireByAge, planningReserveMargin,
        discountRate, annualDemandGrowth, stoMkts, tzAnalysis, maxCapPerTech, runCE, runFirstYear,
        demandYear, ptEligRetCF, incITC, stoMinSOC, initSOCFraction, reDownFactor, demandShifter,
        demandShiftingBlock, run_on_gl, zeroSys, negSys, planningDACs, elect_demand) = setKeyParameters()

    (regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile, regElig, regCostFrac,
        rrToRegTime, rrToFlexTime, rrToContTime) = defineReserveParameters(stoMkts)

    if zeroSys: sc_name = "zeroSys"
    elif negSys: sc_name = "negSys"
    if planningDACs == 1: dac_sc_name = "noDAC"
    elif planningDACs == 2: dac_sc_name = "lateDAC"
    elif planningDACs == 3: dac_sc_name = "earlyDAC"
    if case_to_run == 1: case_name = "reference"
    elif case_to_run == 2: case_name = "lNuclear"
    elif case_to_run == 3: case_name = "lNuclearCCS"
    elif case_to_run == 4: case_name = "lH2"

    if elect_demand == 1: high_elect = "highElectrification"
    elif elect_demand == 0: high_elect = ""

    # Run dispatch and/or CE in years
    for currYear in range(startYear, endYear, yearStepCE):
        # Create results directory
        resultsDir = ('ResultsDispatch' + str(startYear) + '_' + sc_name + '_' + dac_sc_name + '_' + case_name + '_' + high_elect) if startYear == currYear else ('ResultsC' + str(co2Redux2050) + '_' + sc_name + '_' + dac_sc_name + '_' + case_name + '_' + high_elect)
        if not os.path.exists(resultsDir): os.makedirs(resultsDir)

        # Setup initial fleet and demand
        if elect_demand == 0:
            if currYear == startYear:
                (genFleet, demandProfile) = getInitialFleetAndDemand(states, powerSystems,
                    startYear, fuelPrices, elect_demand, currYear, compressFleet, resultsDir, regElig, regCostFrac, demandYear,
                    stoMinSOC, greenField)
        if elect_demand == 1:
            if currYear == startYear:
                (genFleet, demandProfile) = getInitialFleetAndDemand(states, powerSystems,
                    startYear, fuelPrices, elect_demand, currYear, compressFleet, resultsDir, regElig, regCostFrac, demandYear,
                    stoMinSOC, greenField)
            else:
                (genFleetNotUsed, demandProfile) = getInitialFleetAndDemand(states, powerSystems,
                                                                 startYear, fuelPrices, elect_demand, currYear, compressFleet, resultsDir, regElig, regCostFrac, demandYear,
                                                                 stoMinSOC, greenField)

        # Set CO2 cap and demand for year
        # currCo2Cap = co2Ems2020 - (co2Ems2020*co2Redux2050*(currYear-2020)/(2050-2020))
        currCo2Cap = co2Ems2020 - (co2Ems2020 * co2Redux2050 * (currYear - 2020) / (2050 - 2020))

        if zeroSys and planningDACs == 2:
            if currYear == 2020 or currYear == 2030 or currYear == 2040:
                incDACS = False
            elif currYear == 2050:
                incDACS = True

        if negSys and planningDACs == 2:
            if currYear == 2020 or currYear == 2030 or currYear == 2040:
                incDACS = False
            if currYear == 2050:
                currCo2Cap = -1e8
                incDACS = True
        elif negSys and planningDACs == 3:
            if currYear == 2050:
                currCo2Cap = -1e8
                incDACS = True

        print('Entering year ', currYear, ' with CO2 cap (million tons):', round(currCo2Cap/1e6))
        demandWithGrowth = scaleDemandForGrowthAndEE(demandProfile, annualDemandGrowth, demandYear, currYear, elect_demand)

        # Run CE
        if currYear > startYear and runCE:
            print('Starting CE')
            if currYear == startYear + yearStepCE:  #initialize results & inputs
                priorCEModel, priorHoursCE, genFleetPriorCE = None, None, None
                ceBuilds, ceStoEBuilds, retiredUnitsByEcon, retiredUnitsByAge = [['TechnologyType']], [['TechnologyType']], [['ORIS+UnitID']], []
            (genFleet, genFleetNoRetiredUnits, genFleetPriorCE, priorCEModel,
                priorHoursCE) = runCapacityExpansion(genFleet, demandWithGrowth,
                startYear, currYear, endYear, planningReserveMargin, discountRate,
                fuelPrices, states, currCo2Cap, numBlocks, daysPerBlock, daysPerPeak, fullYearCE, retirementCFCutoff, retireByAge,
                tzAnalysis, resultsDir, ceBuilds, ceStoEBuilds, retiredUnitsByEcon, retiredUnitsByAge, maxCapPerTech,
                regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile, rrToRegTime,
                rrToFlexTime, rrToContTime, regElig, regCostFrac, ptEligRetCF,
                genFleetPriorCE, priorCEModel, priorHoursCE, incITC, demandYear,
                stoInCE, seasStoInCE, ceOps, stoMkts, initSOCFraction, includeRes, reDownFactor, incDACS, incNuc, demandShifter, demandShiftingBlock, run_on_gl,
                case_to_run, zeroSys, planningDACs, elect_demand)

        # Run dispatch
        if ucOrED != 'None':
            print('Starting dispatch')
            if ((currYear == startYear and runFirstYear) or (currYear > startYear)):
                if (currYear == startYear) or (runFirstYear == False and currYear == startYear + yearStepCE):
                    genFleetNoRetiredUnits = genFleet
                runDispatch(genFleetNoRetiredUnits, demandWithGrowth, currYear, demandShifter, demandShiftingBlock, fuelPrices,
                    currCo2Cap, useCO2Price, tzAnalysis, resultsDir, stoMkts, demandYear,
                    regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile, includeRes,
                    rrToRegTime, rrToFlexTime, rrToContTime, regCostFrac, ucOrED, initSOCFraction, includeRes)

    results_summary(case_to_run, zeroSys, planningDACs, elect_demand)

# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ###### SET UP INITIAL FLEET AND DEMAND ########################################
# ###############################################################################
def getInitialFleetAndDemand(states, powerSystems, startYear, fuelPrices, elect_demand, currYear,
            compressFleet, resultsDir, regElig, regCostFrac, demandYear, stoMinSOC, greenField, stoEff=0.81):
    genFleet = setupGeneratorFleet(states, powerSystems, startYear,
            fuelPrices, compressFleet, regElig, regCostFrac, stoEff, stoMinSOC)
    # If running greenfield, get rid of existing generator fleet but keep a very small
    # NG, wind, & solar plant to allow rest of script to run.
    if greenField: genFleet = stripDownGenFleet(genFleet, greenField)
    if elect_demand == 0:
        demand = importHourlyERCOTDemand(demandYear)
    elif elect_demand == 1:
        demand = importHourlyEFSDemand(currYear)

    write2dListToCSV([demand], os.path.join(resultsDir, 'demandInitial.csv'))

    # If running greenfield, skip step where get rid of hydro (since none in fleet).
    if not greenField: (genFleet, demand) = removeHydroFromFleetAndDemand(genFleet, demand)
    genFleet.to_csv(os.path.join(resultsDir, 'genFleetInitial.csv'))

    return (genFleet, demand)

# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ###### RUN CAPACITY EXPANSION #################################################
# ###############################################################################
def runCapacityExpansion(genFleet, demandWithGrowth, startYear, currYear, endYear,
        planningReserveMargin, discountRate, fuelPrices, states, currCo2Cap, numBlocks,
        daysPerBlock, daysPerPeak, fullYearCE, retirementCFCutoff, retireByAge, tzAnalysis, resultsDirOrig,
        ceBuilds, ceStoEBuilds, retiredUnitsByEcon, retiredUnitsByAge, maxCapPerTech, regLoadFrac,
        contLoadFrac, regErrorPercentile, flexErrorPercentile, rrToRegTime, rrToFlexTime,
        rrToContTime, regElig, regCostFrac, ptEligRetCF, genFleetPriorCE, priorCEModel,
        priorHoursCE, incITC, demandYear, stoInCE, seasStoInCE, ceOps, stoMkts, initSOCFraction,
        includeRes, reDownFactor, incDACS, incNuc, demandShifter, demandShiftingBlock, run_on_gl,
        case_to_run, zeroSys, planningDACs, elect_demand):

    resultsDir = os.path.join(resultsDirOrig, 'CE')

    if not os.path.exists(resultsDir): os.makedirs(resultsDir)
    print('Entering CE loop for year ' + str(currYear))
    write2dListToCSV([[currCo2Cap]], os.path.join(resultsDir, 'co2CapCE' + str(currYear) + '.csv'))
    newTechsCE = getNewTechs(regElig, regCostFrac, currYear, incITC, stoInCE, seasStoInCE, fuelPrices, incDACS, incNuc)
    genFleet = updateFuelPricesAndCosts(genFleet, currYear, fuelPrices, regCostFrac)

    if priorCEModel != None:                    # if not in first CE loop
        unitsRetireCFPriorCE, genFleet = retireUnitsCFPriorCE(genFleet, genFleetPriorCE, retirementCFCutoff,
            priorCEModel, priorHoursCE, mwToGW, ptEligRetCF, currYear, retiredUnitsByEcon)
        write2dListToCSV([unitsRetireCFPriorCE], os.path.join(resultsDir, 'genRetirementsEconCEPrior' + str(currYear) + '.csv'))
    genFleet, genFleetForCE = createFleetForCurrentCELoop(genFleet, currYear, retiredUnitsByAge, retireByAge)

    print('Units that retire due to age in ' + str(currYear) + ':', retiredUnitsByAge)
    genFleetForCE.to_csv(os.path.join(resultsDir, 'genFleetForCEPreRECombine' + str(currYear) + '.csv'))
    genFleetForCE = combineWindSolarStoPlants(genFleet)
    genFleetForCE.to_csv(os.path.join(resultsDir, 'genFleetForCE' + str(currYear) + '.csv'))

    # Get renewable CFs from MERRA data
    print('Loading RE data')
    hourlyWindGen, hourlySolarGen = getREGen(genFleet, tzAnalysis, demandYear)
    hourlyWindGen.to_csv(path.join(resultsDir, 'windGenFullYrCE' + str(currYear) + '.csv'))
    hourlySolarGen.to_csv(path.join(resultsDir, 'solarGenFullYrCE' + str(currYear) + '.csv'))
    netDemand = np.array(demandWithGrowth) - hourlyWindGen.sum(axis=1).values - hourlySolarGen.sum(axis=1).values
    write2dListToCSV([demandWithGrowth], os.path.join(resultsDir, 'demandFullYrCE' + str(currYear) + '.csv'))
    np.savetxt(path.join(resultsDir, 'netDemandFullYrCE' + str(currYear) + '.csv'), netDemand, delimiter=',')

    # Get blocks of demand and corresponding hours for CE model
    (demandCE, hourlyWindGenCE, hourlySolarGenCE, hoursForCE, hrsByBlock, planningReserve,
        blockWeights, socScalars, peakDemandHour, blockNamesChronoList, lastRepBlockNames,
        specialBlocksPrior) = getDemandForCE(demandWithGrowth, netDemand, hourlyWindGen,
        hourlySolarGen, daysPerBlock, daysPerPeak, fullYearCE, currYear, resultsDir, numBlocks, demandYear, planningReserveMargin)

    for l, n in zip([demandCE, hoursForCE, hourlyWindGenCE, hourlySolarGenCE, [planningReserve]], ['demand', 'hours', 'windGen', 'solarGen', 'planningReserve']):
        write2dListToCSV([l], os.path.join(resultsDir, n + 'CE' + str(currYear) + '.csv'))

    # Get CFs for new wind and solar sites and add wind & solar sites to newTechs
    newCfs = getNewRenewableCFs(genFleet, tzAnalysis, demandYear, reDownFactor)
    newCfsCE = newCfs.iloc[[hr-1 for hr in hoursForCE]]                         # -1 b/c hoursForCE is 1-8760
    newCfs.to_csv(path.join(resultsDir, 'windAndSolarNewCFs' + str(currYear) +'.csv')), newCfsCE.to_csv(path.join(resultsDir, 'windAndSolarNewCFsCE' + str(currYear) + '.csv'))
    newTechsCE = addWSSitesToNewTechs(newCfs, newTechsCE)
    newTechsCE.to_csv(path.join(resultsDir, 'newTechsCE' + str(currYear) + '.csv'))

    # Initialize which generators are on or off at start of each block of hours
    onOffInitialEachPeriod = initializeOnOffExistingGens(genFleetForCE, hrsByBlock, netDemand)

    # Set reserves for existing and incremental reserves for new generators
    print('Calculating reserves')
    if includeRes:
        reserves, resComps = calcWWSISReserves(hourlyWindGen, hourlySolarGen, demandWithGrowth, regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile)
        regUpInc, flexInc = getIncResForAddedRE(newCfs, regErrorPercentile, flexErrorPercentile)
    else:
        reserves, resComps, regUpInc, flexInc = createEmptyReserveDfs(hourlyWindGen, newCfs)
    reservesCE, regUpIncCE, flexIncCE = reserves.iloc[[hr-1 for hr in hoursForCE]], regUpInc.iloc[[hr-1 for hr in hoursForCE]], flexInc.iloc[[hr-1 for hr in hoursForCE]]       # -1 b/c hoursForCE is 1-8760
    for df, name in zip([reserves, resComps, regUpInc, flexInc, reservesCE, regUpIncCE, flexIncCE], ['res', 'resComps', 'regUpInc', 'flexInc', 'resCE', 'regUpIncCE', 'flexIncCE']):
        df.to_csv(path.join(resultsDir, name+str(currYear) + '.csv'))

    ########## RUN CAPACITY EXPANSION
    print('Running CE for ' + str(currYear))
    ws, db, gamsFileDir = createGAMSWorkspaceAndDatabase(run_on_gl)
    writeTimeDependentConstraints(blockNamesChronoList, stoInCE, seasStoInCE, gamsFileDir, ceOps, lastRepBlockNames, specialBlocksPrior)
    writeBuildVariable(ceOps, gamsFileDir)
    genSet, hourSet, hourSymbols = edAndUCSharedFeatures(db, genFleetForCE, hoursForCE, demandCE,
        reservesCE, demandShifter, demandShiftingBlock, rrToRegTime, rrToFlexTime, rrToContTime, 0, hourlySolarGenCE, hourlyWindGenCE)  # 0 is for co2Price
    stoGenSet, stoGenSymbols = storageSetsParamsVariables(db, genFleetForCE, stoMkts)
    stoTechSet, stoTechSymbols = ceSharedFeatures(db, peakDemandHour, genFleetForCE, newTechsCE, planningReserve, discountRate,
            currCo2Cap, hourSet, hourSymbols, newCfsCE, maxCapPerTech, regUpIncCE, flexIncCE, stoMkts, incDACS)

    if ceOps == 'UC': ucFeatures(db, genFleetForCE, genSet)
    ceTimeDependentConstraints(db, hrsByBlock, blockWeights, socScalars, ceOps, onOffInitialEachPeriod,
            genSet, genFleetForCE, stoGenSet, stoGenSymbols, blockNamesChronoList, seasStoInCE,
            newTechsCE, stoTechSet, stoTechSymbols, initSOCFraction)
    capacExpModel, ms, ss = runGAMS('CEWith{o}.gms'.format(o=ceOps), ws, db)

    # ############ SAVE AND PROCESS CE RESULTS
    write2dListToCSV([['ms', 'ss'], [ms, ss]], os.path.join(resultsDir, 'msAndSsCE' + str(currYear) + '.csv'))
    saveCapacExpOperationalData(capacExpModel, genFleetForCE, newTechsCE, hoursForCE, resultsDir, 'CE', currYear)
    newGenerators, newStoECap = saveCEBuilds(ceBuilds, ceStoEBuilds, capacExpModel, currYear)
    genFleet = addNewGensToFleet(genFleet, newGenerators, newStoECap, newTechsCE, currYear)
    genFleet = selectAndMarkUnitsRetiredByCE(genFleet, retirementCFCutoff, capacExpModel,
        currYear, retiredUnitsByEcon, hoursForCE, retiredUnitsByAge, netDemand, newCfs, ptEligRetCF)
    genFleet.to_csv(os.path.join(resultsDir, 'genFleetAfterCE' + str(currYear) + '.csv'))
    writeCEInfoToCSVs(ceBuilds, retiredUnitsByEcon, retiredUnitsByAge, resultsDir, currYear)

    # Save gen fleet filtering retired units for dispatch
    genFleetNoRetiredUnits = getOnlineGenFleet(genFleet, currYear)
    genFleetNoRetiredUnits.to_csv(os.path.join(resultsDir, 'genFleetForDispatch' + str(currYear) + '.csv'))

    # results_summary(case_to_run, zeroSys, planningDACs, elect_demand)
    return (genFleet, genFleetNoRetiredUnits, genFleetForCE, capacExpModel, hoursForCE)

# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ###### RUN DISPATCH ###########################################################
# ###############################################################################
def runDispatch(genFleet, hourlyDemand, currYear, demandShifter, demandShiftingBlock, run_on_gl, fuelPrices, currCo2Cap, useCO2Price,
        tzAnalysis, resultsDir, stoMkts, demandYear, regLoadFrac, contLoadFrac,
        regErrorPercentile, flexErrorPercentile, rrToRegTime, rrToFlexTime, rrToContTime,
        regCostFrac, ucOrED, initSOCFraction, includeRes, firstDay=0, lastDay=364, daysOpt=364, daysLA=1):
    resultsDir = os.path.join(resultsDir, 'Dispatch')
    if not os.path.exists(resultsDir): os.makedirs(resultsDir)
    print('Entering dispatch for year ' + str(currYear))

    # Get renewable generation
    hourlyWindGen, hourlySolarGen = getREGen(genFleet, tzAnalysis, demandYear)
    hourlyWindGen.to_csv(path.join(resultsDir, 'windGenDispatch'+str(currYear)+'.csv'))
    hourlySolarGen.to_csv(path.join(resultsDir, 'solarGenDispatch'+str(currYear)+'.csv'))
    write2dListToCSV([hourlyDemand], os.path.join(resultsDir, 'demandDispatch' + str(currYear) + '.csv'))

    # Get reserves
    if includeRes:
        hourlyReserves, resComps = calcWWSISReserves(hourlyWindGen, hourlySolarGen, hourlyDemand,
                                regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile)
    else:
        hourlyReserves, resComps, regUpInc, flexInc = createEmptyReserveDfs(hourlyWindGen)
    hourlyReserves.to_csv(path.join(resultsDir, 'resDispatch'+str(currYear)+'.csv'))
    resComps.to_csv(path.join(resultsDir, 'resCompsDispatch'+str(currYear)+'.csv'))

    # Update fuel prices
    genFleet = updateFuelPricesAndCosts(genFleet, currYear, fuelPrices, regCostFrac)

    # Combine wind & solar generators
    genFleet = combineWindSolarStoPlants(genFleet)
    genFleet.to_csv(path.join(resultsDir, 'genFleetDispatch' + str(currYear) + '.csv'))

    # Set CO2 price
    co2Price = convertCo2CapToPrice(genFleet, hourlyWindGen, hourlySolarGen, hourlyDemand, currCo2Cap) if useCO2Price else 0
    print('CO2 price:', co2Price, '$/ton')
    write2dListToCSV([[co2Price]], path.join(resultsDir, 'co2PriceDispatch' + str(currYear) + '.csv'))

    # Setup result dataframes
    daysToRun = range(firstDay, lastDay, daysOpt)
    dispatchResults = dict()
    for k in ['vGen', 'vRegup', 'vFlex', 'vCont', 'vTurnon', 'vTurnoff', 'vOnoroff', 'vCharge', 'vStateofcharge']:
        dispatchResults[k] = pd.DataFrame(columns=genFleet['GAMS Symbol'], index=hourlyWindGen.index)
    sysResults = pd.DataFrame(columns=['vNse', 'vZ', 'mcGen', 'mcRegup', 'mcFlex', 'mcCont'], index=hourlyWindGen.index)
    msAndSs = pd.DataFrame(columns=['ms', 'ss'], index=daysToRun)

    # Run dispatch for each day of year
    for day in daysToRun:
        # Get time series for current days
        hours = list(range(day*24, (day + daysOpt + daysLA)*24))
        dayDtIdx = hourlyWindGen.index[hours]
        wind, solar = hourlyWindGen.loc[dayDtIdx].sum(axis=1).values, hourlySolarGen.loc[dayDtIdx].sum(axis=1).values
        demand = [hourlyDemand[i] for i in hours]
        reserves = hourlyReserves.loc[dayDtIdx]

        # Set initial conditions (all returned as pd Series w/ gen index)
        if day == firstDay:  # first day, therefore no initial conditions defined. MW energy values
            (onOffInitial, genAboveMinInitial, mdtCarriedInitial,
                socInitial) = setInitCondsFirstDay(genFleet, initSOCFraction)
        else: # MW energy values
            (onOffInitial, genAboveMinInitial, mdtCarriedInitial,
                socInitial) = setInitConds(dayDtIdx, genFleet, dispatchResults)
        # ############# RUN DISPATCH
        print('Running ' + ucOrED + ' for ' + str(day))
        ws, db, gamsFileDir = createGAMSWorkspaceAndDatabase(run_on_gl)
        genSet, hourSet, hourSymbols = edAndUCSharedFeatures(db, genFleet, hours,
            demand, reserves, demandShifter, demandShiftingBlock, rrToRegTime, rrToFlexTime, rrToContTime, 0, solar, wind)  # 0 is for co2Price
        stoGenSet, stoGenSymbols = storageSetsParamsVariables(db, genFleet, stoMkts)
        if ucOrED == 'UC': 
            ucFeatures(db, genFleet, genSet)
            uc(db, stoGenSet, genSet, socInitial, onOffInitial, genAboveMinInitial, mdtCarriedInitial)
        else:
            ed(db, socInitial, stoGenSet)
        opsModel, ms, ss = runGAMS(ucOrED + '.gms', ws, db)

        # ########### SAVE RESULTS
        msAndSs.loc[day] = [ms, ss]
        dispatchResults, sysResults = saveDispatchResults(dispatchResults, sysResults, opsModel, hourlyWindGen.index, dayDtIdx)
        writeDispatchResults(dispatchResults, sysResults, msAndSs, resultsDir, currYear)

# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ################## GAMS FUNCTIONS #############################################
# ###############################################################################
def createGAMSWorkspaceAndDatabase(run_on_gl):
    # currDir = os.getcwd()
    if run_on_gl == 2:
        gamsFileDir = r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\Model\GAMS"
        gamsSysDir = r"C:\GAMS\win64\30.2"
    elif run_on_gl == 1:
        gamsFileDir = '/home/anph/projects/NETs/Model/GAMS'
        gamsSysDir = '/home/anph/gams_35_1'

    ws = GamsWorkspace(working_directory=gamsFileDir, system_directory=gamsSysDir)
    db = ws.add_database()
    return ws, db, gamsFileDir

def runGAMS(gamsFilename, ws, db):
    t0 = time.time()
    model = ws.add_job_from_file(gamsFilename)
    opts = GamsOptions(ws)
    opts.defines['gdxincname'] = db.name
    model.run(opts, databases=db)
    ms, ss = model.out_db['pModelstat'].find_record().value, model.out_db['pSolvestat'].find_record().value
    if (int(ms) != 8 and int(ms) != 1) or int(ss) != 1: print('Modelstat & solvestat:', ms, ' & ', ss, ' (ms1 global opt, ms8 int soln, ss1 normal)')
    print('Time (mins) for GAMS run: ' + str(round((time.time()-t0)/60)))
    return model, ms, ss

def edAndUCSharedFeatures(db, genFleet, hours, demand, reserves, demandShifter, demandShiftingBlock, rrToRegTime, rrToFlexTime,
        rrToContTime, co2Price, hourlySolarGen, hourlyWindGen, cnse=10000):
    # Sets
    genSet = addGeneratorSets(db, genFleet)
    hourSet, hourSymbols = addHourSet(db, hours)

    # Parameters
    # Demand and reserves
    addDemandParam(db, demand, hourSet, hourSymbols, demandShifter, demandShiftingBlock, mwToGW)
    addReserveParameters(db, reserves, rrToRegTime, rrToFlexTime, rrToContTime, hourSet, hourSymbols, mwToGW)

    # CO2 cap or price
    addCo2Price(db, co2Price)

    # Generators
    addGenParams(db, genFleet, genSet, mwToGW, lbToShortTon)
    addExistingRenewableMaxGenParams(db, hourSet, hourSymbols, hourlySolarGen, hourlyWindGen, mwToGW)
    addSpinReserveEligibility(db, genFleet, genSet)
    addCostNonservedEnergy(db, cnse)
    return genSet, hourSet, hourSymbols

def storageSetsParamsVariables(db, genFleet, stoMkts):
    (stoGenSet, stoGenSymbols) = addStoGenSets(db, genFleet)
    addStorageParams(db, genFleet, stoGenSet, stoGenSymbols, mwToGW, stoMkts)
    return stoGenSet, stoGenSymbols

def ed(db, socInitial, stoGenSet):
    addStorageInitSOC(db, socInitial, stoGenSet, mwToGW)

def ucFeatures(db, genFleet, genSet):
    addGenUCParams(db, genFleet, genSet, mwToGW)
    
def uc(db, stoGenSet, genSet, socInitial, onOffInitial, genAboveMinInitial, mdtCarriedInitial):
    addStorageInitSOC(db, socInitial, stoGenSet, mwToGW)
    addEguInitialConditions(db, genSet, onOffInitial, genAboveMinInitial, mdtCarriedInitial, mwToGW)

def ceSharedFeatures(db, peakDemandHour, genFleet, newTechs, planningReserve, discountRate,
        co2Cap, hourSet, hourSymbols, newCfs, maxCapPerTech, regUpInc, flexInc, stoMkts, incDACS):

    # Sets
    addPeakHourSubset(db, peakDemandHour)
    addStorageSubsets(db, genFleet)
    (techSet, renewTechSet, stoTechSet, stoTechSymbols, thermalSet, dacsSet, CCSSet) = addNewTechsSets(db, newTechs, incDACS)

    # Long-term planning parameters
    addPlanningReserveParam(db, planningReserve, mwToGW)
    addDiscountRateParam(db, discountRate)
    addCO2Cap(db, co2Cap)

    # New tech parameters
    addGenParams(db, newTechs, techSet, mwToGW, lbToShortTon, True)
    addTechCostParams(db, newTechs, techSet, stoTechSet, mwToGW)
    addRenewTechCFParams(db, renewTechSet, hourSet, hourSymbols, newCfs)
    addMaxNewBuilds(db, newTechs, thermalSet, stoTechSet, dacsSet, CCSSet, maxCapPerTech, mwToGW)
    addGenUCParams(db, newTechs, techSet, mwToGW, True)
    addResIncParams(db, regUpInc, flexInc, renewTechSet, hourSet, hourSymbols)
    addSpinReserveEligibility(db, newTechs, techSet, True)
    addStorageParams(db, newTechs, stoTechSet, stoTechSymbols, mwToGW, stoMkts, True)
    return stoTechSet, stoTechSymbols

def ceTimeDependentConstraints(db, hrsByBlock, blockWeights, socScalars, ceOps, onOffInitialEachPeriod,
        genSet, genFleet, stoGenSet, stoGenSymbols, blockNamesChronoList, seasStoInCE,
        newTechs, stoTechSet, stoTechSymbols, initSOCFraction):
    addHourSubsets(db, hrsByBlock)
    addSeasonDemandWeights(db, blockWeights)
    addBlockSOCScalars(db, socScalars)
    if ceOps == 'UC': addInitialOnOffForEachBlock(db, onOffInitialEachPeriod, genSet)
    addStoInitSOCCE(db, genFleet, stoGenSet, stoGenSymbols, mwToGW, blockNamesChronoList, seasStoInCE, initSOCFraction)
    addStoInitSOCCE(db, newTechs, stoTechSet, stoTechSymbols, mwToGW, blockNamesChronoList, seasStoInCE, initSOCFraction, True)

################################################################################
# def checkfunction(ceModel,hoursForCE,gens,resultsDir,modelName,year,genFleetForCE,newTechsCE):
#  sysResults = saveSystemResults(ceModel,hoursForCE)
#  resultsCEgen = saveGeneratorResults(ceModel,gens,hoursForCE,resultsDir,modelName,year,newTechs=False)
# result = saveCapacExpOperationalData(ceModel,genFleetForCE,newTechsCE,hoursForCE,resultsDir,modelName,year)
#    resultsCEgen.to_csv(r'C:\Users\atpha\Documents\Postdocs\Projects\NETs\Model\resultsCEgen.txt')
#   sysResults.to_csv(r'C:\Users\atpha\Documents\Postdocs\Projects\NETs\Model\sysResults.txt')
#   result.to_csv(r'C:\Users\atpha\Documents\Postdocs\Projects\NETs\Model\sysResults.txt')

################################################################################
################################################################################
################################################################################

masterFunction()

