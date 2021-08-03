import pandas as pd
import numpy as np

df = pd.read_csv("Forex-Data/USD_TRY.csv")
ix = np.where(df["Date"] == "Feb 03, 2021")
print(ix[0][0])


print(df.head())