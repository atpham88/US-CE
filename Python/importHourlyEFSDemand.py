# An Pham
# July 6, 2021
# Import hourly EFS demand data from CSVs, return in 1d list w/out header

import os
import pandas as pd

def importHourlyEFSDemand(currYear):
    # Set filename and directory
    filename = 'EFS_Load' + '.csv'
    demandDir = os.path.join('Data', 'ERCOTDemand')
    # Read into pd
    rawDemand = pd.read_csv(os.path.join(demandDir, filename), delimiter=',', index_col='hour')
    if currYear == 2020:
        demand = rawDemand['EFS2020']
    elif currYear == 2030:
        demand = rawDemand['EFS2030']
    elif currYear == 2040:
        demand = rawDemand['EFS2040']
    elif currYear == 2050:
        demand = rawDemand['EFS2050']
    demand = demand.values.tolist()
    hourlyDemand = demand
    return hourlyDemand
