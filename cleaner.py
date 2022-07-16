import csv 
import pandas as pd
missing_val = ["?"]
df = pd.read_csv("main.csv" , na_values=missing_val)
print(df.shape)
df.drop(["Unnamed: 0","Star_Name", "Star_Mass", "Star_Radius" , "Distance" , "Star_luminosity"] , axis=1 , inplace=True)
final = df.dropna()
final.reset_index(drop=True,inplace = True)
print(final)
print(final.info())
print(df.dtypes)
final.to_csv("final.csv" , index=False)