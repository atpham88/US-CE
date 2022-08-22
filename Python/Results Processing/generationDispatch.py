
import pandas as pd
import numpy as np

def genDispatch(results_dir_temp, techCase, planningScr, interConn):
    if interConn == 'EI':
        finalCap = '-724'
    elif interConn == 'ERCOT':
        finalCap = '-90'

    if planningScr == 'NE2020':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2020NEin2020_' + techCase.lower() + '_TrueREFERENCE\\2050CO2Cap'+finalCap+'\\CE\\'
    elif planningScr == 'NE2050':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2020NEin2050_' + techCase.lower() + '_TrueREFERENCE\\2060CO2Cap'+finalCap+'\\CE\\'
    elif planningScr == 'NE2051':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2051NEin2050_' + techCase.lower() + '_TrueREFERENCE\\2060CO2Cap'+finalCap+'\\CE\\'

    if planningScr == 'NE2020':
        gen_data_new = pd.read_csv(results_dir +'vGentechCE2050.csv')
        gen_data_existing = pd.read_csv(results_dir + 'vGenCE2050.csv')
        # read in block weights:
        bw = pd.read_csv(results_dir + 'hoursCEByBlock2050.csv')
    elif planningScr == 'NE2050' or planningScr == 'NE2051':
        gen_data_new = pd.read_csv(results_dir + 'vGentechCE2060.csv')
        gen_data_existing = pd.read_csv(results_dir + 'vGenCE2060.csv')
        # read in block weights:
        bw = pd.read_csv(results_dir + 'hoursCEByBlock2060.csv')

    bw_value = pd.read_csv(results_dir + 'blockWeightsCE2050.csv')

    bw['block_c'] = [int(x) + 1 if len(x) == 1 else 0 for x in bw['block']]
    bw_u = bw.drop_duplicates('block_c', keep='last')
    bw_3 = bw_u['block_c'].max()
    bw_u = bw_u.loc[bw_u['block_c'] != bw_u['block_c'].max()]
    bw_2 = bw_u['block_c'].max()
    bw_u = bw_u.loc[bw_u['block_c'] != bw_u['block_c'].max()]
    bw_1 = bw_u['block_c'].max()
    bw_u = bw_u.loc[bw_u['block_c'] != bw_u['block_c'].max()]
    bw_0 = bw_u['block_c'].max()

    bw['block0'] = [1 if x == str(bw_0 - 1) else 0 for x in bw['block']]
    bw['block0'] = bw['block0'] * bw_value['blockWeight'][0]
    bw['block1'] = [1 if x == str(bw_1 - 1) else 0 for x in bw['block']]
    bw['block1'] = bw['block1'] * bw_value['blockWeight'][1]
    bw['block2'] = [1 if x == str(bw_2 - 1) else 0 for x in bw['block']]
    bw['block2'] = bw['block2'] * bw_value['blockWeight'][2]
    bw['block3'] = [1 if x == str(bw_3 - 1) else 0 for x in bw['block']]
    bw['block3'] = bw['block3'] * bw_value['blockWeight'][3]

    bw['block_c'] = bw['block0'] + bw['block1'] + bw['block2'] + bw['block3']
    bw['block_c'] = [1 if x == 0 else x for x in bw['block_c']]

    # New generation:
    gen_data_new.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    gen_data_new = gen_data_new.T
    gen_data_new.columns = gen_data_new.iloc[0]
    gen_data_new = gen_data_new.drop(gen_data_new.index[0])
    gen_data_new = gen_data_new.reset_index()
    gen_data_new.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    CoalCCS_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CCCCS_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    CC_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('Combined Cycle')]
    battery_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('Hydrogen')]
    nuclear_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('Nuclear')]
    dac_GenN = gen_data_new.loc[gen_data_new['GAMS Symbol'].str.contains('DAC')]
    solar_GenN = gen_data_new[gen_data_new['GAMS Symbol'].str.contains('solar')]
    wind_GenN = gen_data_new[gen_data_new['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN = CoalCCS_GenN.drop('GAMS Symbol', axis=1)
    CoalCCS_GenN = CoalCCS_GenN.sum().multiply(np.array(bw['block_c']))
    CCCCS_GenN = CCCCS_GenN.drop('GAMS Symbol', axis=1)
    CCCCS_GenN = CCCCS_GenN.sum().multiply(np.array(bw['block_c']))
    CC_GenN = CC_GenN.drop('GAMS Symbol', axis=1)
    CC_GenN = CC_GenN.sum().multiply(np.array(bw['block_c'])) - CCCCS_GenN
    battery_GenN = battery_GenN.drop('GAMS Symbol', axis=1)
    battery_GenN = battery_GenN.sum().multiply(np.array(bw['block_c']))
    hydrogen_GenN = hydrogen_GenN.drop('GAMS Symbol', axis=1)
    hydrogen_GenN = hydrogen_GenN.sum().multiply(np.array(bw['block_c']))
    nuclear_GenN = nuclear_GenN.drop('GAMS Symbol', axis=1)
    nuclear_GenN = nuclear_GenN.sum().multiply(np.array(bw['block_c']))
    dac_GenN = dac_GenN.drop('GAMS Symbol', axis=1)
    dac_GenN = dac_GenN.sum().multiply(np.array(bw['block_c']))
    solar_GenN = solar_GenN.drop('GAMS Symbol', axis=1)
    solar_GenN = solar_GenN.sum().multiply(np.array(bw['block_c']))
    wind_GenN = wind_GenN.drop('GAMS Symbol', axis=1)
    wind_GenN = wind_GenN.sum().multiply(np.array(bw['block_c']))

    CoalCCS_GenN = CoalCCS_GenN.sum()/1000
    CCCCS_GenN = CCCCS_GenN.sum()/1000
    CC_GenN = CC_GenN.sum()/1000
    battery_GenN = battery_GenN.sum()/1000
    hydrogen_GenN = hydrogen_GenN.sum()/1000
    nuclear_GenN = nuclear_GenN.sum() / 1000
    dac_GenN = dac_GenN.sum()/1000
    solar_GenN = solar_GenN.sum()/1000
    wind_GenN = wind_GenN.sum()/1000

    # Existing generation:
    if planningScr == 'NE2020':
        planttype = pd.read_csv(results_dir + 'genFleetForCE2050.csv')
    elif planningScr == 'NE2050' or planningScr == 'NE2051':
        planttype = pd.read_csv(results_dir + 'genFleetForCE2060.csv')

    gen_data_existing.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    gen_data_existing = gen_data_existing.T
    gen_data_existing.columns = gen_data_existing.iloc[0]
    gen_data_existing = gen_data_existing.drop(gen_data_existing.index[0])
    gen_data_existing = gen_data_existing.reset_index()
    gen_data_existing.rename(columns={'index': 'Unit'}, inplace=True)

    planttype = planttype[['PlantType', 'region']]
    #gen_data_existing['Total Gen'] = gen_data_existing.iloc[:, 1:].sum(axis=1)
    #gen_data_existing = gen_data_existing[['Total Gen']]
    gen_data_existing['PlantType'] = planttype['PlantType']
    gen_data_existing['region'] = planttype['region']

    Coal_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Coal Steam']
    CC_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Combined Cycle']
    CCCCS_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Combined Cycle CCS']
    CT_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Combustion Turbine']
    OG_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'O/G Steam']
    bio_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Biomass']
    battery_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Batter')]
    hydrogen_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Hydrogen']
    nuclear_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Nuclear']
    dac_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'DAC']
    solarN_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('solar')]
    solarE_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Solar PV']
    windN_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('wind')]
    windE_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Onshore Wind']
    pump_GenE = gen_data_existing.loc[gen_data_existing['PlantType'] == 'Pumped Storage']
    Other1_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Flywheels')]
    Other2_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Fossil Waste')]
    Other3_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Fuel Cell')]
    Other4_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('IGCC')]
    Other5_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Landfill Gas')]
    Other6_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_GenE = gen_data_existing[gen_data_existing['PlantType'].str.contains('Tires')]

    if len(Coal_GenE) > 0:
        Coal_GenE = Coal_GenE.drop(['PlantType', 'region'], axis=1)
        Coal_GenE = Coal_GenE.sum().multiply(np.array(bw['block_c']))
        Coal_GenE = Coal_GenE.sum() / 1000
    else:
        Coal_GenE = 0

    if len(CC_GenE) > 0:
        CC_GenE = CC_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        CC_GenE = CC_GenE.sum().multiply(np.array(bw['block_c']))
        CC_GenE = CC_GenE.sum()/1000
    else:
        CC_GenE = 0

    if len(CCCCS_GenE) > 0:
        CCCCS_GenE = CCCCS_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        CCCCS_GenE = CCCCS_GenE.sum().multiply(np.array(bw['block_c']))
        CCCCS_GenE = CCCCS_GenE.sum()/1000
    else:
        CCCCS_GenE = 0

    if len(CT_GenE) > 0:
        CT_GenE = CT_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        CT_GenE = CT_GenE.sum().multiply(np.array(bw['block_c']))
        CT_GenE = CT_GenE.sum()/1000
    else:
        CT_GenE = 0

    if len(OG_GenE) > 0:
        OG_GenE = OG_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        OG_GenE = OG_GenE.sum().multiply(np.array(bw['block_c']))
        OG_GenE = OG_GenE.sum()/1000
    else:
        OG_GenE = 0

    if len(bio_GenE) > 0:
        bio_GenE = bio_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        bio_GenE = bio_GenE.sum().multiply(np.array(bw['block_c']))
        bio_GenE = bio_GenE.sum()/1000
    else:
        bio_GenE = 0

    if len(battery_GenE) > 0:
        battery_GenE = battery_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        battery_GenE = battery_GenE.sum().multiply(np.array(bw['block_c']))
        battery_GenE = battery_GenE.sum() / 1000
    else:
        battery_GenE = 0

    if len(hydrogen_GenE) > 0:
        hydrogen_GenE = hydrogen_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        hydrogen_GenE = hydrogen_GenE.sum().multiply(np.array(bw['block_c']))
        hydrogen_GenE = hydrogen_GenE.sum() / 1000
    else:
        hydrogen_GenE = 0

    if len(nuclear_GenE) > 0:
        nuclear_GenE = nuclear_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        nuclear_GenE = nuclear_GenE.sum().multiply(np.array(bw['block_c']))
        nuclear_GenE = nuclear_GenE.sum() / 1000
    else:
        nuclear_GenE = 0

    if len(pump_GenE) > 0:
        pump_GenE = pump_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        pump_GenE = pump_GenE.sum().multiply(np.array(bw['block_c']))
        pump_GenE = pump_GenE.sum() / 1000
    else:
        pump_GenE = 0

    if len(dac_GenE) > 0:
        dac_GenE = dac_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        dac_GenE = dac_GenE.sum().multiply(np.array(bw['block_c']))
        dac_GenE = dac_GenE.sum() / 1000
    else:
        dac_GenE = 0

    if len(solarN_GenE) > 0:
        solarN_GenE = solarN_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        solarN_GenE = solarN_GenE.sum().multiply(np.array(bw['block_c']))
        solarN_GenE = solarN_GenE.sum() / 1000
    else:
        solarN_GenE = 0

    if len(solarE_GenE) > 0:
        solarE_GenE = solarE_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        solarE_GenE = solarE_GenE.sum().multiply(np.array(bw['block_c']))
        solarE_GenE = solarE_GenE.sum() / 1000
    else:
        solarE_GenE = 0
    solar_GenE = solarN_GenE + solarE_GenE

    if len(windN_GenE) > 0:
        windN_GenE = windN_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        windN_GenE = windN_GenE.sum().multiply(np.array(bw['block_c']))
        windN_GenE = windN_GenE.sum() / 1000
    else:
        windN_GenE = 0

    if len(windE_GenE) > 0:
        windE_GenE = windE_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        windE_GenE = windE_GenE.sum().multiply(np.array(bw['block_c']))
        windE_GenE = windE_GenE.sum() / 1000
    else:
        windE_GenE = 0
    wind_GenE = windN_GenE + windE_GenE

    if len(Other1_GenE) > 0:
        Other1_GenE = Other1_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other1_GenE = Other1_GenE.sum().multiply(np.array(bw['block_c']))
        Other1_GenE = Other1_GenE.sum() / 1000
    else:
        Other1_GenE = 0

    if len(Other2_GenE) > 0:
        Other2_GenE = Other2_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other2_GenE = Other2_GenE.sum().multiply(np.array(bw['block_c']))
        Other2_GenE = Other2_GenE.sum() / 1000
    else:
        Other2_GenE = 0

    if len(Other3_GenE) > 0:
        Other3_GenE = Other3_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other3_GenE = Other3_GenE.sum().multiply(np.array(bw['block_c']))
        Other3_GenE = Other3_GenE.sum() / 1000
    else:
        Other3_GenE = 0

    if len(Other4_GenE) > 0:
        Other4_GenE = Other4_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other4_GenE = Other4_GenE.sum().multiply(np.array(bw['block_c']))
        Other4_GenE = Other4_GenE.sum() / 1000
    else:
        Other4_GenE = 0

    if len(Other5_GenE) > 0:
        Other5_GenE = Other5_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other5_GenE = Other5_GenE.sum().multiply(np.array(bw['block_c']))
        Other5_GenE = Other5_GenE.sum() / 1000
    else:
        Other5_GenE = 0

    if len(Other6_GenE) > 0:
        Other6_GenE = Other6_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other6_GenE = Other6_GenE.sum().multiply(np.array(bw['block_c']))
        Other6_GenE = Other6_GenE.sum() / 1000
    else:
        Other6_GenE = 0

    if len(Other7_GenE) > 0:
        Other7_GenE = Other7_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other7_GenE = Other7_GenE.sum().multiply(np.array(bw['block_c']))
        Other7_GenE = Other7_GenE.sum() / 1000
    else:
        Other7_GenE = 0

    if len(Other8_GenE) > 0:
        Other8_GenE = Other8_GenE.drop(['Unit', 'PlantType', 'region'], axis=1)
        Other8_GenE = Other8_GenE.sum().multiply(np.array(bw['block_c']))
        Other8_GenE = Other8_GenE.sum() / 1000
    else:
        Other8_GenE = 0

    Others_GenE = Other1_GenE + Other2_GenE + Other3_GenE + Other4_GenE \
                  + Other5_GenE + Other6_GenE + Other7_GenE + Other8_GenE


    Coal_Gen = CoalCCS_GenN + Coal_GenE
    CCCCS_Gen = CCCCS_GenN  + CCCCS_GenE
    CC_Gen = CC_GenN + CC_GenE
    battery_Gen = battery_GenN + battery_GenE
    hydrogen_Gen = hydrogen_GenN + hydrogen_GenE
    nuclear_Gen = nuclear_GenN + nuclear_GenE
    dac_Gen = dac_GenN + dac_GenE
    solar_Gen = solar_GenN + solar_GenE
    wind_Gen = wind_GenN + wind_GenE
    CT_Gen = CT_GenE
    OG_Gen = OG_GenE
    bio_Gen = bio_GenE
    pump_Gen = pump_GenE
    Others_Gen = Others_GenE

    return (Coal_Gen, CCCCS_Gen, CC_Gen, battery_Gen, hydrogen_Gen, nuclear_Gen, dac_Gen, solar_Gen,
            wind_Gen, CT_Gen, OG_Gen, bio_Gen, pump_Gen, Others_Gen)