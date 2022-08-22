import pandas as pd
import numpy as np
import geopandas as gpd
from netCDF4 import Dataset

def resite_figures(shapefile_dir):
    solarFile, windFile = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\solar_cf_2012.csv", \
                          "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\wind_cf_2012.csv"

    # Load data
    solarPowGen = pd.read_csv(solarFile)
    windPowGen = pd.read_csv(windFile)              # assume solar and wind cover same geographic region

    # Get lat and lons for both datasets
    lats_temp, lons_temp = solarPowGen['lat'], solarPowGen['lon']
    latsPd = pd.DataFrame(lats_temp, columns=['lat'])
    latsPd = latsPd.drop_duplicates()
    latsPd = latsPd.sort_values(by=['lat'])
    latsPd = latsPd.reset_index()
    lats = latsPd['lat'].to_numpy()
    lats_temp = lats_temp.to_numpy()

    lonsPd = pd.DataFrame(lons_temp, columns=['lon'])
    lonsPd = lonsPd.drop_duplicates()
    lonsPd = lonsPd.sort_values(by=['lon'])
    lonsPd = lonsPd.reset_index()
    lons = lonsPd['lon'].to_numpy()
    lons_temp = lons_temp.to_numpy()

    latsAll = pd.Series(latsPd['lat'])
    lonsAll = pd.Series(lonsPd['lon'])

    latlonList = [(i, j)
                  for i in latsPd.lat
                  for j in lonsPd.lon]

    latlonPd = pd.DataFrame(data=latlonList, columns=['lat', 'lon'])
    latlonGpd = gpd.GeoDataFrame(latlonPd, geometry=gpd.points_from_xy(latlonPd.lon, latlonPd.lat))
    latlonGpd = latlonGpd.set_crs(epsg=4326, inplace=True)

    cf_solar = solarPowGen.iloc[:,2:]
    cf_wind = windPowGen.iloc[:,2:]
    cf_solar = cf_solar.to_numpy()
    cf_wind = cf_wind.to_numpy()

    cf_solar = pd.DataFrame(np.mean(cf_solar, axis=1))
    cf_wind = pd.DataFrame(np.mean(cf_wind, axis=1))
    cf_solar, cf_wind = cf_solar.stack(), cf_wind.stack()
    cf_solar, cf_wind = cf_solar.reset_index(), cf_wind.reset_index()

    wind_cf = pd.DataFrame(data=lats_temp, columns=['lat'])
    wind_cf['lon'] = lons_temp
    solar_cf = pd.DataFrame(data=lats_temp, columns=['lat'])
    solar_cf['lon'] = lons_temp

    wind_cf['wind_cf'] = cf_wind.iloc[:,2]
    solar_cf['solar_cf'] = cf_solar.iloc[:,2]

    transRegions = dict()
    transRegions['SERC'] = list(range(87, 99)) + list(range(101, 103))
    transRegions['NYISO'] = [127, 128]
    transRegions['ISONE'] = list(range(129, 135))
    transRegions['MISO'] = [37] + list(range(42, 47)) + list(range(68, 87)) + [56, 58, 66] + list(range(103, 109))
    transRegions['PJM'] = list(range(109, 127)) + [99, 100]
    transRegions['SPP'] = [35, 36] + list(range(38, 42)) + list(range(47, 56)) + [57]
    transRegions['ERCOT'] = list(range(60, 66)) + [67]

    for r, p in transRegions.items():
        transRegions[r] = ['p' + str(i) for i in p]

    pRegionShapes = gpd.read_file(shapefile_dir + 'PCAs.shp')
    allPRegions = list()
    for r, pRegions in transRegions.items(): allPRegions += pRegions
    pRegions = allPRegions
    pRegionShapes = pRegionShapes.loc[pRegionShapes['PCA_Code'].isin(pRegions)]
    transRegionsReversed = dict()
    for zone, pRegions in transRegions.items():
        for p in pRegions:
            transRegionsReversed[p] = zone
    pRegionShapes['region'] = pRegionShapes['PCA_Code'].map(transRegionsReversed)
    loadregions = pRegionShapes.dissolve(by='region')
    loadregions = loadregions.reset_index()
    loadregions = loadregions.drop(['PCA_Code', 'PCA_REG', 'RTO_Code'], axis=1)


    return (wind_cf, solar_cf, pRegionShapes, loadregions)
