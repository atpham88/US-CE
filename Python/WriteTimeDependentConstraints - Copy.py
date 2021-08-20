#Michael Craig
#April 24, 2020
#Write .gms file w/ CE text for time blocks and associated constraints

import os
from GAMSAddSetToDatabaseFuncs import createHourSubsetName

def writeTimeDependentConstraints(blockNamesChronoList,stoInCE,seasSto,gamsFileDir,ceOps):
   setText,setDefns = writeSets(blockNamesChronoList,stoInCE)
   paramText,paramDefns = writeParameters(blockNamesChronoList,stoInCE,seasSto,ceOps)
   importText = writeImport(blockNamesChronoList,stoInCE,seasSto,ceOps) 
   varText = writeVariables(blockNamesChronoList) if (seasSto and len(blockNamesChronoList) > 1) else ''
   eqnText = writeEquationsNames(blockNamesChronoList,stoInCE,seasSto,ceOps)
   eqnText += writeEquations(blockNamesChronoList,stoInCE,seasSto,ceOps)
   allText = setText + paramText + importText + paramDefns + setDefns + varText + eqnText
   g = open(os.path.join(gamsFileDir,'CETimeDependentConstraints.gms'),'w')
   g.write(allText)
   g.close()

def writeSets(blockNamesChronoList,stoInCE):
   setText,setDefns = 'Sets\n','\n'
   #Create names for set blocks
   for nB in blockNamesChronoList: setText += '\t' + createHourSubsetName(nB) + '(h)\n'
   #Set which hours are not initial hours
   if stoInCE:
      nonInit = 'nonInitH(h)'
      setDefns += nonInit + '= yes;\n'
      for nB in blockNamesChronoList:
         setDefns += nonInit + '$[ord(h)=' + createInitHourName(nB) + '] = no;\n'
   return setText + '\t;\n',setDefns

def writeParameters(blockNamesChronoList,stoInCE,seasSto,ceOps):
   paramText,paramDefns = 'Parameters\n','\n'
   #Weights to scale up costs and emissions
   for nB in blockNamesChronoList: paramText += '\tpWeight' + createHourSubsetName(nB) + '\n'
   #Init SOC and init hours
   if stoInCE:
      for nB in blockNamesChronoList: 
         nBInitHour = createInitHourName(nB)
         paramText += '\t' + nBInitHour + '\n'
         if seasSto:
            paramText += '\tpSOCScalar{0}\n'.format(createHourSubsetName(nB)) if nB != blockNamesChronoList[0] else '' #no SOC scalar for first block
         for et in ['storageegu','storagetech']:
            if not seasSto: 
               paramText += createNameWithSets(createInitSOCName(nB),et) + '\n'
            elif seasSto and nB == blockNamesChronoList[0]:
               paramText += createNameWithSets(createInitSOCName(nB),et) + '\n'
         paramDefns += nBInitHour + ' = smin(h$' + createHourSubsetName(nB) + '(h),ord(h));\n'
         if ceOps == 'UC': paramText += 'pOnoroffinit' + createHourSubsetName(nB) + '(egu)\n'
   return '\n' + paramText + '\t;\n',paramDefns

def createInitSOCName(nB):
   return 'pInitSOC' + createHourSubsetName(nB)

def createInitHourName(nB):
   return 'pHourInit' + createHourSubsetName(nB)# + createSetsText(['h'])

def writeImport(blockNamesChronoList,stoInCE,seasSto,ceOps):
   importText = """\n$if not set gdxincname $abort 'no include file name for data file provided'\n"""
   importText += '$gdxin %gdxincname%\n'
   blocks = ','.join([createHourSubsetName(nB) for nB in blockNamesChronoList])
   weights = ','.join(['pWeight' + createHourSubsetName(nB) for nB in blockNamesChronoList])
   if stoInCE:
      if seasSto:
         scalars = ','.join(['pSOCScalar' + createHourSubsetName(nB) for nB in blockNamesChronoList[1:]]) #no SOC scalar for first block
      ets,initSOCs = ['storageegu','storagetech'],''
      for nB in blockNamesChronoList:
         if seasSto and nB == blockNamesChronoList[0]:
            initSOCs += ','.join([createInitSOCName(nB) + techLbl(et) for et in ets]) + ','
         elif not seasSto:
            initSOCs += ','.join([createInitSOCName(nB) + techLbl(et) for et in ets]) + ','
   if ceOps == 'UC': onOffInits = ','.join(['pOnoroffinit' + createHourSubsetName(nB) for nB in blockNamesChronoList])
   #Combine all text
   if stoInCE and seasSto: allText = [blocks,weights,scalars,initSOCs.rstrip(',')]
   elif stoInCE: allText = [blocks,weights,initSOCs.rstrip(',')]
   else: allText = [blocks,weights]
   if ceOps == 'UC': allText += [onOffInits]
   importText += '\n'.join(['$load ' + l for l in allText])
   return importText + '\n$gdxin\n'

def writeVariables(blockNamesChronoList):
   varText = '\nVariables\n'
   v = 'vInitSOC'
   for et in ['storageegu','storagetech']: 
      for nB in blockNamesChronoList[1:]:
         varText += ('\t' + v + createHourSubsetName(nB) + techLbl(et) + '(' + et + ')' + '\n')
   return varText + '\t;\n'

def writeEquationsNames(blockNamesChronoList,stoInCE,seasSto,ceOps):
   eqnText = '\nEquations\n'
   gens,stos = ['egu','tech'],['storageegu','storagetech']
   for eqn in ['varCost','co2Ems']: eqnText += '\t' + eqn + '\n'
   if stoInCE:
      for et in stos:
         for eqn in ['defSOC','genPlusUpResToSOC']:
            eqnText += createNameWithSets(eqn,et,'h') + '\n'
         if seasSto:
            for nB in blockNamesChronoList[1:]:
               eqnText += createNameWithSets('setInitSOC'+createHourSubsetName(nB),et,'h') + '\n'
   for g in gens:
      for nB in blockNamesChronoList:
         eqnText += createNameWithSets('rampUp'+createHourSubsetName(nB),g,createHourSubsetName(nB)) + '\n'
         if ceOps == 'UC': eqnText += createNameWithSets('commitment'+createHourSubsetName(nB),g,createHourSubsetName(nB)) + '\n'
   return eqnText + '\t;\n'

def createNameWithSets(eqn,*argv):
   setsText = createSetsText(argv)
   return '\t' + eqn + techLbl(setsText) + setsText

def createSetsText(args):
   setsText = '(' 
   for arg in args: setsText += arg + ',' 
   return setsText.rstrip(',') + ')'

def techLbl(et):
   return 'tech' if 'tech' in et else ''

def getGenPlusReserves(et,setsText):
   return 'vGen{0}{1}+vRegup{0}{1}+vFlex{0}{1}+vCont{0}{1}'.format(techLbl(et),setsText)

def getGenAboveMinPlusReserves(et,setsText):
   return 'vGenabovemin{0}{1}+vRegup{0}{1}+vFlex{0}{1}+vCont{0}{1}'.format(techLbl(et),setsText)   

def writeEquations(blockNamesChronoList,stoInCE,seasSto,ceOps):
   eqns = ''
   #Storage equations
   if stoInCE:
      for et in ['storageegu','storagetech']:
         eqns += '\n'
         setsText = createSetsText([et,'h'])
         socDefnSharedText = '''vStateofcharge{0}({1}, h-1)$nonInitH(h) - 
               1/sqrt(pEfficiency{0}({1})) * vGen{0}({1},h) + 
               sqrt(pEfficiency{0}({1})) * vCharge{0}({1},h)'''.format(techLbl(et),et)
         genSOCSharedText = getGenPlusReserves(et,setsText)
         if seasSto:
            initsText = ''
            for nB in blockNamesChronoList:
               if nB == blockNamesChronoList[0]: socName = 'pInitSOC'
               else: socName = ' + vInitSOC'
               socName += createHourSubsetName(nB)
               initsText += '{0}{1}({2})$[ord(h)={3}]'.format(socName,techLbl(et),et,createInitHourName(nB))
               if 'tech' in et and 'pInit' in socName: initsText += '*vN({t})'.format(t=et) #multiply by # built if pInit (otherwise RHS > 0)
         else:
            initsText = ''
            for nB in blockNamesChronoList:
               initsText += ' + pInitSOC{b}{t}({e})$[ord(h)={i}]'.format(b=createHourSubsetName(nB),t=techLbl(et),e=et,i=createInitHourName(nB))
               if 'tech' in et: initsText += '*vN({t})'.format(t=et) #multiply by # built if pInit (otherwise RHS > 0)
            initsText = initsText.lstrip(' + ')
         #defSOC
         eqns += 'defSOC{0}{1}.. vStateofcharge{0}{1} =e= {2} +\n\t{3};\n'.format(techLbl(et),setsText,initsText,socDefnSharedText)
         #genPlusUpResToSOC
         eqns += '''genPlusUpResToSOC{0}{1}.. {2} =l= vStateofcharge{0}({3}, h-1)$nonInitH(h)
                     + {4};\n'''.format(techLbl(et),setsText,genSOCSharedText,et,initsText) 
         #set initial SOC for short-term (st) storage
         # for nB in blockNamesChronoList[1:]:
         #    eqns += 'pInitSOC{b}{t}({e}) = {isf}*pMaxsoc{t}({e});\n'.format(b=createHourSubsetName(nB),
         #                                                 t=techLbl(et),e='st'+et,isf=str(initSOCFraction))
         #set initial SOC for long-term (lt) storage
         if seasSto:
            for bNum in range(1,len(blockNamesChronoList)):
               nB,nBLast = blockNamesChronoList[bNum],blockNamesChronoList[bNum-1]
               initSOCLastBlock = 'pInitSOC' if nB == blockNamesChronoList[1] else 'vInitSOC'
               initsText = initSOCLastBlock + '{b}{t}({s})'.format(b=createHourSubsetName(nBLast),t=techLbl(et),s='lt'+et)
               if 'tech' in et and 'pInit' in initSOCLastBlock: initsText += '*vN({s})'.format(s='lt'+et) #multiply by # built if pInit (otherwise RHS > 0)
               eqns += '''setInitSOC{0}{1}({2},h)$[ord(h)={3}].. vInitSOC{0}{1}({2}) =l=  vStateofcharge{1}({2},h-1) + (vStateofcharge{1}({2},h-1)
                        -{4}) * pSOCScalar{0};\n'''.format(createHourSubsetName(nB),techLbl(et),
                           'lt'+et,createInitHourName(nB),initsText)
   #Emission and cost equations
   eqns += '\n'
   eguSets = ['egu','tech']
   for v,eqn in zip(['vVarcost','vCO2ems'],['varCost','co2Ems']):
      blockText = ''
      for nB in blockNamesChronoList:
         blockText += ('\n\t+ ' if nB != blockNamesChronoList[0] else '') + 'pWeight' + createHourSubsetName(nB) + '*('
         for et in eguSets:
            setsText = createSetsText([et,createHourSubsetName(nB)])
            if v == 'vVarcost' and ceOps == 'UC': #add in turn on cost
               startCost = '+pStartupfixedcost{t}({e})*vTurnon{t}{s}'.format(t=techLbl(et),e=et,s=setsText)
            else:
               startCost = ''
            blockText += 'sum({s},{v}{t}{s}{sc}){p}'.format(s=setsText,v=v,t=techLbl(et),p='+' if et != eguSets[-1] else '',sc=startCost)
         blockText += '))' #close pWeight parens
         blockText = blockText[:-1] #drop trailing +
      eqns += '{0}.. {1}annual =e= {2};\n'.format(eqn,v,blockText)
   #Ramp ups
   eqns += '\n'
   for nB in blockNamesChronoList:
      for et in eguSets:
         setsText = createSetsText([et,createHourSubsetName(nB)])
         rhs = 'pRamprate{t}({e})'.format(t=techLbl(et),e=et)
         if ceOps == 'ED': 
            genPlusRes = getGenPlusReserves(et,setsText)
            genName = 'vGen'
            if et == 'tech': rhs += '*vN({e})'.format(e=et)
         else: 
            genPlusRes = getGenAboveMinPlusReserves(et,setsText)
            genName = 'vGenabovemin'
            if et == 'tech': rhs += '*vOnorofftech({e},{b}-1) + vTurnontech{s}*pCapactech({e})'.format(e=et,b=createHourSubsetName(nB),
                                                                                                      s=setsText)
         eqns += '''rampUp{b}{t}{s}$[ORD({b})>1].. {gr} - {g}{t}({e},{b}-1) =l= 
                  {r};\n'''.format(b=createHourSubsetName(nB),t=techLbl(et),
                  s=setsText,gr=genPlusRes,e=et,r=rhs,g=genName)
   #Commitments
   if ceOps == 'UC':
      eqns += '\n'
      for nB in blockNamesChronoList:
         for et in eguSets:
            setsText = createSetsText([et,createHourSubsetName(nB)])
            excludeHour1 = '$[ORD({b})>1]'.format(b=createHourSubsetName(nB)) if et == 'tech' else ''
            initOnOff = 'pOnoroffinit{b}({et})$[ORD({b})=1] +'.format(b=createHourSubsetName(nB),et=et) if et == 'egu' else ''
            eqns += '''commitment{b}{t}{s}{c} .. vOnoroff{t}{s} =e= {i} vOnoroff{t}({e},{b}-1)
                        + vTurnon{t}{s} - vTurnoff{t}{s};\n'''.format(t=techLbl(et),s=setsText,c=excludeHour1,i=initOnOff,
                        e=et,b=createHourSubsetName(nB))
   return eqns

