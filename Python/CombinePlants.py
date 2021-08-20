#Michael Craig
#Combine all wind and solar units in fleet together (separately for
#each plant type), then remove all but combined unit from fleet. 

#Inputs: gen fleet (2d list)
def combineWindSolarStoPlants(genFleet):
    genFleet = combinePlants(genFleet,'FuelType','Wind')
    genFleet = combinePlants(genFleet,'FuelType','Solar')
    print('**NOTE: Combining storage facilities in CombinePlants.py')
    genFleet = combinePlants(genFleet,'PlantType','Battery Storage',True)
    genFleet = combinePlants(genFleet,'PlantType','Hydrogen',True)
    return genFleet

#Adds new combined unit, then removes other units
#Inputs: gen fleet (2d list), fuel type to combine, plant type to combine
def combinePlants(fleet,paramCombinedOn,fuelType,storage=False):
    gens = fleet.loc[fleet[paramCombinedOn]==fuelType]
    if gens.shape[0] > 0:
        newRow = gens.iloc[-1].copy()
        newRow['Capacity (MW)'] = gens['Capacity (MW)'].sum()
        newRow['RampRate(MW/hr)'] = gens['RampRate(MW/hr)'].sum()
        if storage:
            newRow['Maximum Charge Rate (MW)'] = gens['Maximum Charge Rate (MW)'].sum()
            newRow['Nameplate Energy Capacity (MWh)'] = gens['Nameplate Energy Capacity (MWh)'].sum()
        newRow['Unit ID'] += 'COMBINED'
        fleet = fleet.drop(index=gens.index)
        fleet = fleet.append(newRow)
    return fleet
