
import pandas as pd

def capRegions(results_dir_temp, techCase, planningScr, interConn):
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
        cap_data = pd.read_csv(results_dir +'genFleetAfterCE2050.csv')
    elif planningScr == 'NE2050' or planningScr == 'NE2051':
        cap_data = pd.read_csv(results_dir + 'genFleetAfterCE2060.csv')

    if interConn == 'EI':
        cap_exp = cap_data[cap_data.YearAddedCE > 2020]
        cap_exp = cap_exp[['PlantType', 'Capacity (MW)', 'region']]
        cap_exp_2 = cap_exp[cap_data.YearAddedCE > 2050]
        cap_exp_2 = cap_exp_2[['PlantType', 'Capacity (MW)', 'region']]
    elif interConn == 'ERCOT':
        cap_exp = cap_data[cap_data.YearAddedCE > 2020]
        cap_exp = cap_exp[['PlantType', 'Capacity (MW)', 'region']]
        cap_exp.loc[(cap_exp['region'] == 'p60'), 'region2'] = 'ERCOT NW'
        cap_exp.loc[(cap_exp['region'] == 'p61'), 'region2'] = 'ERCOT SW'
        cap_exp.loc[(cap_exp['region'] == 'p62'), 'region2'] = 'ERCOT SW'
        cap_exp.loc[(cap_exp['region'] == 'p63'), 'region2'] = 'ERCOT NE'
        cap_exp.loc[(cap_exp['region'] == 'p64'), 'region2'] = 'ERCOT SE'
        cap_exp.loc[(cap_exp['region'] == 'p65'), 'region2'] = 'ERCOT SE'
        cap_exp.loc[(cap_exp['region'] == 'p67'), 'region2'] = 'ERCOT SE'

        if planningScr == 'NE2050' or planningScr == 'NE2051':
            cap_exp_2 = cap_data[cap_data.YearAddedCE > 2050]
            cap_exp_2 = cap_exp_2[['PlantType', 'Capacity (MW)', 'region']]
            cap_exp_2.loc[(cap_exp_2['region'] == 'p60'), 'region2'] = 'ERCOT NW'
            cap_exp_2.loc[(cap_exp_2['region'] == 'p61'), 'region2'] = 'ERCOT SW'
            cap_exp_2.loc[(cap_exp_2['region'] == 'p62'), 'region2'] = 'ERCOT SW'
            cap_exp_2.loc[(cap_exp_2['region'] == 'p63'), 'region2'] = 'ERCOT NE'
            cap_exp_2.loc[(cap_exp_2['region'] == 'p64'), 'region2'] = 'ERCOT SE'
            cap_exp_2.loc[(cap_exp_2['region'] == 'p65'), 'region2'] = 'ERCOT SE'
            cap_exp_2.loc[(cap_exp_2['region'] == 'p67'), 'region2'] = 'ERCOT SE'

    CoalCCS = cap_exp[cap_exp['PlantType'].str.contains('Coal Steam CCS')]
    CC = cap_exp.loc[cap_exp['PlantType'].str.contains('Combined Cycle')]
    CCCCS = cap_exp.loc[cap_exp['PlantType'].str.contains('Combined Cycle CCS')]
    Nuclear = cap_exp.loc[cap_exp['PlantType'].str.contains('Nuclear')]
    Hydrogen = cap_exp.loc[cap_exp['PlantType'].str.contains('Hydrogen')]
    Battery = cap_exp.loc[cap_exp['PlantType'].str.contains('Battery Storage')]
    DAC = cap_exp.loc[cap_exp['PlantType'].str.contains('DAC')]
    Wind1 = cap_exp[cap_exp['PlantType'].str.contains('wind')]
    Solar1 = cap_exp[cap_exp['PlantType'].str.contains('solar')]
    Wind2 = cap_exp[cap_exp['PlantType'].str.contains('Wind')]
    Solar2 = cap_exp[cap_exp['PlantType'].str.contains('Solar')]

    if planningScr == 'NE2050' or planningScr == 'NE2051':
        CoalCCS_2 = cap_exp_2[cap_exp_2['PlantType'].str.contains('Coal Steam CCS')]
        CC_2 = cap_exp_2.loc[cap_exp_2['PlantType'].str.contains('Combined Cycle')]
        CCCCS_2 = cap_exp_2.loc[cap_exp_2['PlantType'].str.contains('Combined Cycle CCS')]
        Nuclear_2 = cap_exp_2.loc[cap_exp_2['PlantType'].str.contains('Nuclear')]
        Hydrogen_2 = cap_exp_2.loc[cap_exp_2['PlantType'].str.contains('Hydrogen')]
        Battery_2 = cap_exp_2.loc[cap_exp_2['PlantType'].str.contains('Battery Storage')]
        DAC_2 = cap_exp_2.loc[cap_exp_2['PlantType'].str.contains('DAC')]
        Wind1_2 = cap_exp_2[cap_exp_2['PlantType'].str.contains('wind')]
        Solar1_2 = cap_exp_2[cap_exp_2['PlantType'].str.contains('solar')]
        Wind2_2 = cap_exp_2[cap_exp_2['PlantType'].str.contains('Wind')]
        Solar2_2 = cap_exp_2[cap_exp_2['PlantType'].str.contains('Solar')]

    if interConn == 'EI':
        CoalCCS_SERC = CoalCCS[CoalCCS['region'].str.contains('SERC')]
        CoalCCS_NE = CoalCCS[CoalCCS['region'].str.contains('NE')]
        CoalCCS_NY = CoalCCS[CoalCCS['region'].str.contains('NY')]
        CoalCCS_MISO = CoalCCS[CoalCCS['region'].str.contains('MISO')]
        CoalCCS_PJM = CoalCCS[CoalCCS['region'].str.contains('PJM')]
        CoalCCS_SPP = CoalCCS[CoalCCS['region'].str.contains('SPP')]

        CC_SERC = CC[CC['region'].str.contains('SERC')]
        CC_NE = CC[CC['region'].str.contains('NE')]
        CC_NY = CC[CC['region'].str.contains('NY')]
        CC_MISO = CC[CC['region'].str.contains('MISO')]
        CC_PJM = CC[CC['region'].str.contains('PJM')]
        CC_SPP = CC[CC['region'].str.contains('SPP')]

        CCCCS_SERC = CCCCS[CCCCS['region'].str.contains('SERC')]
        CCCCS_NE = CCCCS[CCCCS['region'].str.contains('NE')]
        CCCCS_NY = CCCCS[CCCCS['region'].str.contains('NY')]
        CCCCS_MISO = CCCCS[CCCCS['region'].str.contains('MISO')]
        CCCCS_PJM = CCCCS[CCCCS['region'].str.contains('PJM')]
        CCCCS_SPP = CCCCS[CCCCS['region'].str.contains('SPP')]

        Nuclear_SERC = Nuclear[Nuclear['region'].str.contains('SERC')]
        Nuclear_NE = Nuclear[Nuclear['region'].str.contains('NE')]
        Nuclear_NY = Nuclear[Nuclear['region'].str.contains('NY')]
        Nuclear_MISO = Nuclear[Nuclear['region'].str.contains('MISO')]
        Nuclear_PJM = Nuclear[Nuclear['region'].str.contains('PJM')]
        Nuclear_SPP = Nuclear[Nuclear['region'].str.contains('SPP')]

        Hydrogen_SERC = Hydrogen[Hydrogen['region'].str.contains('SERC')]
        Hydrogen_NE = Hydrogen[Hydrogen['region'].str.contains('NE')]
        Hydrogen_NY = Hydrogen[Hydrogen['region'].str.contains('NY')]
        Hydrogen_MISO = Hydrogen[Hydrogen['region'].str.contains('MISO')]
        Hydrogen_PJM = Hydrogen[Hydrogen['region'].str.contains('PJM')]
        Hydrogen_SPP = Hydrogen[Hydrogen['region'].str.contains('SPP')]

        Battery_SERC = Battery[Battery['region'].str.contains('SERC')]
        Battery_NE = Battery[Battery['region'].str.contains('NE')]
        Battery_NY = Battery[Battery['region'].str.contains('NY')]
        Battery_MISO = Battery[Battery['region'].str.contains('MISO')]
        Battery_PJM = Battery[Battery['region'].str.contains('PJM')]
        Battery_SPP = Battery[Battery['region'].str.contains('SPP')]

        DAC_SERC = DAC[DAC['region'].str.contains('SERC')]
        DAC_NE = DAC[DAC['region'].str.contains('NE')]
        DAC_NY = DAC[DAC['region'].str.contains('NY')]
        DAC_MISO = DAC[DAC['region'].str.contains('MISO')]
        DAC_PJM = DAC[DAC['region'].str.contains('PJM')]
        DAC_SPP = DAC[DAC['region'].str.contains('SPP')]

        Wind1_SERC = Wind1[Wind1['region'].str.contains('SERC')]
        Wind1_NE = Wind1[Wind1['region'].str.contains('NE')]
        Wind1_NY = Wind1[Wind1['region'].str.contains('NY')]
        Wind1_MISO = Wind1[Wind1['region'].str.contains('MISO')]
        Wind1_PJM = Wind1[Wind1['region'].str.contains('PJM')]
        Wind1_SPP = Wind1[Wind1['region'].str.contains('SPP')]

        Wind2_SERC = Wind2[Wind2['region'].str.contains('SERC')]
        Wind2_NE = Wind2[Wind2['region'].str.contains('NE')]
        Wind2_NY = Wind2[Wind2['region'].str.contains('NY')]
        Wind2_MISO = Wind2[Wind2['region'].str.contains('MISO')]
        Wind2_PJM = Wind2[Wind2['region'].str.contains('PJM')]
        Wind2_SPP = Wind2[Wind2['region'].str.contains('SPP')]

        Solar1_SERC = Solar1[Solar1['region'].str.contains('SERC')]
        Solar1_NE = Solar1[Solar1['region'].str.contains('NE')]
        Solar1_NY = Solar1[Solar1['region'].str.contains('NY')]
        Solar1_MISO = Solar1[Solar1['region'].str.contains('MISO')]
        Solar1_PJM = Solar1[Solar1['region'].str.contains('PJM')]
        Solar1_SPP = Solar1[Solar1['region'].str.contains('SPP')]

        Solar2_SERC = Solar2[Solar2['region'].str.contains('SERC')]
        Solar2_NE = Solar2[Solar2['region'].str.contains('NE')]
        Solar2_NY = Solar2[Solar2['region'].str.contains('NY')]
        Solar2_MISO = Solar2[Solar2['region'].str.contains('MISO')]
        Solar2_PJM = Solar2[Solar2['region'].str.contains('PJM')]
        Solar2_SPP = Solar2[Solar2['region'].str.contains('SPP')]

        CoalCCS_SERC = CoalCCS_SERC['Capacity (MW)'].sum()/1000
        CoalCCS_NE = CoalCCS_NE['Capacity (MW)'].sum()/1000
        CoalCCS_NY = CoalCCS_NY['Capacity (MW)'].sum()/1000
        CoalCCS_MISO = CoalCCS_MISO['Capacity (MW)'].sum()/1000
        CoalCCS_PJM = CoalCCS_PJM['Capacity (MW)'].sum()/1000
        CoalCCS_SPP = CoalCCS_SPP['Capacity (MW)'].sum()/1000

        CCCCS_SERC = CCCCS_SERC['Capacity (MW)'].sum() / 1000
        CCCCS_NE = CCCCS_NE['Capacity (MW)'].sum() / 1000
        CCCCS_NY = CCCCS_NY['Capacity (MW)'].sum() / 1000
        CCCCS_MISO = CCCCS_MISO['Capacity (MW)'].sum() / 1000
        CCCCS_PJM = CCCCS_PJM['Capacity (MW)'].sum() / 1000
        CCCCS_SPP = CCCCS_SPP['Capacity (MW)'].sum() / 1000

        CC_SERC = CC_SERC['Capacity (MW)'].sum() / 1000 - CCCCS_SERC
        CC_NE = CC_NE['Capacity (MW)'].sum() / 1000 - CCCCS_NE
        CC_NY = CC_NY['Capacity (MW)'].sum() / 1000 - CCCCS_NY
        CC_MISO = CC_MISO['Capacity (MW)'].sum() / 1000 - CCCCS_MISO
        CC_PJM = CC_PJM['Capacity (MW)'].sum() / 1000 - CCCCS_PJM
        CC_SPP = CC_SPP['Capacity (MW)'].sum() / 1000 - CCCCS_SPP

        Nuclear_SERC = Nuclear_SERC['Capacity (MW)'].sum() / 1000
        Nuclear_NE = Nuclear_NE['Capacity (MW)'].sum() / 1000
        Nuclear_NY = Nuclear_NY['Capacity (MW)'].sum() / 1000
        Nuclear_MISO = Nuclear_MISO['Capacity (MW)'].sum() / 1000
        Nuclear_PJM = Nuclear_PJM['Capacity (MW)'].sum() / 1000
        Nuclear_SPP = Nuclear_SPP['Capacity (MW)'].sum() / 1000

        Hydrogen_SERC = Hydrogen_SERC['Capacity (MW)'].sum() / 1000
        Hydrogen_NE = Hydrogen_NE['Capacity (MW)'].sum() / 1000
        Hydrogen_NY = Hydrogen_NY['Capacity (MW)'].sum() / 1000
        Hydrogen_MISO = Hydrogen_MISO['Capacity (MW)'].sum() / 1000
        Hydrogen_PJM = Hydrogen_PJM['Capacity (MW)'].sum() / 1000
        Hydrogen_SPP = Hydrogen_SPP['Capacity (MW)'].sum() / 1000

        Battery_SERC = Battery_SERC['Capacity (MW)'].sum() / 1000
        Battery_NE = Battery_NE['Capacity (MW)'].sum() / 1000
        Battery_NY = Battery_NY['Capacity (MW)'].sum() / 1000
        Battery_MISO = Battery_MISO['Capacity (MW)'].sum() / 1000
        Battery_PJM = Battery_PJM['Capacity (MW)'].sum() / 1000
        Battery_SPP = Battery_SPP['Capacity (MW)'].sum() / 1000

        DAC_SERC = DAC_SERC['Capacity (MW)'].sum() / 1000
        DAC_NE = DAC_NE['Capacity (MW)'].sum() / 1000
        DAC_NY = DAC_NY['Capacity (MW)'].sum() / 1000
        DAC_MISO = DAC_MISO['Capacity (MW)'].sum() / 1000
        DAC_PJM = DAC_PJM['Capacity (MW)'].sum() / 1000
        DAC_SPP = DAC_SPP['Capacity (MW)'].sum() / 1000

        Wind1_SERC = Wind1_SERC['Capacity (MW)'].sum() / 1000
        Wind1_NE = Wind1_NE['Capacity (MW)'].sum() / 1000
        Wind1_NY = Wind1_NY['Capacity (MW)'].sum() / 1000
        Wind1_MISO = Wind1_MISO['Capacity (MW)'].sum() / 1000
        Wind1_PJM = Wind1_PJM['Capacity (MW)'].sum() / 1000
        Wind1_SPP = Wind1_SPP['Capacity (MW)'].sum() / 1000

        Wind2_SERC = Wind2_SERC['Capacity (MW)'].sum() / 1000
        Wind2_NE = Wind2_NE['Capacity (MW)'].sum() / 1000
        Wind2_NY = Wind2_NY['Capacity (MW)'].sum() / 1000
        Wind2_MISO = Wind2_MISO['Capacity (MW)'].sum() / 1000
        Wind2_PJM = Wind2_PJM['Capacity (MW)'].sum() / 1000
        Wind2_SPP = Wind2_SPP['Capacity (MW)'].sum() / 1000

        Solar1_SERC = Solar1_SERC['Capacity (MW)'].sum() / 1000
        Solar1_NE = Solar1_NE['Capacity (MW)'].sum() / 1000
        Solar1_NY = Solar1_NY['Capacity (MW)'].sum() / 1000
        Solar1_MISO = Solar1_MISO['Capacity (MW)'].sum() / 1000
        Solar1_PJM = Solar1_PJM['Capacity (MW)'].sum() / 1000
        Solar1_SPP = Solar1_SPP['Capacity (MW)'].sum() / 1000

        Solar2_SERC = Solar2_SERC['Capacity (MW)'].sum() / 1000
        Solar2_NE = Solar2_NE['Capacity (MW)'].sum() / 1000
        Solar2_NY = Solar2_NY['Capacity (MW)'].sum() / 1000
        Solar2_MISO = Solar2_MISO['Capacity (MW)'].sum() / 1000
        Solar2_PJM = Solar2_PJM['Capacity (MW)'].sum() / 1000
        Solar2_SPP = Solar2_SPP['Capacity (MW)'].sum() / 1000

        Wind_SERC = Wind1_SERC + Wind2_SERC
        Wind_NE = Wind1_NE + Wind2_NE
        Wind_NY = Wind1_NY + Wind2_NY
        Wind_MISO = Wind1_MISO + Wind2_MISO
        Wind_PJM = Wind1_PJM + Wind2_PJM
        Wind_SPP = Wind1_SPP + Wind2_SPP

        Solar_SERC = Solar1_SERC + Solar2_SERC
        Solar_NE = Solar1_NE + Solar2_NE
        Solar_NY = Solar1_NY + Solar2_NY
        Solar_MISO = Solar1_MISO + Solar2_MISO
        Solar_PJM = Solar1_PJM + Solar2_PJM
        Solar_SPP = Solar1_SPP + Solar2_SPP

        CoalCCS_NW = 0
        CoalCCS_SW = 0
        CoalCCS_NOE = 0
        CoalCCS_SE = 0

        CCCCS_NW = 0
        CCCCS_SW = 0
        CCCCS_NOE = 0
        CCCCS_SE = 0

        CC_NW = 0
        CC_SW = 0
        CC_NOE = 0
        CC_SE = 0

        Nuclear_NW = 0
        Nuclear_SW = 0
        Nuclear_NOE = 0
        Nuclear_SE = 0

        Hydrogen_NW = 0
        Hydrogen_SW = 0
        Hydrogen_NOE = 0
        Hydrogen_SE = 0

        Battery_NW = 0
        Battery_SW = 0
        Battery_NOE = 0
        Battery_SE = 0

        DAC_NW = 0
        DAC_SW = 0
        DAC_NOE = 0
        DAC_SE = 0

        Wind_NW = 0
        Wind_SW = 0
        Wind_NOE = 0
        Wind_SE = 0

        Solar_NW = 0
        Solar_SW = 0
        Solar_NOE = 0
        Solar_SE = 0

        if planningScr == 'NE2050' or planningScr == 'NE2051':
            CoalCCS_SERC_2 = CoalCCS_2[CoalCCS_2['region'].str.contains('SERC')]
            CoalCCS_NE_2 = CoalCCS_2[CoalCCS_2['region'].str.contains('NE')]
            CoalCCS_NY_2 = CoalCCS_2[CoalCCS_2['region'].str.contains('NY')]
            CoalCCS_MISO_2 = CoalCCS_2[CoalCCS_2['region'].str.contains('MISO')]
            CoalCCS_PJM_2 = CoalCCS_2[CoalCCS_2['region'].str.contains('PJM')]
            CoalCCS_SPP_2 = CoalCCS_2[CoalCCS_2['region'].str.contains('SPP')]

            CC_SERC_2 = CC_2[CC_2['region'].str.contains('SERC')]
            CC_NE_2 = CC_2[CC_2['region'].str.contains('NE')]
            CC_NY_2 = CC_2[CC_2['region'].str.contains('NY')]
            CC_MISO_2 = CC_2[CC_2['region'].str.contains('MISO')]
            CC_PJM_2 = CC_2[CC_2['region'].str.contains('PJM')]
            CC_SPP_2 = CC_2[CC_2['region'].str.contains('SPP')]

            CCCCS_SERC_2 = CCCCS_2[CCCCS_2['region'].str.contains('SERC')]
            CCCCS_NE_2 = CCCCS_2[CCCCS_2['region'].str.contains('NE')]
            CCCCS_NY_2 = CCCCS_2[CCCCS_2['region'].str.contains('NY')]
            CCCCS_MISO_2 = CCCCS_2[CCCCS_2['region'].str.contains('MISO')]
            CCCCS_PJM_2 = CCCCS_2[CCCCS_2['region'].str.contains('PJM')]
            CCCCS_SPP_2 = CCCCS_2[CCCCS_2['region'].str.contains('SPP')]

            Nuclear_SERC_2 = Nuclear_2[Nuclear_2['region'].str.contains('SERC')]
            Nuclear_NE_2 = Nuclear_2[Nuclear_2['region'].str.contains('NE')]
            Nuclear_NY_2 = Nuclear_2[Nuclear_2['region'].str.contains('NY')]
            Nuclear_MISO_2 = Nuclear_2[Nuclear_2['region'].str.contains('MISO')]
            Nuclear_PJM_2 = Nuclear_2[Nuclear_2['region'].str.contains('PJM')]
            Nuclear_SPP_2 = Nuclear_2[Nuclear_2['region'].str.contains('SPP')]

            Hydrogen_SERC_2 = Hydrogen_2[Hydrogen_2['region'].str.contains('SERC')]
            Hydrogen_NE_2 = Hydrogen_2[Hydrogen_2['region'].str.contains('NE')]
            Hydrogen_NY_2 = Hydrogen_2[Hydrogen_2['region'].str.contains('NY')]
            Hydrogen_MISO_2 = Hydrogen_2[Hydrogen_2['region'].str.contains('MISO')]
            Hydrogen_PJM_2 = Hydrogen_2[Hydrogen_2['region'].str.contains('PJM')]
            Hydrogen_SPP_2 = Hydrogen_2[Hydrogen_2['region'].str.contains('SPP')]

            Battery_SERC_2 = Battery_2[Battery_2['region'].str.contains('SERC')]
            Battery_NE_2 = Battery_2[Battery_2['region'].str.contains('NE')]
            Battery_NY_2 = Battery_2[Battery_2['region'].str.contains('NY')]
            Battery_MISO_2 = Battery_2[Battery_2['region'].str.contains('MISO')]
            Battery_PJM_2 = Battery_2[Battery_2['region'].str.contains('PJM')]
            Battery_SPP_2 = Battery_2[Battery_2['region'].str.contains('SPP')]

            DAC_SERC_2 = DAC_2[DAC_2['region'].str.contains('SERC')]
            DAC_NE_2 = DAC_2[DAC_2['region'].str.contains('NE')]
            DAC_NY_2 = DAC_2[DAC_2['region'].str.contains('NY')]
            DAC_MISO_2 = DAC_2[DAC_2['region'].str.contains('MISO')]
            DAC_PJM_2 = DAC_2[DAC_2['region'].str.contains('PJM')]
            DAC_SPP_2 = DAC_2[DAC_2['region'].str.contains('SPP')]

            Wind1_SERC_2 = Wind1_2[Wind1_2['region'].str.contains('SERC')]
            Wind1_NE_2 = Wind1_2[Wind1_2['region'].str.contains('NE')]
            Wind1_NY_2 = Wind1_2[Wind1_2['region'].str.contains('NY')]
            Wind1_MISO_2 = Wind1_2[Wind1_2['region'].str.contains('MISO')]
            Wind1_PJM_2 = Wind1_2[Wind1_2['region'].str.contains('PJM')]
            Wind1_SPP_2 = Wind1_2[Wind1_2['region'].str.contains('SPP')]

            Wind2_SERC_2 = Wind2_2[Wind2_2['region'].str.contains('SERC')]
            Wind2_NE_2 = Wind2_2[Wind2_2['region'].str.contains('NE')]
            Wind2_NY_2 = Wind2_2[Wind2_2['region'].str.contains('NY')]
            Wind2_MISO_2 = Wind2_2[Wind2_2['region'].str.contains('MISO')]
            Wind2_PJM_2 = Wind2_2[Wind2_2['region'].str.contains('PJM')]
            Wind2_SPP_2 = Wind2_2[Wind2_2['region'].str.contains('SPP')]

            Solar1_SERC_2 = Solar1_2[Solar1_2['region'].str.contains('SERC')]
            Solar1_NE_2 = Solar1_2[Solar1_2['region'].str.contains('NE')]
            Solar1_NY_2 = Solar1_2[Solar1_2['region'].str.contains('NY')]
            Solar1_MISO_2 = Solar1_2[Solar1_2['region'].str.contains('MISO')]
            Solar1_PJM_2 = Solar1_2[Solar1_2['region'].str.contains('PJM')]
            Solar1_SPP_2 = Solar1_2[Solar1_2['region'].str.contains('SPP')]

            Solar2_SERC_2 = Solar2_2[Solar2_2['region'].str.contains('SERC')]
            Solar2_NE_2 = Solar2_2[Solar2_2['region'].str.contains('NE')]
            Solar2_NY_2 = Solar2_2[Solar2_2['region'].str.contains('NY')]
            Solar2_MISO_2 = Solar2_2[Solar2_2['region'].str.contains('MISO')]
            Solar2_PJM_2 = Solar2_2[Solar2_2['region'].str.contains('PJM')]
            Solar2_SPP_2 = Solar2_2[Solar2_2['region'].str.contains('SPP')]

            CoalCCS_SERC_2 = CoalCCS_SERC_2['Capacity (MW)'].sum() / 1000
            CoalCCS_NE_2 = CoalCCS_NE_2['Capacity (MW)'].sum() / 1000
            CoalCCS_NY_2 = CoalCCS_NY_2['Capacity (MW)'].sum() / 1000
            CoalCCS_MISO_2 = CoalCCS_MISO_2['Capacity (MW)'].sum() / 1000
            CoalCCS_PJM_2 = CoalCCS_PJM_2['Capacity (MW)'].sum() / 1000
            CoalCCS_SPP_2 = CoalCCS_SPP_2['Capacity (MW)'].sum() / 1000

            CCCCS_SERC_2 = CCCCS_SERC_2['Capacity (MW)'].sum() / 1000
            CCCCS_NE_2 = CCCCS_NE_2['Capacity (MW)'].sum() / 1000
            CCCCS_NY_2 = CCCCS_NY_2['Capacity (MW)'].sum() / 1000
            CCCCS_MISO_2 = CCCCS_MISO_2['Capacity (MW)'].sum() / 1000
            CCCCS_PJM_2 = CCCCS_PJM_2['Capacity (MW)'].sum() / 1000
            CCCCS_SPP_2 = CCCCS_SPP_2['Capacity (MW)'].sum() / 1000

            CC_SERC_2 = CC_SERC_2['Capacity (MW)'].sum() / 1000 - CCCCS_SERC_2
            CC_NE_2 = CC_NE_2['Capacity (MW)'].sum() / 1000 - CCCCS_NE_2
            CC_NY_2 = CC_NY_2['Capacity (MW)'].sum() / 1000 - CCCCS_NY_2
            CC_MISO_2 = CC_MISO_2['Capacity (MW)'].sum() / 1000 - CCCCS_MISO_2
            CC_PJM_2 = CC_PJM_2['Capacity (MW)'].sum() / 1000 - CCCCS_PJM_2
            CC_SPP_2 = CC_SPP_2['Capacity (MW)'].sum() / 1000 - CCCCS_SPP_2

            Nuclear_SERC_2 = Nuclear_SERC_2['Capacity (MW)'].sum() / 1000
            Nuclear_NE_2 = Nuclear_NE_2['Capacity (MW)'].sum() / 1000
            Nuclear_NY_2 = Nuclear_NY_2['Capacity (MW)'].sum() / 1000
            Nuclear_MISO_2 = Nuclear_MISO_2['Capacity (MW)'].sum() / 1000
            Nuclear_PJM_2 = Nuclear_PJM_2['Capacity (MW)'].sum() / 1000
            Nuclear_SPP_2 = Nuclear_SPP_2['Capacity (MW)'].sum() / 1000

            Hydrogen_SERC_2 = Hydrogen_SERC_2['Capacity (MW)'].sum() / 1000
            Hydrogen_NE_2 = Hydrogen_NE_2['Capacity (MW)'].sum() / 1000
            Hydrogen_NY_2 = Hydrogen_NY_2['Capacity (MW)'].sum() / 1000
            Hydrogen_MISO_2 = Hydrogen_MISO_2['Capacity (MW)'].sum() / 1000
            Hydrogen_PJM_2 = Hydrogen_PJM_2['Capacity (MW)'].sum() / 1000
            Hydrogen_SPP_2 = Hydrogen_SPP_2['Capacity (MW)'].sum() / 1000

            Battery_SERC_2 = Battery_SERC_2['Capacity (MW)'].sum() / 1000
            Battery_NE_2 = Battery_NE_2['Capacity (MW)'].sum() / 1000
            Battery_NY_2 = Battery_NY_2['Capacity (MW)'].sum() / 1000
            Battery_MISO_2 = Battery_MISO_2['Capacity (MW)'].sum() / 1000
            Battery_PJM_2 = Battery_PJM_2['Capacity (MW)'].sum() / 1000
            Battery_SPP_2 = Battery_SPP_2['Capacity (MW)'].sum() / 1000

            DAC_SERC_2 = DAC_SERC_2['Capacity (MW)'].sum() / 1000
            DAC_NE_2 = DAC_NE_2['Capacity (MW)'].sum() / 1000
            DAC_NY_2 = DAC_NY_2['Capacity (MW)'].sum() / 1000
            DAC_MISO_2 = DAC_MISO_2['Capacity (MW)'].sum() / 1000
            DAC_PJM_2 = DAC_PJM_2['Capacity (MW)'].sum() / 1000
            DAC_SPP_2 = DAC_SPP_2['Capacity (MW)'].sum() / 1000

            Wind1_SERC_2 = Wind1_SERC_2['Capacity (MW)'].sum() / 1000
            Wind1_NE_2 = Wind1_NE_2['Capacity (MW)'].sum() / 1000
            Wind1_NY_2 = Wind1_NY_2['Capacity (MW)'].sum() / 1000
            Wind1_MISO_2 = Wind1_MISO_2['Capacity (MW)'].sum() / 1000
            Wind1_PJM_2 = Wind1_PJM_2['Capacity (MW)'].sum() / 1000
            Wind1_SPP_2 = Wind1_SPP_2['Capacity (MW)'].sum() / 1000

            Wind2_SERC_2 = Wind2_SERC_2['Capacity (MW)'].sum() / 1000
            Wind2_NE_2 = Wind2_NE_2['Capacity (MW)'].sum() / 1000
            Wind2_NY_2 = Wind2_NY_2['Capacity (MW)'].sum() / 1000
            Wind2_MISO_2 = Wind2_MISO_2['Capacity (MW)'].sum() / 1000
            Wind2_PJM_2 = Wind2_PJM_2['Capacity (MW)'].sum() / 1000
            Wind2_SPP_2 = Wind2_SPP_2['Capacity (MW)'].sum() / 1000

            Solar1_SERC_2 = Solar1_SERC_2['Capacity (MW)'].sum() / 1000
            Solar1_NE_2 = Solar1_NE_2['Capacity (MW)'].sum() / 1000
            Solar1_NY_2 = Solar1_NY_2['Capacity (MW)'].sum() / 1000
            Solar1_MISO_2 = Solar1_MISO_2['Capacity (MW)'].sum() / 1000
            Solar1_PJM_2 = Solar1_PJM_2['Capacity (MW)'].sum() / 1000
            Solar1_SPP_2 = Solar1_SPP_2['Capacity (MW)'].sum() / 1000

            Solar2_SERC_2 = Solar2_SERC_2['Capacity (MW)'].sum() / 1000
            Solar2_NE_2 = Solar2_NE_2['Capacity (MW)'].sum() / 1000
            Solar2_NY_2 = Solar2_NY_2['Capacity (MW)'].sum() / 1000
            Solar2_MISO_2 = Solar2_MISO_2['Capacity (MW)'].sum() / 1000
            Solar2_PJM_2 = Solar2_PJM_2['Capacity (MW)'].sum() / 1000
            Solar2_SPP_2 = Solar2_SPP_2['Capacity (MW)'].sum() / 1000

            Wind_SERC_2 = Wind1_SERC_2 + Wind2_SERC_2
            Wind_NE_2 = Wind1_NE_2 + Wind2_NE_2
            Wind_NY_2 = Wind1_NY_2 + Wind2_NY_2
            Wind_MISO_2 = Wind1_MISO_2 + Wind2_MISO_2
            Wind_PJM_2 = Wind1_PJM_2 + Wind2_PJM_2
            Wind_SPP_2 = Wind1_SPP_2 + Wind2_SPP_2

            Solar_SERC_2 = Solar1_SERC_2 + Solar2_SERC_2
            Solar_NE_2 = Solar1_NE_2 + Solar2_NE_2
            Solar_NY_2 = Solar1_NY_2 + Solar2_NY_2
            Solar_MISO_2 = Solar1_MISO_2 + Solar2_MISO_2
            Solar_PJM_2 = Solar1_PJM_2 + Solar2_PJM_2
            Solar_SPP_2 = Solar1_SPP_2 + Solar2_SPP_2
        else:
            CoalCCS_SERC_2 = 0
            CoalCCS_NE_2 = 0
            CoalCCS_NY_2 = 0
            CoalCCS_MISO_2 = 0
            CoalCCS_PJM_2 = 0
            CoalCCS_SPP_2 = 0

            CCCCS_SERC_2 = 0
            CCCCS_NE_2 = 0
            CCCCS_NY_2 = 0
            CCCCS_MISO_2 = 0
            CCCCS_PJM_2 = 0
            CCCCS_SPP_2 = 0

            CC_SERC_2 = 0
            CC_NE_2 = 0
            CC_NY_2 = 0
            CC_MISO_2 = 0
            CC_PJM_2 = 0
            CC_SPP_2 = 0

            Nuclear_SERC_2 = 0
            Nuclear_NE_2 = 0
            Nuclear_NY_2 = 0
            Nuclear_MISO_2 = 0
            Nuclear_PJM_2 = 0
            Nuclear_SPP_2 = 0

            Hydrogen_SERC_2 = 0
            Hydrogen_NE_2 = 0
            Hydrogen_NY_2 = 0
            Hydrogen_MISO_2 = 0
            Hydrogen_PJM_2 = 0
            Hydrogen_SPP_2 = 0

            Battery_SERC_2 = 0
            Battery_NE_2 = 0
            Battery_NY_2 = 0
            Battery_MISO_2 = 0
            Battery_PJM_2 = 0
            Battery_SPP_2 = 0

            DAC_SERC_2 = 0
            DAC_NE_2 = 0
            DAC_NY_2 = 0
            DAC_MISO_2 = 0
            DAC_PJM_2 = 0
            DAC_SPP_2 = 0

            Wind_SERC_2 = 0
            Wind_NE_2 = 0
            Wind_NY_2 = 0
            Wind_MISO_2 = 0
            Wind_PJM_2 = 0
            Wind_SPP_2 = 0

            Solar_SERC_2 = 0
            Solar_NE_2 = 0
            Solar_NY_2 = 0
            Solar_MISO_2 = 0
            Solar_PJM_2 = 0
            Solar_SPP_2 = 0

        CoalCCS_NW_2 = 0
        CoalCCS_SW_2 = 0
        CoalCCS_NOE_2 = 0
        CoalCCS_SE_2 = 0

        CCCCS_NW_2 = 0
        CCCCS_SW_2 = 0
        CCCCS_NOE_2 = 0
        CCCCS_SE_2 = 0

        CC_NW_2 = 0
        CC_SW_2 = 0
        CC_NOE_2 = 0
        CC_SE_2 = 0

        Nuclear_NW_2 = 0
        Nuclear_SW_2 = 0
        Nuclear_NOE_2 = 0
        Nuclear_SE_2 = 0

        Hydrogen_NW_2 = 0
        Hydrogen_SW_2 = 0
        Hydrogen_NOE_2 = 0
        Hydrogen_SE_2 = 0

        Battery_NW_2 = 0
        Battery_SW_2 = 0
        Battery_NOE_2 = 0
        Battery_SE_2 = 0

        DAC_NW_2 = 0
        DAC_SW_2 = 0
        DAC_NOE_2 = 0
        DAC_SE_2 = 0

        Wind_NW_2 = 0
        Wind_SW_2 = 0
        Wind_NOE_2 = 0
        Wind_SE_2 = 0

        Solar_NW_2 = 0
        Solar_SW_2 = 0
        Solar_NOE_2 = 0
        Solar_SE_2 = 0

    elif interConn == 'ERCOT':
        CoalCCS_NW = CoalCCS[CoalCCS['region2'].str.contains('ERCOT NW')]
        CoalCCS_SW = CoalCCS[CoalCCS['region2'].str.contains('ERCOT SW')]
        CoalCCS_NOE = CoalCCS[CoalCCS['region2'].str.contains('ERCOT NE')]
        CoalCCS_SE = CoalCCS[CoalCCS['region2'].str.contains('ERCOT SE')]

        CC_NW = CC[CC['region2'].str.contains('ERCOT NW')]
        CC_SW = CC[CC['region2'].str.contains('ERCOT SW')]
        CC_NOE = CC[CC['region2'].str.contains('ERCOT NE')]
        CC_SE = CC[CC['region2'].str.contains('ERCOT SE')]

        CCCCS_NW = CCCCS[CCCCS['region2'].str.contains('ERCOT NW')]
        CCCCS_SW = CCCCS[CCCCS['region2'].str.contains('ERCOT SW')]
        CCCCS_NOE = CCCCS[CCCCS['region2'].str.contains('ERCOT NE')]
        CCCCS_SE = CCCCS[CCCCS['region2'].str.contains('ERCOT SE')]

        Nuclear_NW = Nuclear[Nuclear['region2'].str.contains('ERCOT NW')]
        Nuclear_SW = Nuclear[Nuclear['region2'].str.contains('ERCOT SW')]
        Nuclear_NOE = Nuclear[Nuclear['region2'].str.contains('ERCOT NE')]
        Nuclear_SE = Nuclear[Nuclear['region2'].str.contains('ERCOT SE')]

        Hydrogen_NW = Hydrogen[Hydrogen['region2'].str.contains('ERCOT NW')]
        Hydrogen_SW = Hydrogen[Hydrogen['region2'].str.contains('ERCOT SW')]
        Hydrogen_NOE = Hydrogen[Hydrogen['region2'].str.contains('ERCOT NE')]
        Hydrogen_SE = Hydrogen[Hydrogen['region2'].str.contains('ERCOT SE')]

        Battery_NW = Battery[Battery['region2'].str.contains('ERCOT NW')]
        Battery_SW = Battery[Battery['region2'].str.contains('ERCOT SW')]
        Battery_NOE = Battery[Battery['region2'].str.contains('ERCOT NE')]
        Battery_SE = Battery[Battery['region2'].str.contains('ERCOT SE')]

        DAC_NW = DAC[DAC['region2'].str.contains('ERCOT NW')]
        DAC_SW = DAC[DAC['region2'].str.contains('ERCOT SW')]
        DAC_NOE = DAC[DAC['region2'].str.contains('ERCOT NE')]
        DAC_SE = DAC[DAC['region2'].str.contains('ERCOT SE')]

        Wind1_NW = Wind1[Wind1['region2'].str.contains('ERCOT NW')]
        Wind1_SW = Wind1[Wind1['region2'].str.contains('ERCOT SW')]
        Wind1_NOE = Wind1[Wind1['region2'].str.contains('ERCOT NE')]
        Wind1_SE = Wind1[Wind1['region2'].str.contains('ERCOT SE')]

        Wind2_NW = Wind2[Wind2['region2'].str.contains('ERCOT NW')]
        Wind2_SW = Wind2[Wind2['region2'].str.contains('ERCOT SW')]
        Wind2_NOE = Wind2[Wind2['region2'].str.contains('ERCOT NE')]
        Wind2_SE = Wind2[Wind2['region2'].str.contains('ERCOT SE')]

        Solar1_NW = Solar1[Solar1['region2'].str.contains('ERCOT NW')]
        Solar1_SW = Solar1[Solar1['region2'].str.contains('ERCOT SW')]
        Solar1_NOE = Solar1[Solar1['region2'].str.contains('ERCOT NE')]
        Solar1_SE = Solar1[Solar1['region2'].str.contains('ERCOT SE')]

        Solar2_NW = Solar2[Solar2['region2'].str.contains('ERCOT NW')]
        Solar2_SW = Solar2[Solar2['region2'].str.contains('ERCOT SW')]
        Solar2_NOE = Solar2[Solar2['region2'].str.contains('ERCOT NE')]
        Solar2_SE = Solar2[Solar2['region2'].str.contains('ERCOT SE')]

        CoalCCS_NW = CoalCCS_NW['Capacity (MW)'].sum()/1000
        CoalCCS_SW = CoalCCS_SW['Capacity (MW)'].sum()/1000
        CoalCCS_NOE = CoalCCS_NOE['Capacity (MW)'].sum()/1000
        CoalCCS_SE = CoalCCS_SE['Capacity (MW)'].sum()/1000

        CCCCS_NW = CCCCS_NW['Capacity (MW)'].sum() / 1000
        CCCCS_SW = CCCCS_SW['Capacity (MW)'].sum() / 1000
        CCCCS_NOE = CCCCS_NOE['Capacity (MW)'].sum() / 1000
        CCCCS_SE = CCCCS_SE['Capacity (MW)'].sum() / 1000

        CC_NW = CC_NW['Capacity (MW)'].sum() / 1000 - CCCCS_NW
        CC_SW = CC_SW['Capacity (MW)'].sum() / 1000 - CCCCS_SW
        CC_NOE = CC_NOE['Capacity (MW)'].sum() / 1000 - CCCCS_NOE
        CC_SE = CC_SE['Capacity (MW)'].sum() / 1000 - CCCCS_SE

        Nuclear_NW = Nuclear_NW['Capacity (MW)'].sum() / 1000
        Nuclear_SW = Nuclear_SW['Capacity (MW)'].sum() / 1000
        Nuclear_NOE = Nuclear_NOE['Capacity (MW)'].sum() / 1000
        Nuclear_SE = Nuclear_SE['Capacity (MW)'].sum() / 1000

        Hydrogen_NW = Hydrogen_NW['Capacity (MW)'].sum() / 1000
        Hydrogen_SW = Hydrogen_SW['Capacity (MW)'].sum() / 1000
        Hydrogen_NOE = Hydrogen_NOE['Capacity (MW)'].sum() / 1000
        Hydrogen_SE = Hydrogen_SE['Capacity (MW)'].sum() / 1000

        Battery_NW = Battery_NW['Capacity (MW)'].sum() / 1000
        Battery_SW = Battery_SW['Capacity (MW)'].sum() / 1000
        Battery_NOE = Battery_NOE['Capacity (MW)'].sum() / 1000
        Battery_SE = Battery_SE['Capacity (MW)'].sum() / 1000

        DAC_NW = DAC_NW['Capacity (MW)'].sum() / 1000
        DAC_SW = DAC_SW['Capacity (MW)'].sum() / 1000
        DAC_NOE = DAC_NOE['Capacity (MW)'].sum() / 1000
        DAC_SE = DAC_SE['Capacity (MW)'].sum() / 1000

        Wind1_NW = Wind1_NW['Capacity (MW)'].sum() / 1000
        Wind1_SW = Wind1_SW['Capacity (MW)'].sum() / 1000
        Wind1_NOE = Wind1_NOE['Capacity (MW)'].sum() / 1000
        Wind1_SE = Wind1_SE['Capacity (MW)'].sum() / 1000

        Wind2_NW = Wind2_NW['Capacity (MW)'].sum() / 1000
        Wind2_SW = Wind2_SW['Capacity (MW)'].sum() / 1000
        Wind2_NOE = Wind2_NOE['Capacity (MW)'].sum() / 1000
        Wind2_SE = Wind2_SE['Capacity (MW)'].sum() / 1000

        Solar1_NW = Solar1_NW['Capacity (MW)'].sum() / 1000
        Solar1_SW = Solar1_SW['Capacity (MW)'].sum() / 1000
        Solar1_NOE = Solar1_NOE['Capacity (MW)'].sum() / 1000
        Solar1_SE = Solar1_SE['Capacity (MW)'].sum() / 1000

        Solar2_NW = Solar2_NW['Capacity (MW)'].sum() / 1000
        Solar2_SW = Solar2_SW['Capacity (MW)'].sum() / 1000
        Solar2_NOE = Solar2_NOE['Capacity (MW)'].sum() / 1000
        Solar2_SE = Solar2_SE['Capacity (MW)'].sum() / 1000

        Wind_NW = Wind1_NW + Wind2_NW
        Wind_SW = Wind1_SW + Wind2_SW
        Wind_NOE = Wind1_NOE + Wind2_NOE
        Wind_SE = Wind1_SE + Wind2_SE

        Solar_NW = Solar1_NW + Solar2_NW
        Solar_SW = Solar1_SW + Solar2_SW
        Solar_NOE = Solar1_NOE + Solar2_NOE
        Solar_SE = Solar1_SE + Solar2_SE

        CoalCCS_SERC = 0
        CoalCCS_NE = 0
        CoalCCS_NY = 0
        CoalCCS_MISO = 0
        CoalCCS_PJM = 0
        CoalCCS_SPP = 0

        CCCCS_SERC = 0
        CCCCS_NE = 0
        CCCCS_NY = 0
        CCCCS_MISO = 0
        CCCCS_PJM = 0
        CCCCS_SPP = 0

        CC_SERC = 0
        CC_NE = 0
        CC_NY = 0
        CC_MISO = 0
        CC_PJM = 0
        CC_SPP = 0

        Nuclear_SERC = 0
        Nuclear_NE = 0
        Nuclear_NY = 0
        Nuclear_MISO = 0
        Nuclear_PJM = 0
        Nuclear_SPP = 0

        Hydrogen_SERC = 0
        Hydrogen_NE = 0
        Hydrogen_NY = 0
        Hydrogen_MISO = 0
        Hydrogen_PJM = 0
        Hydrogen_SPP = 0

        Battery_SERC = 0
        Battery_NE = 0
        Battery_NY = 0
        Battery_MISO = 0
        Battery_PJM = 0
        Battery_SPP = 0

        DAC_SERC = 0
        DAC_NE = 0
        DAC_NY = 0
        DAC_MISO = 0
        DAC_PJM = 0
        DAC_SPP = 0

        Wind_SERC = 0
        Wind_NE = 0
        Wind_NY = 0
        Wind_MISO = 0
        Wind_PJM = 0
        Wind_SPP = 0

        Solar_SERC = 0
        Solar_NE = 0
        Solar_NY = 0
        Solar_MISO = 0
        Solar_PJM = 0
        Solar_SPP = 0

        if planningScr == 'NE2050' or planningScr == 'NE2051':
            CoalCCS_NW_2 = CoalCCS_2[CoalCCS_2['region2'].str.contains('ERCOT NW')]
            CoalCCS_SW_2 = CoalCCS_2[CoalCCS_2['region2'].str.contains('ERCOT SW')]
            CoalCCS_NOE_2 = CoalCCS_2[CoalCCS_2['region2'].str.contains('ERCOT NE')]
            CoalCCS_SE_2 = CoalCCS_2[CoalCCS_2['region2'].str.contains('ERCOT SE')]

            CC_NW_2 = CC_2[CC_2['region2'].str.contains('ERCOT NW')]
            CC_SW_2 = CC_2[CC_2['region2'].str.contains('ERCOT SW')]
            CC_NOE_2 = CC_2[CC_2['region2'].str.contains('ERCOT NE')]
            CC_SE_2 = CC_2[CC_2['region2'].str.contains('ERCOT SE')]

            CCCCS_NW_2 = CCCCS_2[CCCCS_2['region2'].str.contains('ERCOT NW')]
            CCCCS_SW_2 = CCCCS_2[CCCCS_2['region2'].str.contains('ERCOT SW')]
            CCCCS_NOE_2 = CCCCS_2[CCCCS_2['region2'].str.contains('ERCOT NE')]
            CCCCS_SE_2 = CCCCS_2[CCCCS_2['region2'].str.contains('ERCOT SE')]

            Nuclear_NW_2 = Nuclear_2[Nuclear_2['region2'].str.contains('ERCOT NW')]
            Nuclear_SW_2 = Nuclear_2[Nuclear_2['region2'].str.contains('ERCOT SW')]
            Nuclear_NOE_2 = Nuclear_2[Nuclear_2['region2'].str.contains('ERCOT NE')]
            Nuclear_SE_2 = Nuclear_2[Nuclear_2['region2'].str.contains('ERCOT SE')]

            Hydrogen_NW_2 = Hydrogen_2[Hydrogen_2['region2'].str.contains('ERCOT NW')]
            Hydrogen_SW_2 = Hydrogen_2[Hydrogen_2['region2'].str.contains('ERCOT SW')]
            Hydrogen_NOE_2 = Hydrogen_2[Hydrogen_2['region2'].str.contains('ERCOT NE')]
            Hydrogen_SE_2 = Hydrogen_2[Hydrogen_2['region2'].str.contains('ERCOT SE')]

            Battery_NW_2 = Battery_2[Battery_2['region2'].str.contains('ERCOT NW')]
            Battery_SW_2 = Battery_2[Battery_2['region2'].str.contains('ERCOT SW')]
            Battery_NOE_2 = Battery_2[Battery_2['region2'].str.contains('ERCOT NE')]
            Battery_SE_2 = Battery_2[Battery_2['region2'].str.contains('ERCOT SE')]

            DAC_NW_2 = DAC_2[DAC_2['region2'].str.contains('ERCOT NW')]
            DAC_SW_2 = DAC_2[DAC_2['region2'].str.contains('ERCOT SW')]
            DAC_NOE_2 = DAC_2[DAC_2['region2'].str.contains('ERCOT NE')]
            DAC_SE_2 = DAC_2[DAC_2['region2'].str.contains('ERCOT SE')]

            Wind1_NW_2 = Wind1_2[Wind1_2['region2'].str.contains('ERCOT NW')]
            Wind1_SW_2 = Wind1_2[Wind1_2['region2'].str.contains('ERCOT SW')]
            Wind1_NOE_2 = Wind1_2[Wind1_2['region2'].str.contains('ERCOT NE')]
            Wind1_SE_2 = Wind1_2[Wind1_2['region2'].str.contains('ERCOT SE')]

            Wind2_NW_2 = Wind2_2[Wind2_2['region2'].str.contains('ERCOT NW')]
            Wind2_SW_2 = Wind2_2[Wind2_2['region2'].str.contains('ERCOT SW')]
            Wind2_NOE_2 = Wind2_2[Wind2_2['region2'].str.contains('ERCOT NE')]
            Wind2_SE_2 = Wind2_2[Wind2_2['region2'].str.contains('ERCOT SE')]

            Solar1_NW_2 = Solar1_2[Solar1_2['region2'].str.contains('ERCOT NW')]
            Solar1_SW_2 = Solar1_2[Solar1_2['region2'].str.contains('ERCOT SW')]
            Solar1_NOE_2 = Solar1_2[Solar1_2['region2'].str.contains('ERCOT NE')]
            Solar1_SE_2 = Solar1_2[Solar1_2['region2'].str.contains('ERCOT SE')]

            Solar2_NW_2 = Solar2_2[Solar2_2['region2'].str.contains('ERCOT NW')]
            Solar2_SW_2 = Solar2_2[Solar2_2['region2'].str.contains('ERCOT SW')]
            Solar2_NOE_2 = Solar2_2[Solar2_2['region2'].str.contains('ERCOT NE')]
            Solar2_SE_2 = Solar2_2[Solar2_2['region2'].str.contains('ERCOT SE')]

            CoalCCS_NW_2 = CoalCCS_NW_2['Capacity (MW)'].sum() / 1000
            CoalCCS_SW_2 = CoalCCS_SW_2['Capacity (MW)'].sum() / 1000
            CoalCCS_NOE_2 = CoalCCS_NOE_2['Capacity (MW)'].sum() / 1000
            CoalCCS_SE_2 = CoalCCS_SE_2['Capacity (MW)'].sum() / 1000

            CCCCS_NW_2 = CCCCS_NW_2['Capacity (MW)'].sum() / 1000
            CCCCS_SW_2 = CCCCS_SW_2['Capacity (MW)'].sum() / 1000
            CCCCS_NOE_2 = CCCCS_NOE_2['Capacity (MW)'].sum() / 1000
            CCCCS_SE_2 = CCCCS_SE_2['Capacity (MW)'].sum() / 1000

            CC_NW_2 = CC_NW_2['Capacity (MW)'].sum() / 1000 - CCCCS_NW_2
            CC_SW_2 = CC_SW_2['Capacity (MW)'].sum() / 1000 - CCCCS_SW_2
            CC_NOE_2 = CC_NOE_2['Capacity (MW)'].sum() / 1000 - CCCCS_NOE_2
            CC_SE_2 = CC_SE_2['Capacity (MW)'].sum() / 1000 - CCCCS_SE_2

            Nuclear_NW_2 = Nuclear_NW_2['Capacity (MW)'].sum() / 1000
            Nuclear_SW_2 = Nuclear_SW_2['Capacity (MW)'].sum() / 1000
            Nuclear_NOE_2 = Nuclear_NOE_2['Capacity (MW)'].sum() / 1000
            Nuclear_SE_2 = Nuclear_SE_2['Capacity (MW)'].sum() / 1000

            Hydrogen_NW_2 = Hydrogen_NW_2['Capacity (MW)'].sum() / 1000
            Hydrogen_SW_2 = Hydrogen_SW_2['Capacity (MW)'].sum() / 1000
            Hydrogen_NOE_2 = Hydrogen_NOE_2['Capacity (MW)'].sum() / 1000
            Hydrogen_SE_2 = Hydrogen_SE_2['Capacity (MW)'].sum() / 1000

            Battery_NW_2 = Battery_NW_2['Capacity (MW)'].sum() / 1000
            Battery_SW_2 = Battery_SW_2['Capacity (MW)'].sum() / 1000
            Battery_NOE_2 = Battery_NOE_2['Capacity (MW)'].sum() / 1000
            Battery_SE_2 = Battery_SE_2['Capacity (MW)'].sum() / 1000

            DAC_NW_2 = DAC_NW_2['Capacity (MW)'].sum() / 1000
            DAC_SW_2 = DAC_SW_2['Capacity (MW)'].sum() / 1000
            DAC_NOE_2 = DAC_NOE_2['Capacity (MW)'].sum() / 1000
            DAC_SE_2 = DAC_SE_2['Capacity (MW)'].sum() / 1000

            Wind1_NW_2 = Wind1_NW_2['Capacity (MW)'].sum() / 1000
            Wind1_SW_2 = Wind1_SW_2['Capacity (MW)'].sum() / 1000
            Wind1_NOE_2 = Wind1_NOE_2['Capacity (MW)'].sum() / 1000
            Wind1_SE_2 = Wind1_SE_2['Capacity (MW)'].sum() / 1000

            Wind2_NW_2 = Wind2_NW_2['Capacity (MW)'].sum() / 1000
            Wind2_SW_2 = Wind2_SW_2['Capacity (MW)'].sum() / 1000
            Wind2_NOE_2 = Wind2_NOE_2['Capacity (MW)'].sum() / 1000
            Wind2_SE_2 = Wind2_SE_2['Capacity (MW)'].sum() / 1000

            Solar1_NW_2 = Solar1_NW_2['Capacity (MW)'].sum() / 1000
            Solar1_SW_2 = Solar1_SW_2['Capacity (MW)'].sum() / 1000
            Solar1_NOE_2 = Solar1_NOE_2['Capacity (MW)'].sum() / 1000
            Solar1_SE_2 = Solar1_SE_2['Capacity (MW)'].sum() / 1000

            Solar2_NW_2 = Solar2_NW_2['Capacity (MW)'].sum() / 1000
            Solar2_SW_2 = Solar2_SW_2['Capacity (MW)'].sum() / 1000
            Solar2_NOE_2 = Solar2_NOE_2['Capacity (MW)'].sum() / 1000
            Solar2_SE_2 = Solar2_SE_2['Capacity (MW)'].sum() / 1000

            Wind_NW_2 = Wind1_NW_2 + Wind2_NW_2
            Wind_SW_2 = Wind1_SW_2 + Wind2_SW_2
            Wind_NOE_2 = Wind1_NOE_2 + Wind2_NOE_2
            Wind_SE_2 = Wind1_SE_2 + Wind2_SE_2

            Solar_NW_2 = Solar1_NW_2 + Solar2_NW_2
            Solar_SW_2 = Solar1_SW_2 + Solar2_SW_2
            Solar_NOE_2 = Solar1_NOE_2 + Solar2_NOE_2
            Solar_SE_2 = Solar1_SE_2 + Solar2_SE_2
        else:
            CoalCCS_NW_2 = 0
            CoalCCS_SW_2 = 0
            CoalCCS_NOE_2 = 0
            CoalCCS_SE_2 = 0

            CCCCS_NW_2 = 0
            CCCCS_SW_2 = 0
            CCCCS_NOE_2 = 0
            CCCCS_SE_2 = 0

            CC_NW_2 = 0
            CC_SW_2 = 0
            CC_NOE_2 = 0
            CC_SE_2 = 0

            Nuclear_NW_2 = 0
            Nuclear_SW_2 = 0
            Nuclear_NOE_2 = 0
            Nuclear_SE_2 = 0

            Hydrogen_NW_2 = 0
            Hydrogen_SW_2 = 0
            Hydrogen_NOE_2 = 0
            Hydrogen_SE_2 = 0

            Battery_NW_2 = 0
            Battery_SW_2 = 0
            Battery_NOE_2 = 0
            Battery_SE_2 = 0

            DAC_NW_2 = 0
            DAC_SW_2 = 0
            DAC_NOE_2 = 0
            DAC_SE_2 = 0

            Wind_NW_2 = 0
            Wind_SW_2 = 0
            Wind_NOE_2 = 0
            Wind_SE_2 = 0

            Solar_NW_2 = 0
            Solar_SW_2 = 0
            Solar_NOE_2 = 0
            Solar_SE_2 = 0

        CoalCCS_SERC_2 = 0
        CoalCCS_NE_2 = 0
        CoalCCS_NY_2 = 0
        CoalCCS_MISO_2 = 0
        CoalCCS_PJM_2 = 0
        CoalCCS_SPP_2 = 0

        CCCCS_SERC_2 = 0
        CCCCS_NE_2 = 0
        CCCCS_NY_2 = 0
        CCCCS_MISO_2 = 0
        CCCCS_PJM_2 = 0
        CCCCS_SPP_2 = 0

        CC_SERC_2 = 0
        CC_NE_2 = 0
        CC_NY_2 = 0
        CC_MISO_2 = 0
        CC_PJM_2 = 0
        CC_SPP_2 = 0

        Nuclear_SERC_2 = 0
        Nuclear_NE_2 = 0
        Nuclear_NY_2 = 0
        Nuclear_MISO_2 = 0
        Nuclear_PJM_2 = 0
        Nuclear_SPP_2 = 0

        Hydrogen_SERC_2 = 0
        Hydrogen_NE_2 = 0
        Hydrogen_NY_2 = 0
        Hydrogen_MISO_2 = 0
        Hydrogen_PJM_2 = 0
        Hydrogen_SPP_2 = 0

        Battery_SERC_2 = 0
        Battery_NE_2 = 0
        Battery_NY_2 = 0
        Battery_MISO_2 = 0
        Battery_PJM_2 = 0
        Battery_SPP_2 = 0

        DAC_SERC_2 = 0
        DAC_NE_2 = 0
        DAC_NY_2 = 0
        DAC_MISO_2 = 0
        DAC_PJM_2 = 0
        DAC_SPP_2 = 0

        Wind_SERC_2 = 0
        Wind_NE_2 = 0
        Wind_NY_2 = 0
        Wind_MISO_2 = 0
        Wind_PJM_2 = 0
        Wind_SPP_2 = 0

        Solar_SERC_2 = 0
        Solar_NE_2 = 0
        Solar_NY_2 = 0
        Solar_MISO_2 = 0
        Solar_PJM_2 = 0
        Solar_SPP_2 = 0

    return (CoalCCS_SERC, CoalCCS_NE, CoalCCS_NY, CoalCCS_MISO, CoalCCS_PJM, CoalCCS_SPP,
            CCCCS_SERC, CCCCS_NE, CCCCS_NY, CCCCS_MISO, CCCCS_PJM, CCCCS_SPP,
            CC_SERC, CC_NE, CC_NY, CC_MISO, CC_PJM, CC_SPP,
            Nuclear_SERC, Nuclear_NE, Nuclear_NY, Nuclear_MISO, Nuclear_PJM, Nuclear_SPP,
            Hydrogen_SERC, Hydrogen_NE, Hydrogen_NY, Hydrogen_MISO, Hydrogen_PJM, Hydrogen_SPP,
            Battery_SERC, Battery_NE, Battery_NY, Battery_MISO, Battery_PJM, Battery_SPP,
            Wind_SERC, Wind_NE, Wind_NY, Wind_MISO, Wind_PJM, Wind_SPP,
            Solar_SERC, Solar_NE, Solar_NY, Solar_MISO, Solar_PJM, Solar_SPP,
            DAC_SERC, DAC_NE, DAC_NY, DAC_MISO, DAC_PJM, DAC_SPP,
            CoalCCS_NW, CoalCCS_SW, CoalCCS_NOE, CoalCCS_SE,
            CCCCS_NW, CCCCS_SW, CCCCS_NOE, CCCCS_SE,
            CC_NW, CC_SW, CC_NOE, CC_SE,
            Nuclear_NW, Nuclear_SW, Nuclear_NOE, Nuclear_SE,
            Hydrogen_NW, Hydrogen_SW, Hydrogen_NOE, Hydrogen_SE,
            Battery_NW, Battery_SW, Battery_NOE, Battery_SE,
            DAC_NW, DAC_SW, DAC_NOE, DAC_SE,
            Wind_NW, Wind_SW, Wind_NOE, Wind_SE,
            Solar_NW, Solar_SW, Solar_NOE, Solar_SE,
            CoalCCS_SERC_2, CoalCCS_NE_2, CoalCCS_NY_2, CoalCCS_MISO_2, CoalCCS_PJM_2, CoalCCS_SPP_2,
            CCCCS_SERC_2, CCCCS_NE_2, CCCCS_NY_2, CCCCS_MISO_2, CCCCS_PJM_2, CCCCS_SPP_2,
            CC_SERC_2, CC_NE_2, CC_NY_2, CC_MISO_2, CC_PJM_2, CC_SPP_2,
            Nuclear_SERC_2, Nuclear_NE_2, Nuclear_NY_2, Nuclear_MISO_2, Nuclear_PJM_2, Nuclear_SPP_2,
            Hydrogen_SERC_2, Hydrogen_NE_2, Hydrogen_NY_2, Hydrogen_MISO_2, Hydrogen_PJM_2, Hydrogen_SPP_2,
            Battery_SERC_2, Battery_NE_2, Battery_NY_2, Battery_MISO_2, Battery_PJM_2, Battery_SPP_2,
            Wind_SERC_2, Wind_NE_2, Wind_NY_2, Wind_MISO_2, Wind_PJM_2, Wind_SPP_2,
            Solar_SERC_2, Solar_NE_2, Solar_NY_2, Solar_MISO_2, Solar_PJM_2, Solar_SPP_2,
            DAC_SERC_2, DAC_NE_2, DAC_NY_2, DAC_MISO_2, DAC_PJM_2, DAC_SPP_2,
            CoalCCS_NW_2, CoalCCS_SW_2, CoalCCS_NOE_2, CoalCCS_SE_2,
            CCCCS_NW_2, CCCCS_SW_2, CCCCS_NOE_2, CCCCS_SE_2,
            CC_NW_2, CC_SW_2, CC_NOE_2, CC_SE_2,
            Nuclear_NW_2, Nuclear_SW_2, Nuclear_NOE_2, Nuclear_SE_2,
            Hydrogen_NW_2, Hydrogen_SW_2, Hydrogen_NOE_2, Hydrogen_SE_2,
            Battery_NW_2, Battery_SW_2, Battery_NOE_2, Battery_SE_2,
            DAC_NW_2, DAC_SW_2, DAC_NOE_2, DAC_SE_2,
            Wind_NW_2, Wind_SW_2, Wind_NOE_2, Wind_SE_2,
            Solar_NW_2, Solar_SW_2, Solar_NOE_2, Solar_SE_2)