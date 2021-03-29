import pandas as pd
df_new=pd.read_excel("CatalogEntries-Vita.xlsx")
df_new.to_csv("CatalogEntries-Vita1.csv",encoding='utf-8',index=False)
