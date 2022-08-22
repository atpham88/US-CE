
import pandas as pd

def costCal(results_dir_temp, techCase, planningScr, interConn, elec):
    if interConn == 'EI':
        finalCap = '-724'
    elif interConn == 'ERCOT':
        finalCap = '-90'

    if techCase == 'Stringent Cap':
        if interConn == 'EI':
            finalCap = '-1932'
        elif interConn == 'ERCOT':
            finalCap = '-241'

    if elec == True:
        if planningScr == 'NE2020':
            results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2020_reference' + '_TrueREFERENCE\\2050CO2Cap' + finalCap + '\\CE\\'
        elif planningScr == 'NE2050':
            results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2050_reference' + '_TrueREFERENCE\\2060CO2Cap' + finalCap + '\\CE\\'
            results_dir_2050 = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2050_reference' + '_TrueREFERENCE\\2050CO2Cap' + finalCap + '\\CE\\'
        elif planningScr == 'NE2051':
            results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2051NEin2050_reference' + '_TrueREFERENCE\\2060CO2Cap' + finalCap + '\\CE\\'
            results_dir_2050 = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2051NEin2050_reference'+ '_TrueREFERENCE\\2050CO2Cap' + finalCap + '\\CE\\'
    elif elec == False:
        if planningScr == 'NE2020':
            results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2020_reference' + '_TrueHIGH\\2050CO2Cap' + finalCap + '\\CE\\'
        elif planningScr == 'NE2050':
            results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2050_reference' + '_TrueHIGH\\2060CO2Cap' + finalCap + '\\CE\\'
            results_dir_2050 = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2020NEin2050_reference' + '_TrueHIGH\\2050CO2Cap' + finalCap + '\\CE\\'
        elif planningScr == 'NE2051':
            results_dir = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2051NEin2050_reference' + '_TrueHIGH\\2060CO2Cap' + finalCap + '\\CE\\'
            results_dir_2050 = results_dir_temp + interConn + '\\' + techCase + '\\' + 'Results_' + interConn + '_Negative' + finalCap + '_DACS2051NEin2050_reference' + '_TrueHIGH\\2050CO2Cap' + finalCap + '\\CE\\'

    if planningScr == 'NE2020':
        totCost_data = pd.read_csv(results_dir +'vZannualCE2050.csv',header=None)
        totCost_data = totCost_data.iloc[0, 0] / 1000000
        opCost_data = pd.read_csv(results_dir + 'vVarcostannualCE2050.csv', header=None)
        opCost_data = opCost_data.iloc[0, 0] / 1000000
        fixedCost_data = totCost_data - opCost_data
        totCost_data1 = 0
        opCost_data1 = 0
        fixedCost_data1 = 0
    elif planningScr == 'NE2050' or planningScr == 'NE2051':
        totCost_data1 = pd.read_csv(results_dir + 'vZannualCE2060.csv', header=None)
        totCost_data1 = totCost_data1.iloc[0, 0] / 1000000
        opCost_data1 = pd.read_csv(results_dir + 'vVarcostannualCE2060.csv', header=None)
        opCost_data1 = opCost_data1.iloc[0, 0] / 1000000
        fixedCost_data1 = totCost_data1 - opCost_data1

        totCost_data2 = pd.read_csv(results_dir_2050 + 'vZannualCE2050.csv', header=None)
        totCost_data2 = totCost_data2.iloc[0, 0] / 1000000
        opCost_data2 = pd.read_csv(results_dir_2050 + 'vVarcostannualCE2050.csv', header=None)
        opCost_data2 = opCost_data2.iloc[0, 0] / 1000000
        fixedCost_data2 = totCost_data2 - opCost_data2

        fixedCost_data = fixedCost_data1 + fixedCost_data2
        opCost_data = opCost_data1
        totCost_data = fixedCost_data + opCost_data

    return (totCost_data, opCost_data, fixedCost_data, totCost_data1, opCost_data1, fixedCost_data1)