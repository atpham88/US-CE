
import pandas as pd

def transInvestments_temp(results_dir_temp, techCase, planningScr, interConn):
    if interConn == 'EI':
        finalCap = '-724'
    elif interConn == 'ERCOT':
        finalCap = '-90'

    if planningScr == 'NE2020':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2020NEin2020_' + 'reference' + '_TrueREFERENCE\\2050CO2Cap'+finalCap+'\\CE\\'
    elif planningScr == 'NE2050':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2020NEin2050_' + 'reference' + '_TrueREFERENCE\\2060CO2Cap'+finalCap+'\\CE\\'
        results_dir2 = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2050_' + 'reference' + '_TrueREFERENCE\\2050CO2Cap' + finalCap + '\\CE\\'
    elif planningScr == 'NE2051':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2051NEin2050_' + 'reference' + '_TrueREFERENCE\\2060CO2Cap'+finalCap+'\\CE\\'
        results_dir2 = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2051NEin2050_' + 'reference' + '_TrueREFERENCE\\2050CO2Cap' + finalCap + '\\CE\\'

    if planningScr == 'NE2020':
        trans_data = pd.read_csv(results_dir +'vNl2050.csv')
        trans_data2 = 0
    elif planningScr == 'NE2050' or planningScr == 'NE2051':
        trans_data = pd.read_csv(results_dir + 'vNl2060.csv')
        trans_data2 = pd.read_csv(results_dir2 + 'vNl2050.csv')

    if interConn == 'EI':
        miso_serc = trans_data.iloc[0, 1] + trans_data.iloc[6, 1]
        pjm_serc = trans_data.iloc[1, 1] + trans_data.iloc[7, 1]
        ne_ny = trans_data.iloc[2, 1] + trans_data.iloc[8, 1]
        pjm_ny = trans_data.iloc[3, 1] + trans_data.iloc[9, 1]
        pjm_miso = trans_data.iloc[4, 1] + trans_data.iloc[10, 1]
        spp_miso = trans_data.iloc[5, 1] + trans_data.iloc[11, 1]

        p60_p61 = 0
        p60_p62 = 0
        p60_p63 = 0
        p61_p62 = 0
        p61_p63 = 0
        p61_p64 = 0
        p61_p65 = 0
        p63_p64 = 0
        p63_p67 = 0
        p64_p65 = 0
        p64_p67 = 0
        p65_p67 = 0
    elif interConn == 'ERCOT':
        miso_serc = 0
        pjm_serc = 0
        ne_ny = 0
        pjm_ny = 0
        pjm_miso = 0
        spp_miso = 0

        p60_p61 = trans_data.iloc[0, 1] + trans_data.iloc[12, 1]
        p60_p62 = trans_data.iloc[1, 1] + trans_data.iloc[13, 1]
        p60_p63 = trans_data.iloc[2, 1] + trans_data.iloc[14, 1]
        p61_p62 = trans_data.iloc[3, 1] + trans_data.iloc[15, 1]
        p61_p63 = trans_data.iloc[4, 1] + trans_data.iloc[16, 1]
        p61_p64 = trans_data.iloc[5, 1] + trans_data.iloc[17, 1]
        p61_p65 = trans_data.iloc[6, 1] + trans_data.iloc[18, 1]
        p63_p64 = trans_data.iloc[7, 1] + trans_data.iloc[19, 1]
        p63_p67 = trans_data.iloc[8, 1] + trans_data.iloc[20, 1]
        p64_p65 = trans_data.iloc[9, 1] + trans_data.iloc[21, 1]
        p64_p67 = trans_data.iloc[10, 1] + trans_data.iloc[22, 1]
        p65_p67 = trans_data.iloc[11, 1] + trans_data.iloc[23, 1]

    ercot_tot = p60_p61 + p60_p62 + p60_p63 + p61_p62 + p61_p63 + p61_p64 + p61_p65 + p63_p64 + p63_p67 + p64_p65 + p64_p67 + p65_p67

    return (miso_serc, pjm_serc, ne_ny, pjm_ny, pjm_miso, spp_miso, ercot_tot)