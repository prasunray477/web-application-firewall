               # ************************************joining datasets*********************************************

import pandas as pd

df_good = pd.read_csv('/content/good_reqs.csv')
df_bad = pd.read_csv('/content/bad_reqs.csv')

display(df_good.head())
display(df_bad.head())

df_joined = pd.concat([df_good, df_bad], ignore_index=True)
display(df_joined.head())
display(df_joined.shape)

df_joined.to_csv('combined_data.csv', index=False)

