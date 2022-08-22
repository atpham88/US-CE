
import pandas as pd
import numpy as np

def genDispatchRegions(results_dir_temp, techCase, planningScr, interConn):
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

    # Regional generation:
    if interConn == 'EI':
        CoalCCS_GenN_SERC = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('SERC')]
        CoalCCS_GenN_SERC = CoalCCS_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_NY = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('NY')]
        CoalCCS_GenN_NY = CoalCCS_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_NE = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('NE')]
        CoalCCS_GenN_NE = CoalCCS_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_MISO = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('MISO')]
        CoalCCS_GenN_MISO = CoalCCS_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_PJM = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('PJM')]
        CoalCCS_GenN_PJM = CoalCCS_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_SPP = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('SPP')]
        CoalCCS_GenN_SPP = CoalCCS_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        CCCCS_GenN_SERC = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('SERC')]
        CCCCS_GenN_SERC = CCCCS_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_NY = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('NY')]
        CCCCS_GenN_NY = CCCCS_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_NE = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('NE')]
        CCCCS_GenN_NE = CCCCS_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_MISO = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('MISO')]
        CCCCS_GenN_MISO = CCCCS_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_PJM = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('PJM')]
        CCCCS_GenN_PJM = CCCCS_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_SPP = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('SPP')]
        CCCCS_GenN_SPP = CCCCS_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        CC_GenN_SERC = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('SERC')]
        CC_GenN_SERC = CC_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_SERC
        CC_GenN_NY = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('NY')]
        CC_GenN_NY = CC_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_NY
        CC_GenN_NE = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('NE')]
        CC_GenN_NE = CC_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_NE
        CC_GenN_MISO = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('MISO')]
        CC_GenN_MISO = CC_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_MISO
        CC_GenN_PJM = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('PJM')]
        CC_GenN_PJM = CC_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_PJM
        CC_GenN_SPP = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('SPP')]
        CC_GenN_SPP = CC_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_SPP

        battery_GenN_SERC = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('SERC')]
        battery_GenN_SERC = battery_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_NY = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('NY')]
        battery_GenN_NY = battery_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_NE = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('NE')]
        battery_GenN_NE = battery_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_MISO = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('MISO')]
        battery_GenN_MISO = battery_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_PJM = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('PJM')]
        battery_GenN_PJM = battery_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_SPP = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('SPP')]
        battery_GenN_SPP = battery_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        hydrogen_GenN_SERC = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('SERC')]
        hydrogen_GenN_SERC = hydrogen_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_NY = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('NY')]
        hydrogen_GenN_NY = hydrogen_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_NE = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('NE')]
        hydrogen_GenN_NE = hydrogen_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_MISO = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('MISO')]
        hydrogen_GenN_MISO = hydrogen_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_PJM = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('PJM')]
        hydrogen_GenN_PJM = hydrogen_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_SPP = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('SPP')]
        hydrogen_GenN_SPP = hydrogen_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        nuclear_GenN_SERC = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('SERC')]
        nuclear_GenN_SERC = nuclear_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_NY = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('NY')]
        nuclear_GenN_NY = nuclear_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_NE = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('NE')]
        nuclear_GenN_NE = nuclear_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_MISO = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('MISO')]
        nuclear_GenN_MISO = nuclear_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_PJM = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('PJM')]
        nuclear_GenN_PJM = nuclear_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_SPP = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('SPP')]
        nuclear_GenN_SPP = nuclear_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        dac_GenN_SERC = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('SERC')]
        dac_GenN_SERC = dac_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_NY = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('NY')]
        dac_GenN_NY = dac_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_NE = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('NE')]
        dac_GenN_NE = dac_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_MISO = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('MISO')]
        dac_GenN_MISO = dac_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_PJM = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('PJM')]
        dac_GenN_PJM = dac_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_SPP = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('SPP')]
        dac_GenN_SPP = dac_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        solar_GenN_SERC = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('SERC')]
        solar_GenN_SERC = solar_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_NY = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('NY')]
        solar_GenN_NY = solar_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_NE = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('NE')]
        solar_GenN_NE = solar_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_MISO = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('MISO')]
        solar_GenN_MISO = solar_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_PJM = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('PJM')]
        solar_GenN_PJM = solar_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_SPP = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('SPP')]
        solar_GenN_SPP = solar_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        wind_GenN_SERC = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('SERC')]
        wind_GenN_SERC = wind_GenN_SERC.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_NY = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('NY')]
        wind_GenN_NY = wind_GenN_NY.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_NE = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('NE')]
        wind_GenN_NE = wind_GenN_NE.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_MISO = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('MISO')]
        wind_GenN_MISO = wind_GenN_MISO.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_PJM = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('PJM')]
        wind_GenN_PJM = wind_GenN_PJM.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_SPP = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('SPP')]
        wind_GenN_SPP = wind_GenN_SPP.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        CoalCCS_GenN_SERC = CoalCCS_GenN_SERC.sum().sum() / 1000
        CCCCS_GenN_SERC = CCCCS_GenN_SERC.sum().sum() / 1000
        CC_GenN_SERC = CC_GenN_SERC.sum().sum() / 1000
        battery_GenN_SERC = battery_GenN_SERC.sum().sum() / 1000
        hydrogen_GenN_SERC = hydrogen_GenN_SERC.sum().sum() / 1000
        nuclear_GenN_SERC = nuclear_GenN_SERC.sum().sum() / 1000
        dac_GenN_SERC = dac_GenN_SERC.sum().sum() / 1000
        solar_GenN_SERC = solar_GenN_SERC.sum().sum() / 1000
        wind_GenN_SERC = wind_GenN_SERC.sum().sum() / 1000

        CoalCCS_GenN_NY = CoalCCS_GenN_NY.sum().sum() / 1000
        CCCCS_GenN_NY = CCCCS_GenN_NY.sum().sum() / 1000
        CC_GenN_NY = CC_GenN_NY.sum().sum() / 1000
        battery_GenN_NY = battery_GenN_NY.sum().sum() / 1000
        hydrogen_GenN_NY = hydrogen_GenN_NY.sum().sum() / 1000
        nuclear_GenN_NY = nuclear_GenN_NY.sum().sum() / 1000
        dac_GenN_NY = dac_GenN_NY.sum().sum() / 1000
        solar_GenN_NY = solar_GenN_NY.sum().sum() / 1000
        wind_GenN_NY = wind_GenN_NY.sum().sum() / 1000

        CoalCCS_GenN_NE = CoalCCS_GenN_NE.sum().sum() / 1000
        CCCCS_GenN_NE = CCCCS_GenN_NE.sum().sum() / 1000
        CC_GenN_NE = CC_GenN_NE.sum().sum() / 1000
        battery_GenN_NE = battery_GenN_NE.sum().sum() / 1000
        hydrogen_GenN_NE = hydrogen_GenN_NE.sum().sum() / 1000
        nuclear_GenN_NE = nuclear_GenN_NE.sum().sum()/ 1000
        dac_GenN_NE = dac_GenN_NE.sum().sum() / 1000
        solar_GenN_NE = solar_GenN_NE.sum().sum() / 1000
        wind_GenN_NE = wind_GenN_NE.sum().sum() / 1000

        CoalCCS_GenN_MISO = CoalCCS_GenN_MISO.sum().sum() / 1000
        CCCCS_GenN_MISO = CCCCS_GenN_MISO.sum().sum() / 1000
        CC_GenN_MISO = CC_GenN_MISO.sum().sum() / 1000
        battery_GenN_MISO = battery_GenN_MISO.sum().sum() / 1000
        hydrogen_GenN_MISO = hydrogen_GenN_MISO.sum().sum() / 1000
        nuclear_GenN_MISO = nuclear_GenN_MISO.sum().sum() / 1000
        dac_GenN_MISO = dac_GenN_MISO.sum().sum() / 1000
        solar_GenN_MISO = solar_GenN_MISO.sum().sum() / 1000
        wind_GenN_MISO = wind_GenN_MISO.sum().sum() / 1000

        CoalCCS_GenN_PJM = CoalCCS_GenN_PJM.sum().sum() / 1000
        CCCCS_GenN_PJM = CCCCS_GenN_PJM.sum().sum() / 1000
        CC_GenN_PJM = CC_GenN_PJM.sum().sum() / 1000
        battery_GenN_PJM = battery_GenN_PJM.sum().sum() / 1000
        hydrogen_GenN_PJM = hydrogen_GenN_PJM.sum().sum() / 1000
        nuclear_GenN_PJM = nuclear_GenN_PJM.sum().sum() / 1000
        dac_GenN_PJM = dac_GenN_PJM.sum().sum() / 1000
        solar_GenN_PJM = solar_GenN_PJM.sum().sum() / 1000
        wind_GenN_PJM = wind_GenN_PJM.sum().sum() / 1000

        CoalCCS_GenN_SPP = CoalCCS_GenN_SPP.sum().sum() / 1000
        CCCCS_GenN_SPP = CCCCS_GenN_SPP.sum().sum() / 1000
        CC_GenN_SPP = CC_GenN_SPP.sum().sum() / 1000
        battery_GenN_SPP = battery_GenN_SPP.sum().sum() / 1000
        hydrogen_GenN_SPP = hydrogen_GenN_SPP.sum().sum() / 1000
        nuclear_GenN_SPP = nuclear_GenN_SPP.sum().sum() / 1000
        dac_GenN_SPP = dac_GenN_SPP.sum().sum() / 1000
        solar_GenN_SPP = solar_GenN_SPP.sum().sum() / 1000
        wind_GenN_SPP = wind_GenN_SPP.sum().sum() / 1000

        CoalCCS_GenN_NW = 0
        CoalCCS_GenN_SW = 0
        CoalCCS_GenN_NOE = 0
        CoalCCS_GenN_SE = 0

        CCCCS_GenN_NW = 0
        CCCCS_GenN_SW = 0
        CCCCS_GenN_NOE = 0
        CCCCS_GenN_SE = 0

        CC_GenN_NW = 0
        CC_GenN_SW = 0
        CC_GenN_NOE = 0
        CC_GenN_SE = 0

        battery_GenN_NW = 0
        battery_GenN_SW = 0
        battery_GenN_NOE = 0
        battery_GenN_SE = 0

        hydrogen_GenN_NW = 0
        hydrogen_GenN_SW = 0
        hydrogen_GenN_NOE = 0
        hydrogen_GenN_SE = 0

        nuclear_GenN_NW = 0
        nuclear_GenN_SW = 0
        nuclear_GenN_NOE = 0
        nuclear_GenN_SE = 0

        dac_GenN_NW = 0
        dac_GenN_SW = 0
        dac_GenN_NOE = 0
        dac_GenN_SE = 0

        solar_GenN_NW = 0
        solar_GenN_SW = 0
        solar_GenN_NOE = 0
        solar_GenN_SE = 0

        wind_GenN_NW = 0
        wind_GenN_SW = 0
        wind_GenN_NOE = 0
        wind_GenN_SE = 0

    elif interConn == 'ERCOT':
        CoalCCS_GenN_p60 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p60')]
        CoalCCS_GenN_p60 = CoalCCS_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_p61 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p61')]
        CoalCCS_GenN_p61 = CoalCCS_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_p62 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p62')]
        CoalCCS_GenN_p62 = CoalCCS_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_p63 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p63')]
        CoalCCS_GenN_p63 = CoalCCS_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_p64 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p64')]
        CoalCCS_GenN_p64 = CoalCCS_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_p65 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p65')]
        CoalCCS_GenN_p65 = CoalCCS_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CoalCCS_GenN_p67 = CoalCCS_GenN.loc[CoalCCS_GenN['GAMS Symbol'].str.contains('p67')]
        CoalCCS_GenN_p67 = CoalCCS_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        CCCCS_GenN_p60 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p60')]
        CCCCS_GenN_p60 = CCCCS_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_p61 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p61')]
        CCCCS_GenN_p61 = CCCCS_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_p62 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p62')]
        CCCCS_GenN_p62 = CCCCS_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_p63 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p63')]
        CCCCS_GenN_p63 = CCCCS_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_p64 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p64')]
        CCCCS_GenN_p64 = CCCCS_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_p65 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p65')]
        CCCCS_GenN_p65 = CCCCS_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        CCCCS_GenN_p67 = CCCCS_GenN.loc[CCCCS_GenN['GAMS Symbol'].str.contains('p67')]
        CCCCS_GenN_p67 = CCCCS_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        CC_GenN_p60 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p60')]
        CC_GenN_p60 = CC_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p60
        CC_GenN_p61 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p61')]
        CC_GenN_p61 = CC_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p61
        CC_GenN_p62 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p62')]
        CC_GenN_p62 = CC_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p62
        CC_GenN_p63 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p63')]
        CC_GenN_p63 = CC_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p63
        CC_GenN_p64 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p64')]
        CC_GenN_p64 = CC_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p64
        CC_GenN_p65 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p65')]
        CC_GenN_p65 = CC_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p65
        CC_GenN_p67 = CC_GenN.loc[CC_GenN['GAMS Symbol'].str.contains('p67')]
        CC_GenN_p67 = CC_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c'])) - CCCCS_GenN_p67

        battery_GenN_p60 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p60')]
        battery_GenN_p60 = battery_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_p61 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p61')]
        battery_GenN_p61 = battery_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_p62 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p62')]
        battery_GenN_p62 = battery_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_p63 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p63')]
        battery_GenN_p63 = battery_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_p64 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p64')]
        battery_GenN_p64 = battery_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_p65 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p65')]
        battery_GenN_p65 = battery_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        battery_GenN_p67 = battery_GenN.loc[battery_GenN['GAMS Symbol'].str.contains('p67')]
        battery_GenN_p67 = battery_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        hydrogen_GenN_p60 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p60')]
        hydrogen_GenN_p60 = hydrogen_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_p61 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p61')]
        hydrogen_GenN_p61 = hydrogen_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_p62 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p62')]
        hydrogen_GenN_p62 = hydrogen_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_p63 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p63')]
        hydrogen_GenN_p63 = hydrogen_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_p64 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p64')]
        hydrogen_GenN_p64 = hydrogen_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_p65 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p65')]
        hydrogen_GenN_p65 = hydrogen_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        hydrogen_GenN_p67 = hydrogen_GenN.loc[hydrogen_GenN['GAMS Symbol'].str.contains('p67')]
        hydrogen_GenN_p67 = hydrogen_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        nuclear_GenN_p60 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p60')]
        nuclear_GenN_p60 = nuclear_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_p61 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p61')]
        nuclear_GenN_p61 = nuclear_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_p62 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p62')]
        nuclear_GenN_p62 = nuclear_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_p63 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p63')]
        nuclear_GenN_p63 = nuclear_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_p64 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p64')]
        nuclear_GenN_p64 = nuclear_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_p65 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p65')]
        nuclear_GenN_p65 = nuclear_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        nuclear_GenN_p67 = nuclear_GenN.loc[nuclear_GenN['GAMS Symbol'].str.contains('p67')]
        nuclear_GenN_p67 = nuclear_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        dac_GenN_p60 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p60')]
        dac_GenN_p60 = dac_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_p61 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p61')]
        dac_GenN_p61 = dac_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_p62 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p62')]
        dac_GenN_p62 = dac_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_p63 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p63')]
        dac_GenN_p63 = dac_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_p64 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p64')]
        dac_GenN_p64 = dac_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_p65 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p65')]
        dac_GenN_p65 = dac_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        dac_GenN_p67 = dac_GenN.loc[dac_GenN['GAMS Symbol'].str.contains('p67')]
        dac_GenN_p67 = dac_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        solar_GenN_p60 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p60')]
        solar_GenN_p60 = solar_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_p61 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p61')]
        solar_GenN_p61 = solar_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_p62 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p62')]
        solar_GenN_p62 = solar_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_p63 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p63')]
        solar_GenN_p63 = solar_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_p64 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p64')]
        solar_GenN_p64 = solar_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_p65 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p65')]
        solar_GenN_p65 = solar_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        solar_GenN_p67 = solar_GenN.loc[solar_GenN['GAMS Symbol'].str.contains('p67')]
        solar_GenN_p67 = solar_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        wind_GenN_p60 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p60')]
        wind_GenN_p60 = wind_GenN_p60.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_p61 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p61')]
        wind_GenN_p61 = wind_GenN_p61.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_p62 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p62')]
        wind_GenN_p62 = wind_GenN_p62.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_p63 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p63')]
        wind_GenN_p63 = wind_GenN_p63.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_p64 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p64')]
        wind_GenN_p64 = wind_GenN_p64.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_p65 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p65')]
        wind_GenN_p65 = wind_GenN_p65.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))
        wind_GenN_p67 = wind_GenN.loc[wind_GenN['GAMS Symbol'].str.contains('p67')]
        wind_GenN_p67 = wind_GenN_p67.drop('GAMS Symbol', axis=1).multiply(np.array(bw['block_c']))

        CoalCCS_GenN_p60 = CoalCCS_GenN_p60.sum().sum() / 1000
        CCCCS_GenN_p60 = CCCCS_GenN_p60.sum().sum() / 1000
        CC_GenN_p60 = CC_GenN_p60.sum().sum() / 1000
        battery_GenN_p60 = battery_GenN_p60.sum().sum() / 1000
        hydrogen_GenN_p60 = hydrogen_GenN_p60.sum().sum() / 1000
        nuclear_GenN_p60 = nuclear_GenN_p60.sum().sum() / 1000
        dac_GenN_p60 = dac_GenN_p60.sum().sum() / 1000
        solar_GenN_p60 = solar_GenN_p60.sum().sum() / 1000
        wind_GenN_p60 = wind_GenN_p60.sum().sum() / 1000

        CoalCCS_GenN_p61 = CoalCCS_GenN_p61.sum().sum() / 1000
        CCCCS_GenN_p61 = CCCCS_GenN_p61.sum().sum() / 1000
        CC_GenN_p61 = CC_GenN_p61.sum().sum() / 1000
        battery_GenN_p61 = battery_GenN_p61.sum().sum() / 1000
        hydrogen_GenN_p61 = hydrogen_GenN_p61.sum().sum() / 1000
        nuclear_GenN_p61 = nuclear_GenN_p61.sum().sum() / 1000
        dac_GenN_p61 = dac_GenN_p61.sum().sum() / 1000
        solar_GenN_p61 = solar_GenN_p61.sum().sum() / 1000
        wind_GenN_p61 = wind_GenN_p61.sum().sum() / 1000

        CoalCCS_GenN_p62 = CoalCCS_GenN_p62.sum().sum() / 1000
        CCCCS_GenN_p62 = CCCCS_GenN_p62.sum().sum() / 1000
        CC_GenN_p62 = CC_GenN_p62.sum().sum() / 1000
        battery_GenN_p62 = battery_GenN_p62.sum().sum() / 1000
        hydrogen_GenN_p62 = hydrogen_GenN_p62.sum().sum() / 1000
        nuclear_GenN_p62 = nuclear_GenN_p62.sum().sum() / 1000
        dac_GenN_p62 = dac_GenN_p62.sum().sum() / 1000
        solar_GenN_p62 = solar_GenN_p62.sum().sum() / 1000
        wind_GenN_p62 = wind_GenN_p62.sum().sum() / 1000

        CoalCCS_GenN_p63 = CoalCCS_GenN_p63.sum().sum() / 1000
        CCCCS_GenN_p63 = CCCCS_GenN_p63.sum().sum() / 1000
        CC_GenN_p63 = CC_GenN_p63.sum().sum() / 1000
        battery_GenN_p63 = battery_GenN_p63.sum().sum() / 1000
        hydrogen_GenN_p63 = hydrogen_GenN_p63.sum().sum() / 1000
        nuclear_GenN_p63 = nuclear_GenN_p63.sum().sum() / 1000
        dac_GenN_p63 = dac_GenN_p63.sum().sum() / 1000
        solar_GenN_p63 = solar_GenN_p63.sum().sum() / 1000
        wind_GenN_p63 = wind_GenN_p63.sum().sum() / 1000

        CoalCCS_GenN_p64 = CoalCCS_GenN_p64.sum().sum() / 1000
        CCCCS_GenN_p64 = CCCCS_GenN_p64.sum().sum() / 1000
        CC_GenN_p64 = CC_GenN_p64.sum().sum() / 1000
        battery_GenN_p64 = battery_GenN_p64.sum().sum() / 1000
        hydrogen_GenN_p64 = hydrogen_GenN_p64.sum().sum() / 1000
        nuclear_GenN_p64 = nuclear_GenN_p64.sum().sum() / 1000
        dac_GenN_p64 = dac_GenN_p64.sum().sum() / 1000
        solar_GenN_p64 = solar_GenN_p64.sum().sum() / 1000
        wind_GenN_p64 = wind_GenN_p64.sum().sum() / 1000

        CoalCCS_GenN_p65 = CoalCCS_GenN_p65.sum().sum() / 1000
        CCCCS_GenN_p65 = CCCCS_GenN_p65.sum().sum() / 1000
        CC_GenN_p65 = CC_GenN_p65.sum().sum() / 1000
        battery_GenN_p65 = battery_GenN_p65.sum().sum() / 1000
        hydrogen_GenN_p65 = hydrogen_GenN_p65.sum().sum() / 1000
        nuclear_GenN_p65 = nuclear_GenN_p65.sum().sum() / 1000
        dac_GenN_p65 = dac_GenN_p65.sum().sum() / 1000
        solar_GenN_p65 = solar_GenN_p65.sum().sum() / 1000
        wind_GenN_p65 = wind_GenN_p65.sum().sum() / 1000

        CoalCCS_GenN_p67 = CoalCCS_GenN_p67.sum().sum() / 1000
        CCCCS_GenN_p67 = CCCCS_GenN_p67.sum().sum() / 1000
        CC_GenN_p67 = CC_GenN_p67.sum().sum() / 1000
        battery_GenN_p67 = battery_GenN_p67.sum().sum() / 1000
        hydrogen_GenN_p67 = hydrogen_GenN_p67.sum().sum() / 1000
        nuclear_GenN_p67 = nuclear_GenN_p67.sum().sum() / 1000
        dac_GenN_p67 = dac_GenN_p67.sum().sum() / 1000
        solar_GenN_p67 = solar_GenN_p67.sum().sum() / 1000
        wind_GenN_p67 = wind_GenN_p67.sum().sum() / 1000


        CoalCCS_GenN_NW = CoalCCS_GenN_p60
        CoalCCS_GenN_SW = CoalCCS_GenN_p61 + CoalCCS_GenN_p62
        CoalCCS_GenN_NOE = CoalCCS_GenN_p63
        CoalCCS_GenN_SE = CoalCCS_GenN_p64 + CoalCCS_GenN_p65 + CoalCCS_GenN_p67

        CCCCS_GenN_NW = CCCCS_GenN_p60
        CCCCS_GenN_SW = CCCCS_GenN_p61 + CCCCS_GenN_p62
        CCCCS_GenN_NOE = CCCCS_GenN_p63
        CCCCS_GenN_SE = CCCCS_GenN_p64 + CCCCS_GenN_p65 + CCCCS_GenN_p67

        CC_GenN_NW = CC_GenN_p60
        CC_GenN_SW = CC_GenN_p61 + CC_GenN_p62
        CC_GenN_NOE = CC_GenN_p63
        CC_GenN_SE = CC_GenN_p64 + CC_GenN_p65 + CC_GenN_p67

        battery_GenN_NW = battery_GenN_p60
        battery_GenN_SW = battery_GenN_p61 + battery_GenN_p62
        battery_GenN_NOE = battery_GenN_p63
        battery_GenN_SE = battery_GenN_p64 + battery_GenN_p65 + battery_GenN_p67

        hydrogen_GenN_NW = hydrogen_GenN_p60
        hydrogen_GenN_SW = hydrogen_GenN_p61 + hydrogen_GenN_p62
        hydrogen_GenN_NOE = hydrogen_GenN_p63
        hydrogen_GenN_SE = hydrogen_GenN_p64 + hydrogen_GenN_p65 + hydrogen_GenN_p67

        nuclear_GenN_NW = nuclear_GenN_p60
        nuclear_GenN_SW = nuclear_GenN_p61 + nuclear_GenN_p62
        nuclear_GenN_NOE = nuclear_GenN_p63
        nuclear_GenN_SE = nuclear_GenN_p64 + nuclear_GenN_p65 + nuclear_GenN_p67

        dac_GenN_NW = dac_GenN_p60
        dac_GenN_SW = dac_GenN_p61 + dac_GenN_p62
        dac_GenN_NOE = dac_GenN_p63
        dac_GenN_SE = dac_GenN_p64 + dac_GenN_p65 + dac_GenN_p67

        solar_GenN_NW = solar_GenN_p60
        solar_GenN_SW = solar_GenN_p61 + solar_GenN_p62
        solar_GenN_NOE = solar_GenN_p63
        solar_GenN_SE = solar_GenN_p64 + solar_GenN_p65 + solar_GenN_p67

        wind_GenN_NW = wind_GenN_p60
        wind_GenN_SW = wind_GenN_p61 + wind_GenN_p62
        wind_GenN_NOE = wind_GenN_p63
        wind_GenN_SE = wind_GenN_p64 + wind_GenN_p65 + wind_GenN_p67

        CoalCCS_GenN_SERC = 0
        CCCCS_GenN_SERC = 0
        CC_GenN_SERC = 0
        battery_GenN_SERC = 0
        hydrogen_GenN_SERC = 0
        nuclear_GenN_SERC = 0
        solar_GenN_SERC = 0
        wind_GenN_SERC = 0

        CoalCCS_GenN_NY = 0
        CCCCS_GenN_NY = 0
        CC_GenN_NY = 0
        battery_GenN_NY = 0
        hydrogen_GenN_NY = 0
        nuclear_GenN_NY = 0
        dac_GenN_NY = 0
        solar_GenN_NY = 0
        wind_GenN_NY = 0

        CoalCCS_GenN_NE = 0
        CCCCS_GenN_NE = 0
        CC_GenN_NE = 0
        battery_GenN_NE = 0
        hydrogen_GenN_NE = 0
        nuclear_GenN_NE = 0
        dac_GenN_NE = 0
        solar_GenN_NE = 0
        wind_GenN_NE = 0

        CoalCCS_GenN_MISO = 0
        CCCCS_GenN_MISO = 0
        CC_GenN_MISO = 0
        battery_GenN_MISO = 0
        hydrogen_GenN_MISO = 0
        nuclear_GenN_MISO = 0
        dac_GenN_MISO = 0
        solar_GenN_MISO = 0
        wind_GenN_MISO = 0

        CoalCCS_GenN_PJM = 0
        CCCCS_GenN_PJM = 0
        CC_GenN_PJM = 0
        battery_GenN_PJM = 0
        hydrogen_GenN_PJM = 0
        nuclear_GenN_PJM = 0
        dac_GenN_PJM = 0
        solar_GenN_PJM = 0
        wind_GenN_PJM = 0

        CoalCCS_GenN_SPP = 0
        CCCCS_GenN_SPP = 0
        CC_GenN_SPP = 0
        battery_GenN_SPP = 0
        hydrogen_GenN_SPP = 0
        nuclear_GenN_SPP = 0
        dac_GenN_SPP = 0
        solar_GenN_SPP = 0
        wind_GenN_SPP = 0

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

    if interConn == 'EI':
        Coal_GenE_SERC = Coal_GenE.loc[Coal_GenE['region'] == 'SERC']
        Coal_GenE_NY = Coal_GenE.loc[Coal_GenE['region'] == 'NY']
        Coal_GenE_NE = Coal_GenE.loc[Coal_GenE['region'] == 'NE']
        Coal_GenE_MISO = Coal_GenE.loc[Coal_GenE['region'] == 'MISO']
        Coal_GenE_PJM = Coal_GenE.loc[Coal_GenE['region'] == 'PJM']
        Coal_GenE_SPP = Coal_GenE.loc[Coal_GenE['region'] == 'SPP']

        CC_GenE_SERC = CC_GenE.loc[CC_GenE['region'] == 'SERC']
        CC_GenE_NY = CC_GenE.loc[CC_GenE['region'] == 'NY']
        CC_GenE_NE = CC_GenE.loc[CC_GenE['region'] == 'NE']
        CC_GenE_MISO = CC_GenE.loc[CC_GenE['region'] == 'MISO']
        CC_GenE_PJM = CC_GenE.loc[CC_GenE['region'] == 'PJM']
        CC_GenE_SPP = CC_GenE.loc[CC_GenE['region'] == 'SPP']

        CCCCS_GenE_SERC = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'SERC']
        CCCCS_GenE_NY = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'NY']
        CCCCS_GenE_NE = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'NE']
        CCCCS_GenE_MISO = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'MISO']
        CCCCS_GenE_PJM = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'PJM']
        CCCCS_GenE_SPP = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'SPP']

        battery_GenE_SERC = battery_GenE.loc[battery_GenE['region'] == 'SERC']
        battery_GenE_NY = battery_GenE.loc[battery_GenE['region'] == 'NY']
        battery_GenE_NE = battery_GenE.loc[battery_GenE['region'] == 'NE']
        battery_GenE_MISO = battery_GenE.loc[battery_GenE['region'] == 'MISO']
        battery_GenE_PJM = battery_GenE.loc[battery_GenE['region'] == 'PJM']
        battery_GenE_SPP = battery_GenE.loc[battery_GenE['region'] == 'SPP']

        hydrogen_GenE_SERC = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'SERC']
        hydrogen_GenE_NY = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'NY']
        hydrogen_GenE_NE = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'NE']
        hydrogen_GenE_MISO = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'MISO']
        hydrogen_GenE_PJM = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'PJM']
        hydrogen_GenE_SPP = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'SPP']

        nuclear_GenE_SERC = nuclear_GenE.loc[nuclear_GenE['region'] == 'SERC']
        nuclear_GenE_NY = nuclear_GenE.loc[nuclear_GenE['region'] == 'NY']
        nuclear_GenE_NE = nuclear_GenE.loc[nuclear_GenE['region'] == 'NE']
        nuclear_GenE_MISO = nuclear_GenE.loc[nuclear_GenE['region'] == 'MISO']
        nuclear_GenE_PJM = nuclear_GenE.loc[nuclear_GenE['region'] == 'PJM']
        nuclear_GenE_SPP = nuclear_GenE.loc[nuclear_GenE['region'] == 'SPP']

        dac_GenE_SERC = dac_GenE.loc[dac_GenE['region'] == 'SERC']
        dac_GenE_NY = dac_GenE.loc[dac_GenE['region'] == 'NY']
        dac_GenE_NE = dac_GenE.loc[dac_GenE['region'] == 'NE']
        dac_GenE_MISO = dac_GenE.loc[dac_GenE['region'] == 'MISO']
        dac_GenE_PJM = dac_GenE.loc[dac_GenE['region'] == 'PJM']
        dac_GenE_SPP = dac_GenE.loc[dac_GenE['region'] == 'SPP']

        solarN_GenE_SERC = solarN_GenE.loc[solarN_GenE['region'] == 'SERC']
        solarN_GenE_NY = solarN_GenE.loc[solarN_GenE['region'] == 'NY']
        solarN_GenE_NE = solarN_GenE.loc[solarN_GenE['region'] == 'NE']
        solarN_GenE_MISO = solarN_GenE.loc[solarN_GenE['region'] == 'MISO']
        solarN_GenE_PJM = solarN_GenE.loc[solarN_GenE['region'] == 'PJM']
        solarN_GenE_SPP = solarN_GenE.loc[solarN_GenE['region'] == 'SPP']

        solarE_GenE_SERC = solarE_GenE.loc[solarE_GenE['region'] == 'SERC']
        solarE_GenE_NY = solarE_GenE.loc[solarE_GenE['region'] == 'NY']
        solarE_GenE_NE = solarE_GenE.loc[solarE_GenE['region'] == 'NE']
        solarE_GenE_MISO = solarE_GenE.loc[solarE_GenE['region'] == 'MISO']
        solarE_GenE_PJM = solarE_GenE.loc[solarE_GenE['region'] == 'PJM']
        solarE_GenE_SPP = solarE_GenE.loc[solarE_GenE['region'] == 'SPP']

        windN_GenE_SERC = windN_GenE.loc[windN_GenE['region'] == 'SERC']
        windN_GenE_NY = windN_GenE.loc[windN_GenE['region'] == 'NY']
        windN_GenE_NE = windN_GenE.loc[windN_GenE['region'] == 'NE']
        windN_GenE_MISO = windN_GenE.loc[windN_GenE['region'] == 'MISO']
        windN_GenE_PJM = windN_GenE.loc[windN_GenE['region'] == 'PJM']
        windN_GenE_SPP = windN_GenE.loc[windN_GenE['region'] == 'SPP']

        windE_GenE_SERC = windE_GenE.loc[windE_GenE['region'] == 'SERC']
        windE_GenE_NY = windE_GenE.loc[windE_GenE['region'] == 'NY']
        windE_GenE_NE = windE_GenE.loc[windE_GenE['region'] == 'NE']
        windE_GenE_MISO = windE_GenE.loc[windE_GenE['region'] == 'MISO']
        windE_GenE_PJM = windE_GenE.loc[windE_GenE['region'] == 'PJM']
        windE_GenE_SPP = windE_GenE.loc[windE_GenE['region'] == 'SPP']

        if len(CC_GenE_SERC) > 0:
            CC_GenE_SERC = CC_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_SERC = CC_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            CC_GenE_SERC = CC_GenE_SERC.sum() / 1000
        else:
            CC_GenE_SERC = 0
        if len(CC_GenE_NY) > 0:
            CC_GenE_NY = CC_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_NY = CC_GenE_NY.sum().multiply(np.array(bw['block_c']))
            CC_GenE_NY = CC_GenE_NY.sum() / 1000
        else:
            CC_GenE_NY = 0
        if len(CC_GenE_NE) > 0:
            CC_GenE_NE = CC_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_NE = CC_GenE_NE.sum().multiply(np.array(bw['block_c']))
            CC_GenE_NE = CC_GenE_NE.sum() / 1000
        else:
            CC_GenE_NE = 0
        if len(CC_GenE_MISO) > 0:
            CC_GenE_MISO = CC_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_MISO = CC_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            CC_GenE_MISO = CC_GenE_MISO.sum() / 1000
        else:
            CC_GenE_MISO = 0
        if len(CC_GenE_PJM) > 0:
            CC_GenE_PJM = CC_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_PJM = CC_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            CC_GenE_PJM = CC_GenE_PJM.sum() / 1000
        else:
            CC_GenE_PJM = 0
        if len(CC_GenE_SPP) > 0:
            CC_GenE_SPP = CC_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_SPP = CC_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            CC_GenE_SPP = CC_GenE_SPP.sum() / 1000
        else:
            CC_GenE_SPP = 0

        if len(CCCCS_GenE_SERC) > 0:
            CCCCS_GenE_SERC = CCCCS_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_SERC = CCCCS_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_SERC = CCCCS_GenE_SERC.sum() / 1000
        else:
            CCCCS_GenE_SERC = 0
        if len(CCCCS_GenE_NY) > 0:
            CCCCS_GenE_NY = CCCCS_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_NY = CCCCS_GenE_NY.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_NY = CCCCS_GenE_NY.sum() / 1000
        else:
            CCCCS_GenE_NY = 0
        if len(CCCCS_GenE_NE) > 0:
            CCCCS_GenE_NE = CCCCS_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_NE = CCCCS_GenE_NE.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_NE = CCCCS_GenE_NE.sum() / 1000
        else:
            CCCCS_GenE_NE = 0
        if len(CCCCS_GenE_MISO) > 0:
            CCCCS_GenE_MISO = CCCCS_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_MISO = CCCCS_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_MISO = CCCCS_GenE_MISO.sum() / 1000
        else:
            CCCCS_GenE_MISO = 0
        if len(CCCCS_GenE_PJM) > 0:
            CCCCS_GenE_PJM = CCCCS_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_PJM = CCCCS_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_PJM = CCCCS_GenE_PJM.sum() / 1000
        else:
            CCCCS_GenE_PJM = 0
        if len(CCCCS_GenE_SPP) > 0:
            CCCCS_GenE_SPP = CCCCS_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_SPP = CCCCS_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_SPP = CCCCS_GenE_SPP.sum() / 1000
        else:
            CCCCS_GenE_SPP = 0

        if len(battery_GenE_SERC) > 0:
            battery_GenE_SERC = battery_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_SERC = battery_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            battery_GenE_SERC = battery_GenE_SERC.sum() / 1000
        else:
            battery_GenE_SERC = 0
        if len(battery_GenE_NY) > 0:
            battery_GenE_NY = battery_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_NY = battery_GenE_NY.sum().multiply(np.array(bw['block_c']))
            battery_GenE_NY = battery_GenE_NY.sum() / 1000
        else:
            battery_GenE_NY = 0
        if len(battery_GenE_NE) > 0:
            battery_GenE_NE = battery_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_NE = battery_GenE_NE.sum().multiply(np.array(bw['block_c']))
            battery_GenE_NE = battery_GenE_NE.sum() / 1000
        else:
            battery_GenE_NE = 0
        if len(battery_GenE_MISO) > 0:
            battery_GenE_MISO = battery_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_MISO = battery_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            battery_GenE_MISO = battery_GenE_MISO.sum() / 1000
        else:
            battery_GenE_MISO = 0
        if len(battery_GenE_PJM) > 0:
            battery_GenE_PJM = battery_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_PJM = battery_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            battery_GenE_PJM = battery_GenE_PJM.sum() / 1000
        else:
            battery_GenE_PJM = 0
        if len(battery_GenE_SPP) > 0:
            battery_GenE_SPP = battery_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_SPP = battery_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            battery_GenE_SPP = battery_GenE_SPP.sum() / 1000
        else:
            battery_GenE_SPP = 0

        if len(hydrogen_GenE_SERC) > 0:
            hydrogen_GenE_SERC = hydrogen_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_SERC = hydrogen_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_SERC = hydrogen_GenE_SERC.sum() / 1000
        else:
            hydrogen_GenE_SERC = 0
        if len(hydrogen_GenE_NY) > 0:
            hydrogen_GenE_NY = hydrogen_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_NY = hydrogen_GenE_NY.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_NY = hydrogen_GenE_NY.sum() / 1000
        else:
            hydrogen_GenE_NY = 0
        if len(hydrogen_GenE_NE) > 0:
            hydrogen_GenE_NE = hydrogen_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_NE = hydrogen_GenE_NE.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_NE = hydrogen_GenE_NE.sum() / 1000
        else:
            hydrogen_GenE_NE = 0
        if len(hydrogen_GenE_MISO) > 0:
            hydrogen_GenE_MISO = hydrogen_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_MISO = hydrogen_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_MISO = hydrogen_GenE_MISO.sum() / 1000
        else:
            hydrogen_GenE_MISO = 0
        if len(hydrogen_GenE_PJM) > 0:
            hydrogen_GenE_PJM = hydrogen_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_PJM = hydrogen_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_PJM = hydrogen_GenE_PJM.sum() / 1000
        else:
            hydrogen_GenE_PJM = 0
        if len(hydrogen_GenE_SPP) > 0:
            hydrogen_GenE_SPP = hydrogen_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_SPP = hydrogen_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_SPP = hydrogen_GenE_SPP.sum() / 1000
        else:
            hydrogen_GenE_SPP = 0

        if len(nuclear_GenE_SERC) > 0:
            nuclear_GenE_SERC = nuclear_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_SERC = nuclear_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_SERC = nuclear_GenE_SERC.sum() / 1000
        else:
            nuclear_GenE_SERC = 0
        if len(nuclear_GenE_NY) > 0:
            nuclear_GenE_NY = nuclear_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_NY = nuclear_GenE_NY.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_NY = nuclear_GenE_NY.sum() / 1000
        else:
            nuclear_GenE_NY = 0
        if len(nuclear_GenE_NE) > 0:
            nuclear_GenE_NE = nuclear_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_NE = nuclear_GenE_NE.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_NE = nuclear_GenE_NE.sum() / 1000
        else:
            nuclear_GenE_NE = 0
        if len(nuclear_GenE_MISO) > 0:
            nuclear_GenE_MISO = nuclear_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_MISO = nuclear_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_MISO = nuclear_GenE_MISO.sum() / 1000
        else:
            nuclear_GenE_MISO = 0
        if len(nuclear_GenE_PJM) > 0:
            nuclear_GenE_PJM = nuclear_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_PJM = nuclear_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_PJM = nuclear_GenE_PJM.sum() / 1000
        else:
            nuclear_GenE_PJM = 0
        if len(nuclear_GenE_SPP) > 0:
            nuclear_GenE_SPP = nuclear_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_SPP = nuclear_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_SPP = nuclear_GenE_SPP.sum() / 1000
        else:
            nuclear_GenE_SPP = 0

        if len(dac_GenE_SERC) > 0:
            dac_GenE_SERC = dac_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_SERC = dac_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            dac_GenE_SERC = dac_GenE_SERC.sum() / 1000
        else:
            dac_GenE_SERC = 0
        if len(dac_GenE_NY) > 0:
            dac_GenE_NY = dac_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_NY = dac_GenE_NY.sum().multiply(np.array(bw['block_c']))
            dac_GenE_NY = dac_GenE_NY.sum() / 1000
        else:
            dac_GenE_NY = 0
        if len(dac_GenE_NE) > 0:
            dac_GenE_NE = dac_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_NE = dac_GenE_NE.sum().multiply(np.array(bw['block_c']))
            dac_GenE_NE = dac_GenE_NE.sum() / 1000
        else:
            dac_GenE_NE = 0
        if len(dac_GenE_MISO) > 0:
            dac_GenE_MISO = dac_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_MISO = dac_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            dac_GenE_MISO = dac_GenE_MISO.sum() / 1000
        else:
            dac_GenE_MISO = 0
        if len(dac_GenE_PJM) > 0:
            dac_GenE_PJM = dac_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_PJM = dac_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            dac_GenE_PJM = dac_GenE_PJM.sum() / 1000
        else:
            dac_GenE_PJM = 0
        if len(dac_GenE_SPP) > 0:
            dac_GenE_SPP = dac_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_SPP = dac_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            dac_GenE_SPP = dac_GenE_SPP.sum() / 1000
        else:
            dac_GenE_SPP = 0

        if len(solarN_GenE_SERC) > 0:
            solarN_GenE_SERC = solarN_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_SERC = solarN_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_SERC = solarN_GenE_SERC.sum() / 1000
        else:
            solarN_GenE_SERC = 0
        if len(solarN_GenE_NY) > 0:
            solarN_GenE_NY = solarN_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_NY = solarN_GenE_NY.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_NY = solarN_GenE_NY.sum() / 1000
        else:
            solarN_GenE_NY = 0
        if len(solarN_GenE_NE) > 0:
            solarN_GenE_NE = solarN_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_NE = solarN_GenE_NE.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_NE = solarN_GenE_NE.sum() / 1000
        else:
            solarN_GenE_NE = 0
        if len(solarN_GenE_MISO) > 0:
            solarN_GenE_MISO = solarN_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_MISO = solarN_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_MISO = solarN_GenE_MISO.sum() / 1000
        else:
            solarN_GenE_MISO = 0
        if len(solarN_GenE_PJM) > 0:
            solarN_GenE_PJM = solarN_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_PJM = solarN_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_PJM = solarN_GenE_PJM.sum() / 1000
        else:
            solarN_GenE_PJM = 0
        if len(solarN_GenE_SPP) > 0:
            solarN_GenE_SPP = solarN_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_SPP = solarN_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_SPP = solarN_GenE_SPP.sum() / 1000
        else:
            solarN_GenE_SPP = 0

        if len(solarE_GenE_SERC) > 0:
            solarE_GenE_SERC = solarE_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_SERC = solarE_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_SERC = solarE_GenE_SERC.sum() / 1000
        else:
            solarE_GenE_SERC = 0
        if len(solarE_GenE_NY) > 0:
            solarE_GenE_NY = solarE_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_NY = solarE_GenE_NY.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_NY = solarE_GenE_NY.sum() / 1000
        else:
            solarE_GenE_NY = 0
        if len(solarE_GenE_NE) > 0:
            solarE_GenE_NE = solarE_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_NE = solarE_GenE_NE.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_NE = solarE_GenE_NE.sum() / 1000
        else:
            solarE_GenE_NE = 0
        if len(solarE_GenE_MISO) > 0:
            solarE_GenE_MISO = solarE_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_MISO = solarE_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_MISO = solarE_GenE_MISO.sum() / 1000
        else:
            solarE_GenE_MISO = 0
        if len(solarE_GenE_PJM) > 0:
            solarE_GenE_PJM = solarE_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_PJM = solarE_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_PJM = solarE_GenE_PJM.sum() / 1000
        else:
            solarE_GenE_PJM = 0
        if len(solarE_GenE_SPP) > 0:
            solarE_GenE_SPP = solarE_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_SPP = solarE_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_SPP = solarE_GenE_SPP.sum() / 1000
        else:
            solarE_GenE_SPP = 0

        solar_GenE_SERC = solarN_GenE_SERC + solarE_GenE_SERC
        solar_GenE_NY = solarN_GenE_NY + solarE_GenE_NY
        solar_GenE_NE = solarN_GenE_NE + solarE_GenE_NE
        solar_GenE_MISO = solarN_GenE_MISO + solarE_GenE_MISO
        solar_GenE_PJM = solarN_GenE_PJM + solarE_GenE_PJM
        solar_GenE_SPP = solarN_GenE_SPP + solarE_GenE_SPP

        if len(windN_GenE_SERC) > 0:
            windN_GenE_SERC = windN_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_SERC = windN_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            windN_GenE_SERC = windN_GenE_SERC.sum() / 1000
        else:
            windN_GenE_SERC = 0
        if len(windN_GenE_NY) > 0:
            windN_GenE_NY = windN_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_NY = windN_GenE_NY.sum().multiply(np.array(bw['block_c']))
            windN_GenE_NY = windN_GenE_NY.sum() / 1000
        else:
            windN_GenE_NY = 0
        if len(windN_GenE_NE) > 0:
            windN_GenE_NE = windN_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_NE = windN_GenE_NE.sum().multiply(np.array(bw['block_c']))
            windN_GenE_NE = windN_GenE_NE.sum() / 1000
        else:
            windN_GenE_NE = 0
        if len(windN_GenE_MISO) > 0:
            windN_GenE_MISO = windN_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_MISO = windN_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            windN_GenE_MISO = windN_GenE_MISO.sum() / 1000
        else:
            windN_GenE_MISO = 0
        if len(windN_GenE_PJM) > 0:
            windN_GenE_PJM = windN_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_PJM = windN_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            windN_GenE_PJM = windN_GenE_PJM.sum() / 1000
        else:
            windN_GenE_PJM = 0
        if len(windN_GenE_SPP) > 0:
            windN_GenE_SPP = windN_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_SPP = windN_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            windN_GenE_SPP = windN_GenE_SPP.sum() / 1000
        else:
            windN_GenE_SPP = 0

        if len(windE_GenE_SERC) > 0:
            windE_GenE_SERC = windE_GenE_SERC.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_SERC = windE_GenE_SERC.sum().multiply(np.array(bw['block_c']))
            windE_GenE_SERC = windE_GenE_SERC.sum() / 1000
        else:
            windE_GenE_SERC = 0
        if len(windE_GenE_NY) > 0:
            windE_GenE_NY = windE_GenE_NY.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_NY = windE_GenE_NY.sum().multiply(np.array(bw['block_c']))
            windE_GenE_NY = windE_GenE_NY.sum() / 1000
        else:
            windE_GenE_NY = 0
        if len(windE_GenE_NE) > 0:
            windE_GenE_NE = windE_GenE_NE.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_NE = windE_GenE_NE.sum().multiply(np.array(bw['block_c']))
            windE_GenE_NE = windE_GenE_NE.sum() / 1000
        else:
            windE_GenE_NE = 0
        if len(windE_GenE_MISO) > 0:
            windE_GenE_MISO = windE_GenE_MISO.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_MISO = windE_GenE_MISO.sum().multiply(np.array(bw['block_c']))
            windE_GenE_MISO = windE_GenE_MISO.sum() / 1000
        else:
            windE_GenE_MISO = 0
        if len(windE_GenE_PJM) > 0:
            windE_GenE_PJM = windE_GenE_PJM.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_PJM = windE_GenE_PJM.sum().multiply(np.array(bw['block_c']))
            windE_GenE_PJM = windE_GenE_PJM.sum() / 1000
        else:
            windE_GenE_PJM = 0
        if len(windE_GenE_SPP) > 0:
            windE_GenE_SPP = windE_GenE_SPP.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_SPP = windE_GenE_SPP.sum().multiply(np.array(bw['block_c']))
            windE_GenE_SPP = windE_GenE_SPP.sum() / 1000
        else:
            windE_GenE_SPP = 0

        wind_GenE_SERC = windN_GenE_SERC + windE_GenE_SERC
        wind_GenE_NY = windN_GenE_NY + windE_GenE_NY
        wind_GenE_NE = windN_GenE_NE + windE_GenE_SERC
        wind_GenE_MISO = windN_GenE_MISO + windE_GenE_MISO
        wind_GenE_PJM = windN_GenE_PJM + windE_GenE_PJM
        wind_GenE_SPP = windN_GenE_SPP + windE_GenE_SPP

        CCCCS_Gen_SERC = CCCCS_GenN_SERC + CCCCS_GenE_SERC
        CC_Gen_SERC = CC_GenN_SERC + CC_GenE_SERC
        battery_Gen_SERC = battery_GenN_SERC + battery_GenE_SERC
        hydrogen_Gen_SERC = hydrogen_GenN_SERC + hydrogen_GenE_SERC
        nuclear_Gen_SERC = nuclear_GenN_SERC + nuclear_GenE_SERC
        dac_Gen_SERC = dac_GenN_SERC + dac_GenE_SERC
        solar_Gen_SERC = solar_GenN_SERC + solar_GenE_SERC
        wind_Gen_SERC = wind_GenN_SERC + wind_GenE_SERC

        CCCCS_Gen_NY = CCCCS_GenN_NY + CCCCS_GenE_NY
        CC_Gen_NY = CC_GenN_NY + CC_GenE_NY
        battery_Gen_NY = battery_GenN_NY + battery_GenE_NY
        hydrogen_Gen_NY = hydrogen_GenN_NY + hydrogen_GenE_NY
        nuclear_Gen_NY = nuclear_GenN_NY + nuclear_GenE_NY
        dac_Gen_NY = dac_GenN_NY + dac_GenE_NY
        solar_Gen_NY = solar_GenN_NY + solar_GenE_NY
        wind_Gen_NY = wind_GenN_NY + wind_GenE_NY

        CCCCS_Gen_NE = CCCCS_GenN_NE + CCCCS_GenE_NE
        CC_Gen_NE = CC_GenN_NE + CC_GenE_NE
        battery_Gen_NE = battery_GenN_NE + battery_GenE_NE
        hydrogen_Gen_NE = hydrogen_GenN_NE + hydrogen_GenE_NE
        nuclear_Gen_NE = nuclear_GenN_NE + nuclear_GenE_NE
        dac_Gen_NE = dac_GenN_NE + dac_GenE_NE
        solar_Gen_NE = solar_GenN_NE + solar_GenE_NE
        wind_Gen_NE = wind_GenN_NE + wind_GenE_NE

        CCCCS_Gen_MISO = CCCCS_GenN_MISO + CCCCS_GenE_MISO
        CC_Gen_MISO = CC_GenN_MISO + CC_GenE_MISO
        battery_Gen_MISO = battery_GenN_MISO + battery_GenE_MISO
        hydrogen_Gen_MISO = hydrogen_GenN_MISO + hydrogen_GenE_MISO
        nuclear_Gen_MISO = nuclear_GenN_MISO + nuclear_GenE_MISO
        dac_Gen_MISO = dac_GenN_MISO + dac_GenE_MISO
        solar_Gen_MISO = solar_GenN_MISO + solar_GenE_MISO
        wind_Gen_MISO = wind_GenN_MISO + wind_GenE_MISO

        CCCCS_Gen_PJM = CCCCS_GenN_PJM + CCCCS_GenE_PJM
        CC_Gen_PJM = CC_GenN_PJM + CC_GenE_PJM
        battery_Gen_PJM = battery_GenN_PJM + battery_GenE_PJM
        hydrogen_Gen_PJM = hydrogen_GenN_PJM + hydrogen_GenE_PJM
        nuclear_Gen_PJM = nuclear_GenN_PJM + nuclear_GenE_PJM
        dac_Gen_PJM = dac_GenN_PJM + dac_GenE_PJM
        solar_Gen_PJM = solar_GenN_PJM + solar_GenE_PJM
        wind_Gen_PJM = wind_GenN_PJM + wind_GenE_PJM

        CCCCS_Gen_SPP = CCCCS_GenN_SPP + CCCCS_GenE_SPP
        CC_Gen_SPP = CC_GenN_SPP + CC_GenE_SPP
        battery_Gen_SPP = battery_GenN_SPP + battery_GenE_SPP
        hydrogen_Gen_SPP = hydrogen_GenN_SPP + hydrogen_GenE_SPP
        nuclear_Gen_SPP = nuclear_GenN_SPP + nuclear_GenE_SPP
        dac_Gen_SPP = dac_GenN_SPP + dac_GenE_SPP
        solar_Gen_SPP = solar_GenN_SPP + solar_GenE_SPP
        wind_Gen_SPP = wind_GenN_SPP + wind_GenE_SPP

        CCCCS_Gen_NW = 0
        CC_Gen_NW = 0
        battery_Gen_NW = 0
        hydrogen_Gen_NW = 0
        nuclear_Gen_NW = 0
        dac_Gen_NW = 0
        solar_Gen_NW = 0
        wind_Gen_NW = 0

        CCCCS_Gen_SW = 0
        CC_Gen_SW = 0
        battery_Gen_SW = 0
        hydrogen_Gen_SW = 0
        nuclear_Gen_SW = 0
        dac_Gen_SW = 0
        solar_Gen_SW = 0
        wind_Gen_SW = 0

        CCCCS_Gen_NOE = 0
        CC_Gen_NOE = 0
        battery_Gen_NOE = 0
        hydrogen_Gen_NOE = 0
        nuclear_Gen_NOE = 0
        dac_Gen_NOE = 0
        solar_Gen_NOE = 0
        wind_Gen_NOE = 0

        CCCCS_Gen_SE = 0
        CC_Gen_SE = 0
        battery_Gen_SE = 0
        hydrogen_Gen_SE = 0
        nuclear_Gen_SE = 0
        dac_Gen_SE = 0
        solar_Gen_SE = 0
        wind_Gen_SE = 0

    elif interConn == 'ERCOT':
        CCCCS_Gen_SERC = 0
        CC_Gen_SERC = 0
        battery_Gen_SERC = 0
        hydrogen_Gen_SERC = 0
        nuclear_Gen_SERC = 0
        dac_Gen_SERC = 0
        solar_Gen_SERC = 0
        wind_Gen_SERC = 0

        CCCCS_Gen_NY = 0
        CC_Gen_NY = 0
        battery_Gen_NY = 0
        hydrogen_Gen_NY = 0
        nuclear_Gen_NY = 0
        dac_Gen_NY = 0
        solar_Gen_NY = 0
        wind_Gen_NY = 0

        CCCCS_Gen_NE = 0
        CC_Gen_NE = 0
        battery_Gen_NE = 0
        hydrogen_Gen_NE = 0
        nuclear_Gen_NE = 0
        dac_Gen_NE = 0
        solar_Gen_NE = 0
        wind_Gen_NE = 0

        CCCCS_Gen_MISO = 0
        CC_Gen_MISO = 0
        battery_Gen_MISO = 0
        hydrogen_Gen_MISO = 0
        nuclear_Gen_MISO = 0
        dac_Gen_MISO = 0
        solar_Gen_MISO = 0
        wind_Gen_MISO = 0

        CCCCS_Gen_PJM = 0
        CC_Gen_PJM = 0
        battery_Gen_PJM = 0
        hydrogen_Gen_PJM = 0
        nuclear_Gen_PJM = 0
        dac_Gen_PJM = 0
        solar_Gen_PJM = 0
        wind_Gen_PJM = 0

        CCCCS_Gen_SPP = 0
        CC_Gen_SPP = 0
        battery_Gen_SPP = 0
        hydrogen_Gen_SPP = 0
        nuclear_Gen_SPP = 0
        dac_Gen_SPP = 0
        solar_Gen_SPP = 0
        wind_Gen_SPP = 0

        Coal_GenE_p60 = Coal_GenE.loc[Coal_GenE['region'] == 'p60']
        Coal_GenE_p61 = Coal_GenE.loc[Coal_GenE['region'] == 'p61']
        Coal_GenE_p62 = Coal_GenE.loc[Coal_GenE['region'] == 'p62']
        Coal_GenE_p63 = Coal_GenE.loc[Coal_GenE['region'] == 'p63']
        Coal_GenE_p64 = Coal_GenE.loc[Coal_GenE['region'] == 'p64']
        Coal_GenE_p65 = Coal_GenE.loc[Coal_GenE['region'] == 'p65']
        Coal_GenE_p67 = Coal_GenE.loc[Coal_GenE['region'] == 'p67']

        CC_GenE_p60 = CC_GenE.loc[CC_GenE['region'] == 'p60']
        CC_GenE_p61 = CC_GenE.loc[CC_GenE['region'] == 'p61']
        CC_GenE_p62 = CC_GenE.loc[CC_GenE['region'] == 'p62']
        CC_GenE_p63 = CC_GenE.loc[CC_GenE['region'] == 'p63']
        CC_GenE_p64 = CC_GenE.loc[CC_GenE['region'] == 'p64']
        CC_GenE_p65 = CC_GenE.loc[CC_GenE['region'] == 'p65']
        CC_GenE_p67 = CC_GenE.loc[CC_GenE['region'] == 'p67']

        CCCCS_GenE_p60 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p60']
        CCCCS_GenE_p61 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p61']
        CCCCS_GenE_p62 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p62']
        CCCCS_GenE_p63 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p63']
        CCCCS_GenE_p64 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p64']
        CCCCS_GenE_p65 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p65']
        CCCCS_GenE_p67 = CCCCS_GenE.loc[CCCCS_GenE['region'] == 'p67']

        battery_GenE_p60 = battery_GenE.loc[battery_GenE['region'] == 'p60']
        battery_GenE_p61 = battery_GenE.loc[battery_GenE['region'] == 'p61']
        battery_GenE_p62 = battery_GenE.loc[battery_GenE['region'] == 'p62']
        battery_GenE_p63 = battery_GenE.loc[battery_GenE['region'] == 'p63']
        battery_GenE_p64 = battery_GenE.loc[battery_GenE['region'] == 'p64']
        battery_GenE_p65 = battery_GenE.loc[battery_GenE['region'] == 'p65']
        battery_GenE_p67 = battery_GenE.loc[battery_GenE['region'] == 'p67']

        hydrogen_GenE_p60 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p60']
        hydrogen_GenE_p61 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p61']
        hydrogen_GenE_p62 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p62']
        hydrogen_GenE_p63 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p63']
        hydrogen_GenE_p64 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p64']
        hydrogen_GenE_p65 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p65']
        hydrogen_GenE_p67 = hydrogen_GenE.loc[hydrogen_GenE['region'] == 'p67']

        nuclear_GenE_p60 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p60']
        nuclear_GenE_p61 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p61']
        nuclear_GenE_p62 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p62']
        nuclear_GenE_p63 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p63']
        nuclear_GenE_p64 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p64']
        nuclear_GenE_p65 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p65']
        nuclear_GenE_p67 = nuclear_GenE.loc[nuclear_GenE['region'] == 'p67']

        dac_GenE_p60 = dac_GenE.loc[dac_GenE['region'] == 'p60']
        dac_GenE_p61 = dac_GenE.loc[dac_GenE['region'] == 'p61']
        dac_GenE_p62 = dac_GenE.loc[dac_GenE['region'] == 'p62']
        dac_GenE_p63 = dac_GenE.loc[dac_GenE['region'] == 'p63']
        dac_GenE_p64 = dac_GenE.loc[dac_GenE['region'] == 'p64']
        dac_GenE_p65 = dac_GenE.loc[dac_GenE['region'] == 'p65']
        dac_GenE_p67 = dac_GenE.loc[dac_GenE['region'] == 'p67']

        solarN_GenE_p60 = solarN_GenE.loc[solarN_GenE['region'] == 'p60']
        solarN_GenE_p61 = solarN_GenE.loc[solarN_GenE['region'] == 'p61']
        solarN_GenE_p62 = solarN_GenE.loc[solarN_GenE['region'] == 'p62']
        solarN_GenE_p63 = solarN_GenE.loc[solarN_GenE['region'] == 'p63']
        solarN_GenE_p64 = solarN_GenE.loc[solarN_GenE['region'] == 'p64']
        solarN_GenE_p65 = solarN_GenE.loc[solarN_GenE['region'] == 'p65']
        solarN_GenE_p67 = solarN_GenE.loc[solarN_GenE['region'] == 'p67']

        solarE_GenE_p60 = solarE_GenE.loc[solarE_GenE['region'] == 'p60']
        solarE_GenE_p61 = solarE_GenE.loc[solarE_GenE['region'] == 'p61']
        solarE_GenE_p62 = solarE_GenE.loc[solarE_GenE['region'] == 'p62']
        solarE_GenE_p63 = solarE_GenE.loc[solarE_GenE['region'] == 'p63']
        solarE_GenE_p64 = solarE_GenE.loc[solarE_GenE['region'] == 'p64']
        solarE_GenE_p65 = solarE_GenE.loc[solarE_GenE['region'] == 'p65']
        solarE_GenE_p67 = solarE_GenE.loc[solarE_GenE['region'] == 'p67']

        windN_GenE_p60 = windN_GenE.loc[windN_GenE['region'] == 'p60']
        windN_GenE_p61 = windN_GenE.loc[windN_GenE['region'] == 'p61']
        windN_GenE_p62 = windN_GenE.loc[windN_GenE['region'] == 'p62']
        windN_GenE_p63 = windN_GenE.loc[windN_GenE['region'] == 'p63']
        windN_GenE_p64 = windN_GenE.loc[windN_GenE['region'] == 'p64']
        windN_GenE_p65 = windN_GenE.loc[windN_GenE['region'] == 'p65']
        windN_GenE_p67 = windN_GenE.loc[windN_GenE['region'] == 'p67']

        windE_GenE_p60 = windE_GenE.loc[windE_GenE['region'] == 'p60']
        windE_GenE_p61 = windE_GenE.loc[windE_GenE['region'] == 'p61']
        windE_GenE_p62 = windE_GenE.loc[windE_GenE['region'] == 'p62']
        windE_GenE_p63 = windE_GenE.loc[windE_GenE['region'] == 'p63']
        windE_GenE_p64 = windE_GenE.loc[windE_GenE['region'] == 'p64']
        windE_GenE_p65 = windE_GenE.loc[windE_GenE['region'] == 'p65']
        windE_GenE_p67 = windE_GenE.loc[windE_GenE['region'] == 'p67']

        if len(CC_GenE_p60) > 0:
            CC_GenE_p60 = CC_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p60 = CC_GenE_p60.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p60 = CC_GenE_p60.sum() / 1000
        else:
            CC_GenE_p60 = 0
        if len(CC_GenE_p61) > 0:
            CC_GenE_p61 = CC_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p61 = CC_GenE_p61.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p61 = CC_GenE_p61.sum() / 1000
        else:
            CC_GenE_p61 = 0
        if len(CC_GenE_p62) > 0:
            CC_GenE_p62 = CC_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p62 = CC_GenE_p62.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p62 = CC_GenE_p62.sum() / 1000
        else:
            CC_GenE_p62 = 0
        if len(CC_GenE_p63) > 0:
            CC_GenE_p63 = CC_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p63 = CC_GenE_p63.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p63 = CC_GenE_p63.sum() / 1000
        else:
            CC_GenE_p63 = 0
        if len(CC_GenE_p64) > 0:
            CC_GenE_p64 = CC_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p64 = CC_GenE_p64.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p64 = CC_GenE_p64.sum() / 1000
        else:
            CC_GenE_p64 = 0
        if len(CC_GenE_p65) > 0:
            CC_GenE_p65 = CC_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p65 = CC_GenE_p65.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p65 = CC_GenE_p65.sum() / 1000
        else:
            CC_GenE_p65 = 0
        if len(CC_GenE_p67) > 0:
            CC_GenE_p67 = CC_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            CC_GenE_p67 = CC_GenE_p67.sum().multiply(np.array(bw['block_c']))
            CC_GenE_p67 = CC_GenE_p67.sum() / 1000
        else:
            CC_GenE_p67 = 0
        CC_GenE_NW = CC_GenE_p60
        CC_GenE_SW = CC_GenE_p61 + CC_GenE_p62
        CC_GenE_NOE = CC_GenE_p63
        CC_GenE_SE = CC_GenE_p64 + CC_GenE_p65 + CC_GenE_p67

        if len(CCCCS_GenE_p60) > 0:
            CCCCS_GenE_p60 = CCCCS_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p60 = CCCCS_GenE_p60.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p60 = CCCCS_GenE_p60.sum() / 1000
        else:
            CCCCS_GenE_p60 = 0
        if len(CCCCS_GenE_p61) > 0:
            CCCCS_GenE_p61 = CCCCS_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p61 = CCCCS_GenE_p61.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p61 = CCCCS_GenE_p61.sum() / 1000
        else:
            CCCCS_GenE_p61 = 0
        if len(CCCCS_GenE_p62) > 0:
            CCCCS_GenE_p62 = CCCCS_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p62 = CCCCS_GenE_p62.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p62 = CCCCS_GenE_p62.sum() / 1000
        else:
            CCCCS_GenE_p62 = 0
        if len(CCCCS_GenE_p63) > 0:
            CCCCS_GenE_p63 = CCCCS_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p63 = CCCCS_GenE_p63.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p63 = CCCCS_GenE_p63.sum() / 1000
        else:
            CCCCS_GenE_p63 = 0
        if len(CCCCS_GenE_p64) > 0:
            CCCCS_GenE_p64 = CCCCS_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p64 = CCCCS_GenE_p64.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p64 = CCCCS_GenE_p64.sum() / 1000
        else:
            CCCCS_GenE_p64 = 0
        if len(CCCCS_GenE_p65) > 0:
            CCCCS_GenE_p65 = CCCCS_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p65 = CCCCS_GenE_p65.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p65 = CCCCS_GenE_p65.sum() / 1000
        else:
            CCCCS_GenE_p65 = 0
        if len(CCCCS_GenE_p67) > 0:
            CCCCS_GenE_p67 = CCCCS_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            CCCCS_GenE_p67 = CCCCS_GenE_p67.sum().multiply(np.array(bw['block_c']))
            CCCCS_GenE_p67 = CCCCS_GenE_p67.sum() / 1000
        else:
            CCCCS_GenE_p67 = 0
        CCCCS_GenE_NW = CCCCS_GenE_p60
        CCCCS_GenE_SW = CCCCS_GenE_p61 + CCCCS_GenE_p62
        CCCCS_GenE_NOE = CCCCS_GenE_p63
        CCCCS_GenE_SE = CCCCS_GenE_p64 + CCCCS_GenE_p65 + CCCCS_GenE_p67

        if len(battery_GenE_p60) > 0:
            battery_GenE_p60 = battery_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p60 = battery_GenE_p60.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p60 = battery_GenE_p60.sum() / 1000
        else:
            battery_GenE_p60 = 0
        if len(battery_GenE_p61) > 0:
            battery_GenE_p61 = battery_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p61 = battery_GenE_p61.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p61 = battery_GenE_p61.sum() / 1000
        else:
            battery_GenE_p61 = 0
        if len(battery_GenE_p62) > 0:
            battery_GenE_p62 = battery_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p62 = battery_GenE_p62.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p62 = battery_GenE_p62.sum() / 1000
        else:
            battery_GenE_p62 = 0
        if len(battery_GenE_p63) > 0:
            battery_GenE_p63 = battery_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p63 = battery_GenE_p63.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p63 = battery_GenE_p63.sum() / 1000
        else:
            battery_GenE_p63 = 0
        if len(battery_GenE_p64) > 0:
            battery_GenE_p64 = battery_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p64 = battery_GenE_p64.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p64 = battery_GenE_p64.sum() / 1000
        else:
            battery_GenE_p64 = 0
        if len(battery_GenE_p65) > 0:
            battery_GenE_p65 = battery_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p65 = battery_GenE_p65.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p65 = battery_GenE_p65.sum() / 1000
        else:
            battery_GenE_p65 = 0
        if len(battery_GenE_p67) > 0:
            battery_GenE_p67 = battery_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            battery_GenE_p67 = battery_GenE_p67.sum().multiply(np.array(bw['block_c']))
            battery_GenE_p67 = battery_GenE_p67.sum() / 1000
        else:
            battery_GenE_p67 = 0
        battery_GenE_NW = battery_GenE_p60
        battery_GenE_SW = battery_GenE_p61 + battery_GenE_p62
        battery_GenE_NOE = battery_GenE_p63
        battery_GenE_SE = battery_GenE_p64 + battery_GenE_p65 + battery_GenE_p67

        if len(hydrogen_GenE_p60) > 0:
            hydrogen_GenE_p60 = hydrogen_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p60 = hydrogen_GenE_p60.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p60 = hydrogen_GenE_p60.sum() / 1000
        else:
            hydrogen_GenE_p60 = 0
        if len(hydrogen_GenE_p61) > 0:
            hydrogen_GenE_p61 = hydrogen_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p61 = hydrogen_GenE_p61.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p61 = hydrogen_GenE_p61.sum() / 1000
        else:
            hydrogen_GenE_p61 = 0
        if len(hydrogen_GenE_p62) > 0:
            hydrogen_GenE_p62 = hydrogen_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p62 = hydrogen_GenE_p62.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p62 = hydrogen_GenE_p62.sum() / 1000
        else:
            hydrogen_GenE_p62 = 0
        if len(hydrogen_GenE_p63) > 0:
            hydrogen_GenE_p63 = hydrogen_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p63 = hydrogen_GenE_p63.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p63 = hydrogen_GenE_p63.sum() / 1000
        else:
            hydrogen_GenE_p63 = 0
        if len(hydrogen_GenE_p64) > 0:
            hydrogen_GenE_p64 = hydrogen_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p64 = hydrogen_GenE_p64.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p64 = hydrogen_GenE_p64.sum() / 1000
        else:
            hydrogen_GenE_p64 = 0
        if len(hydrogen_GenE_p65) > 0:
            hydrogen_GenE_p65 = hydrogen_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p65 = hydrogen_GenE_p65.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p65 = hydrogen_GenE_p65.sum() / 1000
        else:
            hydrogen_GenE_p65 = 0
        if len(hydrogen_GenE_p67) > 0:
            hydrogen_GenE_p67 = hydrogen_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            hydrogen_GenE_p67 = hydrogen_GenE_p67.sum().multiply(np.array(bw['block_c']))
            hydrogen_GenE_p67 = hydrogen_GenE_p67.sum() / 1000
        else:
            hydrogen_GenE_p67 = 0
        hydrogen_GenE_NW = hydrogen_GenE_p60
        hydrogen_GenE_SW = hydrogen_GenE_p61 + hydrogen_GenE_p62
        hydrogen_GenE_NOE = hydrogen_GenE_p63
        hydrogen_GenE_SE = hydrogen_GenE_p64 + hydrogen_GenE_p65 + hydrogen_GenE_p67

        if len(nuclear_GenE_p60) > 0:
            nuclear_GenE_p60 = nuclear_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p60 = nuclear_GenE_p60.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p60 = nuclear_GenE_p60.sum() / 1000
        else:
            nuclear_GenE_p60 = 0
        if len(nuclear_GenE_p61) > 0:
            nuclear_GenE_p61 = nuclear_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p61 = nuclear_GenE_p61.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p61 = nuclear_GenE_p61.sum() / 1000
        else:
            nuclear_GenE_p61 = 0
        if len(nuclear_GenE_p62) > 0:
            nuclear_GenE_p62 = nuclear_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p62 = nuclear_GenE_p62.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p62 = nuclear_GenE_p62.sum() / 1000
        else:
            nuclear_GenE_p62 = 0
        if len(nuclear_GenE_p63) > 0:
            nuclear_GenE_p63 = nuclear_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p63 = nuclear_GenE_p63.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p63 = nuclear_GenE_p63.sum() / 1000
        else:
            nuclear_GenE_p63 = 0
        if len(nuclear_GenE_p64) > 0:
            nuclear_GenE_p64 = nuclear_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p64 = nuclear_GenE_p64.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p64 = nuclear_GenE_p64.sum() / 1000
        else:
            nuclear_GenE_p64 = 0
        if len(nuclear_GenE_p65) > 0:
            nuclear_GenE_p65 = nuclear_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p65 = nuclear_GenE_p65.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p65 = nuclear_GenE_p65.sum() / 1000
        else:
            nuclear_GenE_p65 = 0
        if len(nuclear_GenE_p67) > 0:
            nuclear_GenE_p67 = nuclear_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            nuclear_GenE_p67 = nuclear_GenE_p67.sum().multiply(np.array(bw['block_c']))
            nuclear_GenE_p67 = nuclear_GenE_p67.sum() / 1000
        else:
            nuclear_GenE_p67 = 0
        nuclear_GenE_NW = nuclear_GenE_p60
        nuclear_GenE_SW = nuclear_GenE_p61 + nuclear_GenE_p62
        nuclear_GenE_NOE = nuclear_GenE_p63
        nuclear_GenE_SE = nuclear_GenE_p64 + nuclear_GenE_p65 + nuclear_GenE_p67

        if len(dac_GenE_p60) > 0:
            dac_GenE_p60 = dac_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p60 = dac_GenE_p60.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p60 = dac_GenE_p60.sum() / 1000
        else:
            dac_GenE_p60 = 0
        if len(dac_GenE_p61) > 0:
            dac_GenE_p61 = dac_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p61 = dac_GenE_p61.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p61 = dac_GenE_p61.sum() / 1000
        else:
            dac_GenE_p61 = 0
        if len(dac_GenE_p62) > 0:
            dac_GenE_p62 = dac_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p62 = dac_GenE_p62.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p62 = dac_GenE_p62.sum() / 1000
        else:
            dac_GenE_p62 = 0
        if len(dac_GenE_p63) > 0:
            dac_GenE_p63 = dac_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p63 = dac_GenE_p63.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p63 = dac_GenE_p63.sum() / 1000
        else:
            dac_GenE_p63 = 0
        if len(dac_GenE_p64) > 0:
            dac_GenE_p64 = dac_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p64 = dac_GenE_p64.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p64 = dac_GenE_p64.sum() / 1000
        else:
            dac_GenE_p64 = 0
        if len(dac_GenE_p65) > 0:
            dac_GenE_p65 = dac_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p65 = dac_GenE_p65.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p65 = dac_GenE_p65.sum() / 1000
        else:
            dac_GenE_p65 = 0
        if len(dac_GenE_p67) > 0:
            dac_GenE_p67 = dac_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            dac_GenE_p67 = dac_GenE_p67.sum().multiply(np.array(bw['block_c']))
            dac_GenE_p67 = dac_GenE_p67.sum() / 1000
        else:
            dac_GenE_p67 = 0
        dac_GenE_NW = dac_GenE_p60
        dac_GenE_SW = dac_GenE_p61 + dac_GenE_p62
        dac_GenE_NOE = dac_GenE_p63
        dac_GenE_SE = dac_GenE_p64 + dac_GenE_p65 + dac_GenE_p67

        if len(solarE_GenE_p60) > 0:
            solarE_GenE_p60 = solarE_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p60 = solarE_GenE_p60.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p60 = solarE_GenE_p60.sum() / 1000
        else:
            solarE_GenE_p60 = 0
        if len(solarE_GenE_p61) > 0:
            solarE_GenE_p61 = solarE_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p61 = solarE_GenE_p61.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p61 = solarE_GenE_p61.sum() / 1000
        else:
            solarE_GenE_p61 = 0
        if len(solarE_GenE_p62) > 0:
            solarE_GenE_p62 = solarE_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p62 = solarE_GenE_p62.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p62 = solarE_GenE_p62.sum() / 1000
        else:
            solarE_GenE_p62 = 0
        if len(solarE_GenE_p63) > 0:
            solarE_GenE_p63 = solarE_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p63 = solarE_GenE_p63.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p63 = solarE_GenE_p63.sum() / 1000
        else:
            solarE_GenE_p63 = 0
        if len(solarE_GenE_p64) > 0:
            solarE_GenE_p64 = solarE_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p64 = solarE_GenE_p64.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p64 = solarE_GenE_p64.sum() / 1000
        else:
            solarE_GenE_p64 = 0
        if len(solarE_GenE_p65) > 0:
            solarE_GenE_p65 = solarE_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p65 = solarE_GenE_p65.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p65 = solarE_GenE_p65.sum() / 1000
        else:
            solarE_GenE_p65 = 0
        if len(solarE_GenE_p67) > 0:
            solarE_GenE_p67 = solarE_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarE_GenE_p67 = solarE_GenE_p67.sum().multiply(np.array(bw['block_c']))
            solarE_GenE_p67 = solarE_GenE_p67.sum() / 1000
        else:
            solarE_GenE_p67 = 0
        solarE_GenE_NW = solarE_GenE_p60
        solarE_GenE_SW = solarE_GenE_p61 + solarE_GenE_p62
        solarE_GenE_NOE = solarE_GenE_p63
        solarE_GenE_SE = solarE_GenE_p64 + solarE_GenE_p65 + solarE_GenE_p67

        if len(solarN_GenE_p60) > 0:
            solarN_GenE_p60 = solarN_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p60 = solarN_GenE_p60.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p60 = solarN_GenE_p60.sum() / 1000
        else:
            solarN_GenE_p60 = 0
        if len(solarN_GenE_p61) > 0:
            solarN_GenE_p61 = solarN_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p61 = solarN_GenE_p61.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p61 = solarN_GenE_p61.sum() / 1000
        else:
            solarN_GenE_p61 = 0
        if len(solarN_GenE_p62) > 0:
            solarN_GenE_p62 = solarN_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p62 = solarN_GenE_p62.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p62 = solarN_GenE_p62.sum() / 1000
        else:
            solarN_GenE_p62 = 0
        if len(solarN_GenE_p63) > 0:
            solarN_GenE_p63 = solarN_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p63 = solarN_GenE_p63.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p63 = solarN_GenE_p63.sum() / 1000
        else:
            solarN_GenE_p63 = 0
        if len(solarN_GenE_p64) > 0:
            solarN_GenE_p64 = solarN_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p64 = solarN_GenE_p64.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p64 = solarN_GenE_p64.sum() / 1000
        else:
            solarN_GenE_p64 = 0
        if len(solarN_GenE_p65) > 0:
            solarN_GenE_p65 = solarN_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p65 = solarN_GenE_p65.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p65 = solarN_GenE_p65.sum() / 1000
        else:
            solarN_GenE_p65 = 0
        if len(solarN_GenE_p67) > 0:
            solarN_GenE_p67 = solarN_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            solarN_GenE_p67 = solarN_GenE_p67.sum().multiply(np.array(bw['block_c']))
            solarN_GenE_p67 = solarN_GenE_p67.sum() / 1000
        else:
            solarN_GenE_p67 = 0
        solarN_GenE_NW = solarN_GenE_p60
        solarN_GenE_SW = solarN_GenE_p61 + solarN_GenE_p62
        solarN_GenE_NOE = solarN_GenE_p63
        solarN_GenE_SE = solarN_GenE_p64 + solarN_GenE_p65 + solarN_GenE_p67

        if len(windE_GenE_p60) > 0:
            windE_GenE_p60 = windE_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p60 = windE_GenE_p60.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p60 = windE_GenE_p60.sum() / 1000
        else:
            windE_GenE_p60 = 0
        if len(windE_GenE_p61) > 0:
            windE_GenE_p61 = windE_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p61 = windE_GenE_p61.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p61 = windE_GenE_p61.sum() / 1000
        else:
            windE_GenE_p61 = 0
        if len(windE_GenE_p62) > 0:
            windE_GenE_p62 = windE_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p62 = windE_GenE_p62.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p62 = windE_GenE_p62.sum() / 1000
        else:
            windE_GenE_p62 = 0
        if len(windE_GenE_p63) > 0:
            windE_GenE_p63 = windE_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p63 = windE_GenE_p63.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p63 = windE_GenE_p63.sum() / 1000
        else:
            windE_GenE_p63 = 0
        if len(windE_GenE_p64) > 0:
            windE_GenE_p64 = windE_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p64 = windE_GenE_p64.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p64 = windE_GenE_p64.sum() / 1000
        else:
            windE_GenE_p64 = 0
        if len(windE_GenE_p65) > 0:
            windE_GenE_p65 = windE_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p65 = windE_GenE_p65.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p65 = windE_GenE_p65.sum() / 1000
        else:
            windE_GenE_p65 = 0
        if len(windE_GenE_p67) > 0:
            windE_GenE_p67 = windE_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            windE_GenE_p67 = windE_GenE_p67.sum().multiply(np.array(bw['block_c']))
            windE_GenE_p67 = windE_GenE_p67.sum() / 1000
        else:
            windE_GenE_p67 = 0
        windE_GenE_NW = windE_GenE_p60
        windE_GenE_SW = windE_GenE_p61 + windE_GenE_p62
        windE_GenE_NOE = windE_GenE_p63
        windE_GenE_SE = windE_GenE_p64 + windE_GenE_p65 + windE_GenE_p67

        if len(windN_GenE_p60) > 0:
            windN_GenE_p60 = windN_GenE_p60.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p60 = windN_GenE_p60.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p60 = windN_GenE_p60.sum() / 1000
        else:
            windN_GenE_p60 = 0
        if len(windN_GenE_p61) > 0:
            windN_GenE_p61 = windN_GenE_p61.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p61 = windN_GenE_p61.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p61 = windN_GenE_p61.sum() / 1000
        else:
            windN_GenE_p61 = 0
        if len(windN_GenE_p62) > 0:
            windN_GenE_p62 = windN_GenE_p62.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p62 = windN_GenE_p62.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p62 = windN_GenE_p62.sum() / 1000
        else:
            windN_GenE_p62 = 0
        if len(windN_GenE_p63) > 0:
            windN_GenE_p63 = windN_GenE_p63.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p63 = windN_GenE_p63.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p63 = windN_GenE_p63.sum() / 1000
        else:
            windN_GenE_p63 = 0
        if len(windN_GenE_p64) > 0:
            windN_GenE_p64 = windN_GenE_p64.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p64 = windN_GenE_p64.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p64 = windN_GenE_p64.sum() / 1000
        else:
            windN_GenE_p64 = 0
        if len(windN_GenE_p65) > 0:
            windN_GenE_p65 = windN_GenE_p65.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p65 = windN_GenE_p65.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p65 = windN_GenE_p65.sum() / 1000
        else:
            windN_GenE_p65 = 0
        if len(windN_GenE_p67) > 0:
            windN_GenE_p67 = windN_GenE_p67.drop(['Unit', 'PlantType', 'region'], axis=1)
            windN_GenE_p67 = windN_GenE_p67.sum().multiply(np.array(bw['block_c']))
            windN_GenE_p67 = windN_GenE_p67.sum() / 1000
        else:
            windN_GenE_p67 = 0
        windN_GenE_NW = windN_GenE_p60
        windN_GenE_SW = windN_GenE_p61 + windN_GenE_p62
        windN_GenE_NOE = windN_GenE_p63
        windN_GenE_SE = windN_GenE_p64 + windN_GenE_p65 + windN_GenE_p67

        CCCCS_Gen_NW = CCCCS_GenN_NW  + CCCCS_GenE_NW
        CC_Gen_NW = CC_GenN_NW + CC_GenE_NW
        battery_Gen_NW = battery_GenN_NW + battery_GenE_NW
        hydrogen_Gen_NW = hydrogen_GenN_NW + hydrogen_GenE_NW
        nuclear_Gen_NW = nuclear_GenN_NW + nuclear_GenE_NW
        dac_Gen_NW = dac_GenN_NW + dac_GenE_NW
        solar_Gen_NW = solar_GenN_NW + solarE_GenE_NW + solarN_GenE_NW
        wind_Gen_NW = wind_GenN_NW + windE_GenE_NW + windN_GenE_NW

        CCCCS_Gen_SW = CCCCS_GenN_SW + CCCCS_GenE_SW
        CC_Gen_SW = CC_GenN_SW + CC_GenE_SW
        battery_Gen_SW = battery_GenN_SW + battery_GenE_SW
        hydrogen_Gen_SW = hydrogen_GenN_SW + hydrogen_GenE_SW
        nuclear_Gen_SW = nuclear_GenN_SW + nuclear_GenE_SW
        dac_Gen_SW = dac_GenN_SW + dac_GenE_SW
        solar_Gen_SW = solar_GenN_SW + solarE_GenE_SW + solarN_GenE_SW
        wind_Gen_SW = wind_GenN_SW + windE_GenE_SW + windN_GenE_SW

        CCCCS_Gen_NOE = CCCCS_GenN_NOE + CCCCS_GenE_NOE
        CC_Gen_NOE = CC_GenN_NOE + CC_GenE_NOE
        battery_Gen_NOE = battery_GenN_NOE + battery_GenE_NOE
        hydrogen_Gen_NOE = hydrogen_GenN_NOE + hydrogen_GenE_NOE
        nuclear_Gen_NOE = nuclear_GenN_NOE + nuclear_GenE_NOE
        dac_Gen_NOE = dac_GenN_NOE + dac_GenE_NOE
        solar_Gen_NOE = solar_GenN_NOE + solarE_GenE_NOE + solarN_GenE_NOE
        wind_Gen_NOE = wind_GenN_NOE + windE_GenE_NOE + windN_GenE_NOE

        CCCCS_Gen_SE = CCCCS_GenN_SE + CCCCS_GenE_SE
        CC_Gen_SE = CC_GenN_SE + CC_GenE_SE
        battery_Gen_SE = battery_GenN_SE + battery_GenE_SE
        hydrogen_Gen_SE = hydrogen_GenN_SE + hydrogen_GenE_SE
        nuclear_Gen_SE = nuclear_GenN_SE + nuclear_GenE_SE
        dac_Gen_SE = dac_GenN_SE + dac_GenE_SE
        solar_Gen_SE = solar_GenN_SE + solarE_GenE_SE + solarN_GenE_SE
        wind_Gen_SE = wind_GenN_SE + windE_GenE_SE + windN_GenE_SE

    return (CCCCS_Gen_SERC,CC_Gen_SERC,battery_Gen_SERC,hydrogen_Gen_SERC,nuclear_Gen_SERC,dac_Gen_SERC,
            solar_Gen_SERC,wind_Gen_SERC,CCCCS_Gen_NY,CC_Gen_NY,battery_Gen_NY,hydrogen_Gen_NY,nuclear_Gen_NY,
            dac_Gen_NY,solar_Gen_NY, wind_Gen_NY,CCCCS_Gen_NE,CC_Gen_NE,battery_Gen_NE,hydrogen_Gen_NE,
            nuclear_Gen_NE,dac_Gen_NE,solar_Gen_NE,wind_Gen_NE,CCCCS_Gen_MISO,CC_Gen_MISO,battery_Gen_MISO,
            hydrogen_Gen_MISO,nuclear_Gen_MISO ,dac_Gen_MISO,solar_Gen_MISO,wind_Gen_MISO,CCCCS_Gen_PJM,
            CC_Gen_PJM,battery_Gen_PJM,hydrogen_Gen_PJM,nuclear_Gen_PJM,dac_Gen_PJM,solar_Gen_PJM,wind_Gen_PJM,
            CCCCS_Gen_SPP,CC_Gen_SPP,battery_Gen_SPP,hydrogen_Gen_SPP,nuclear_Gen_SPP,dac_Gen_SPP,solar_Gen_SPP,wind_Gen_SPP,
            CCCCS_Gen_NW,CC_Gen_NW,battery_Gen_NW,hydrogen_Gen_NW,nuclear_Gen_NW,dac_Gen_NW,solar_Gen_NW,wind_Gen_NW,
            CCCCS_Gen_SW,CC_Gen_SW,battery_Gen_SW,hydrogen_Gen_SW,nuclear_Gen_SW,dac_Gen_SW,solar_Gen_SW,wind_Gen_SW,
            CCCCS_Gen_NOE,CC_Gen_NOE,battery_Gen_NOE,hydrogen_Gen_NOE,nuclear_Gen_NOE,dac_Gen_NOE,solar_Gen_NOE,
            wind_Gen_NOE,CCCCS_Gen_SE,CC_Gen_SE,battery_Gen_SE,hydrogen_Gen_SE,nuclear_Gen_SE,dac_Gen_SE,
            solar_Gen_SE,wind_Gen_SE)