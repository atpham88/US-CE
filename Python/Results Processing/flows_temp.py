
import pandas as pd

def transFlows_temp(results_dir_temp, techCase, planningScr, interConn):
    if interConn == 'EI':
        finalCap = '-724'
    elif interConn == 'ERCOT':
        finalCap = '-90'

    if planningScr == 'NE2020':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2020NEin2020_' + 'reference' + '_TrueREFERENCE\\2050CO2Cap'+finalCap+'\\CE\\'
    elif planningScr == 'NE2050':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2020NEin2050_' + 'reference' + '_TrueREFERENCE\\2060CO2Cap'+finalCap+'\\CE\\'
    elif planningScr == 'NE2051':
        results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative'+finalCap+'_DACS2051NEin2050_' + 'reference' + '_TrueREFERENCE\\2060CO2Cap'+finalCap+'\\CE\\'

    if planningScr == 'NE2020':
        trans_data = pd.read_csv(results_dir +'vLineflowCE2050.csv')
        bw = pd.read_csv(results_dir + 'hoursCEByBlock2050.csv')
    elif planningScr == 'NE2050' or planningScr == 'NE2051':
        trans_data = pd.read_csv(results_dir + 'vLineflowCE2060.csv')
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

    if interConn == 'EI':
        serc_to_miso = -trans_data.SERCMISO*bw['block_c']
        serc_to_pjm = -trans_data.SERCPJM*bw['block_c']
        ny_to_ne = -trans_data.NYNE*bw['block_c']
        ny_to_pjm = -trans_data.NYPJM*bw['block_c']
        miso_to_pjm = -trans_data.MISOPJM*bw['block_c']
        miso_to_spp = -trans_data.MISOSPP*bw['block_c']
        miso_to_serc = -trans_data.MISOSERC*bw['block_c']
        pjm_to_serc = -trans_data.PJMSERC*bw['block_c']
        ne_to_ny = -trans_data.NENY*bw['block_c']
        pjm_to_ny = -trans_data.PJMNY*bw['block_c']
        pjm_to_miso = -trans_data.PJMMISO*bw['block_c']
        spp_to_miso = -trans_data.SPPMISO*bw['block_c']

        serc_to_miso = serc_to_miso.sum()
        serc_to_pjm = serc_to_pjm.sum()
        ny_to_ne = ny_to_ne.sum()
        ny_to_pjm = ny_to_pjm.sum()
        miso_to_pjm = miso_to_pjm.sum()
        miso_to_spp = miso_to_spp.sum()
        miso_to_serc = miso_to_serc.sum()
        pjm_to_serc = pjm_to_serc.sum()
        ne_to_ny = ne_to_ny.sum()
        pjm_to_ny = pjm_to_ny.sum()
        pjm_to_miso = pjm_to_miso.sum()
        spp_to_miso = spp_to_miso.sum()

        netFlow_serc = (- serc_to_miso - serc_to_pjm + miso_to_serc + pjm_to_serc)/1000
        netFlow_ny = (- ny_to_ne - ny_to_pjm + ne_to_ny + pjm_to_ny)/1000
        netFlow_miso = (- miso_to_pjm - miso_to_spp - miso_to_serc + serc_to_miso + pjm_to_miso + spp_to_miso)/1000
        netFlow_pjm = (- pjm_to_serc - pjm_to_ny - pjm_to_miso + serc_to_pjm + ny_to_pjm + miso_to_pjm)/1000
        netFlow_ne = (- ne_to_ny + ny_to_ne)/1000
        netFlow_spp = (- spp_to_miso + miso_to_spp)/1000

        netFlow_NW_ERCOT = 0
        netFlow_SW_ERCOT = 0
        netFlow_NE_ERCOT = 0
        netFlow_SE_ERCOT = 0

    elif interConn == 'ERCOT':
        netFlow_serc = 0
        netFlow_ny = 0
        netFlow_miso = 0
        netFlow_pjm = 0
        netFlow_ne = 0
        netFlow_spp = 0

        p60p61 = -trans_data.p60p61*bw['block_c']
        p60p62 = -trans_data.p60p62*bw['block_c']
        p60p63 = -trans_data.p60p63*bw['block_c']
        p61p62 = -trans_data.p61p62*bw['block_c']
        p61p63 = -trans_data.p61p63*bw['block_c']
        p61p64 = -trans_data.p61p64*bw['block_c']
        p61p65 = -trans_data.p61p65*bw['block_c']
        p63p64 = -trans_data.p63p64*bw['block_c']
        p63p67 = -trans_data.p63p67*bw['block_c']
        p64p65 = -trans_data.p64p65*bw['block_c']
        p64p67 = -trans_data.p64p67*bw['block_c']
        p65p67 = -trans_data.p65p67*bw['block_c']
        p61p60 = -trans_data.p61p60*bw['block_c']
        p62p60 = -trans_data.p62p60*bw['block_c']
        p63p60 = -trans_data.p63p60*bw['block_c']
        p62p61 = -trans_data.p62p61*bw['block_c']
        p63p61 = -trans_data.p63p61*bw['block_c']
        p64p61 = -trans_data.p64p61*bw['block_c']
        p65p61 = -trans_data.p65p61*bw['block_c']
        p64p63 = -trans_data.p64p63*bw['block_c']
        p67p63 = -trans_data.p67p63*bw['block_c']
        p65p64 = -trans_data.p65p64*bw['block_c']
        p67p64 = -trans_data.p67p64*bw['block_c']
        p67p65 = -trans_data.p67p65*bw['block_c']

        p60p61 = p60p61.sum()
        p60p62 = p60p62.sum()
        p60p63 = p60p63.sum()
        p61p62 = p61p62.sum()
        p61p63 = p61p63.sum()
        p61p64 = p61p64.sum()
        p61p65 = p61p65.sum()
        p63p64 = p63p64.sum()
        p63p67 = p63p67.sum()
        p64p65 = p64p65.sum()
        p64p67 = p64p67.sum()
        p65p67 = p65p67.sum()
        p61p60 = p61p60.sum()
        p62p60 = p62p60.sum()
        p63p60 = p63p60.sum()
        p62p61 = p62p61.sum()
        p63p61 = p63p61.sum()
        p64p61 = p64p61.sum()
        p65p61 = p65p61.sum()
        p64p63 = p64p63.sum()
        p67p63 = p67p63.sum()
        p65p64 = p65p64.sum()
        p67p64 = p67p64.sum()
        p67p65 = p67p65.sum()

        netFlow_p60 = - p60p61 - p60p62 - p60p63 + p61p60  + p62p60 + p63p60
        netFlow_p61 = - p61p62 - p61p63 - p61p64 - p61p65 - p61p60 + p62p61 + p63p61 + p64p61 + p65p61
        netFlow_p62 = - p62p61 - p62p60 + p60p62 + p61p62
        netFlow_p63 = - p63p64 - p63p67 - p63p60 - p63p61 + p60p63 + p61p63 + p64p63 + p67p63
        netFlow_p64 = - p64p65 - p64p67 - p64p61 - p64p63 + p61p64 + p63p64 + p65p64 + p67p64
        netFlow_p65 = - p65p67 - p65p61 - p65p64 + p61p65 + p64p65 + p67p65
        netFlow_p67 = - p67p63 - p67p65 - p67p64 + p63p67 + p64p67 + p65p67

        netFlow_NW_ERCOT = netFlow_p60/1000
        netFlow_SW_ERCOT = (netFlow_p61 + netFlow_p62)/1000
        netFlow_NE_ERCOT = netFlow_p63/1000
        netFlow_SE_ERCOT = (netFlow_p64 + netFlow_p65 + netFlow_p67)/1000


    return (netFlow_serc, netFlow_ny, netFlow_miso, netFlow_pjm, netFlow_ne, netFlow_spp,
            netFlow_NW_ERCOT, netFlow_SW_ERCOT, netFlow_NE_ERCOT, netFlow_SE_ERCOT)