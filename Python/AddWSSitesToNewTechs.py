import pandas as pd

def addWSSitesToNewTechs(newCfs,df):
    for l,f in zip(['wind','solar'],['Wind','Solar']):
        re = df.loc[df['FuelType']==f]
        sites = [c for c in newCfs if l in c]
        sitesDf = pd.concat([re]*len(sites),ignore_index=True)
        sitesDf['PlantType'] = sites
        #Get lat/lon
        txt = sitesDf['PlantType'].str.split('lat',expand=True)[1]
        sitesDf[['Latitude','Longitude']] = txt.str.split('lon',expand=True).astype(float)
        df = pd.concat([df,sitesDf],ignore_index=True)
        df.drop(re.index,inplace=True)
        df.reset_index(inplace=True,drop=True)
    df['GAMS Symbol'] = df['PlantType']
    return df