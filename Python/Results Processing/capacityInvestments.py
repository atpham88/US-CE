
import pandas as pd

def capInvestments(results_dir_temp, techCase, planningScr, interConn):
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

    cap_exp = cap_data[cap_data.YearAddedCE > 2020]
    cap_exp_2 = cap_data[cap_data.YearAddedCE > 2050]
    cap_exp = cap_exp[['PlantType', 'Capacity (MW)']]
    cap_exp_2 = cap_exp_2[['PlantType', 'Capacity (MW)']]

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

    CoalCCS = CoalCCS['Capacity (MW)'].sum()/1000
    CCCCS = CCCCS['Capacity (MW)'].sum()/1000
    CC = CC['Capacity (MW)'].sum()/1000 - CCCCS
    Nuclear = Nuclear['Capacity (MW)'].sum()/1000
    Hydrogen = Hydrogen['Capacity (MW)'].sum()/1000
    Battery = Battery['Capacity (MW)'].sum()/1000
    DAC = DAC['Capacity (MW)'].sum()/1000
    Wind1 = Wind1['Capacity (MW)'].sum()/1000
    Solar1 = Solar1['Capacity (MW)'].sum()/1000
    Wind2 = Wind2['Capacity (MW)'].sum() / 1000
    Solar2 = Solar2['Capacity (MW)'].sum() / 1000
    Wind = Wind1 + Wind2
    Solar = Solar1 + Solar2

    # Only expanded in 2060:
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

    CoalCCS_2 = CoalCCS_2['Capacity (MW)'].sum() / 1000
    CCCCS_2 = CCCCS_2['Capacity (MW)'].sum() / 1000
    CC_2 = CC_2['Capacity (MW)'].sum() / 1000 - CCCCS_2
    Nuclear_2 = Nuclear_2['Capacity (MW)'].sum() / 1000
    Hydrogen_2 = Hydrogen_2['Capacity (MW)'].sum() / 1000
    Battery_2 = Battery_2['Capacity (MW)'].sum() / 1000
    DAC_2 = DAC_2['Capacity (MW)'].sum() / 1000
    Wind1_2 = Wind1_2['Capacity (MW)'].sum() / 1000
    Solar1_2 = Solar1_2['Capacity (MW)'].sum() / 1000
    Wind2_2 = Wind2_2['Capacity (MW)'].sum() / 1000
    Solar2_2 = Solar2_2['Capacity (MW)'].sum() / 1000
    Wind_2 = Wind1_2 + Wind2_2
    Solar_2 = Solar1_2 + Solar2_2

    return (CoalCCS, CCCCS, CC, Nuclear, Hydrogen, Battery, DAC, Wind, Solar,
            CoalCCS_2, CCCCS_2, CC_2, Nuclear_2, Hydrogen_2, Battery_2, DAC_2, Wind_2, Solar_2)