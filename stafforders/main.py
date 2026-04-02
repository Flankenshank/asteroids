import pandas as pd

df = pd.read_excel("Pricelist.xlsx", sheet_name="Sheet1")
print(df.head())