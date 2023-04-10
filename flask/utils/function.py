import pandas as pd

df1 = pd.read_csv('fertilizers.csv')
df2 = pd.read_csv('codes_iso.csv')

df_merge = pd.merge(df1,df2, on="Entity")
df_merge = df_merge.to_csv("fertilizers_regions.csv",index=False)

