import csv 
import pandas as pd
df = pd.read_csv("main.csv")
print(df.shape)
del df["Star_luminosity"]
df = df[df["Distance_1"].notna()]
df = df[df["Star_Mass_1"].notna()]
df = df[df["Star_Radius_1"].notna()]
df = df[df["Star_Name"].notna()]
df = df[df["Star_Mass"].notna()]
df = df[df["Star_Radius"].notna()]
df = df[df["Distance"].notna()]
print(df.shape)
df.to_csv("final.csv" , index=False)