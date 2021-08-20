#Michael Craig

from AuxFuncs import *
from GAMSAuxFuncs import *
import copy, csv, pandas as pd,os,numpy as np

def saveCapacExpOperationalData(ceModel,genFleetForCE,newTechsCE,hoursForCE,resultsDir,
                                modelName,year):
    hoursForCESymbols = [createHourSymbol(hr) for hr in hoursForCE]
    saveGeneratorResults(ceModel,genFleetForCE,hoursForCESymbols,resultsDir,modelName,year)
    saveGeneratorResults(ceModel,newTechsCE,hoursForCESymbols,resultsDir,modelName,year,True)
    sysResults = saveSystemResults(ceModel,hoursForCESymbols)
    sysResults.to_csv(os.path.join(resultsDir,'sysResults' + modelName + str(year) + '.csv'))
    for n in ['vCO2emsannual','vZannual', 'vVarcostannual']:
        result = extract0dVarResultsFromGAMSModel(ceModel,n)
        write2dListToCSV([[result]],os.path.join(resultsDir,n + modelName + str(year) + '.csv'))
    return result

def saveGeneratorResults(ceModel,gens,hoursForCE,resultsDir,modelName,year,newTechs=False):
    for v in ['vGen','vRegup','vFlex','vCont','vTurnon','vTurnoff','vOnoroff','vCharge','vStateofcharge']:
        df = pd.DataFrame(index=gens['GAMS Symbol'],columns=hoursForCE)
        v += 'tech' if newTechs else ''
        if v in [i.name for i in ceModel.out_db]:
            for rec in ceModel.out_db[v]: df.loc[rec.key(0),rec.key(1)] = rec.level
        df.to_csv(os.path.join(resultsDir,v + modelName + str(year) + '.csv'))
        resultsCEgen = df
        return resultsCEgen
    
def saveSystemResults(ceModel,hoursForCE):
    resultLabelToEqnName = {'mcGen':'meetdemand','mcRegup':'meetregupreserve',
        'mcFlex':'meetflexreserve','mcCont':'meetcontreserve','flex':'vFlexreserve',
        'regup':'vRegupreserve'}
    sysResults = pd.DataFrame(index=[k for k in resultLabelToEqnName],columns=hoursForCE)
    for result,varName in resultLabelToEqnName.items():
        if varName in [i.name for i in ceModel.out_db]:
            for rec in ceModel.out_db[varName]:
                value = rec.marginal if 'mc' in result else rec.level
                sysResults.loc[result,rec.key(0)] = value
    return sysResults