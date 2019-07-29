from pandas import Series, DataFrame
import pandas as pd

df = pd.read_csv('NYC_Restaurants.csv', dtype=unicode)
df['RESTAURANT'] = df['DBA']+df['BUILDING']+df['STREET']+df['ZIPCODE']+df['BORO']
print df.iloc[0:10]

