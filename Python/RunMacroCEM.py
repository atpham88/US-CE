#Shell script for running macro CEM
#Order of inputs: interconn, co2cap

import sys,os
from MacroCEM import macroCEM

#Set working directory to location of this script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Process inputs and call master function
inputData = sys.argv[1:] #exclude 1st item (script name)
interconn = inputData[0]
co2Cap = int(inputData[1])

macroCEM(interconn,co2Cap)