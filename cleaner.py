import csv 
import pandas as pd
df = pd.read_csv("main.csv")
print(df.shape)
df.drop(["Unnamed: 0","Star_Name", "Star_Mass", "Star_Radius" , "Distance" , "Star_luminosity"] , axis=1 , inplace=True)
final = df.dropna()
final.reset_index(drop=True,inplace = True)
print(final)
print(final.info())
final.to_csv("final.csv" , index=False)