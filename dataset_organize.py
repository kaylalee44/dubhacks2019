import pandas as pd
import numpy as np

data_2016 = pd.read_csv("./Airbnb Datasets/listings-2016.csv")
data_2019 = pd.read_csv("./Airbnb Datasets/listings-2019.csv")

df_2016 = pd.DataFrame(data_2016)
df_2019 = pd.DataFrame(data_2019)

df_2016["year_found"] = 2016
df_2019["year_found"] = 2019

# df_2016.join(df_2019, on="id", how="left")

# print(df_2016.head(1)) #sanity check
for col_2016 in df_2016.columns:
    if col_2016 not in df_2019.columns:
        df_2016 = df_2016.drop(columns=col_2016)

for col_2019 in df_2019.columns:
    if col_2019 not in df_2016.columns:
        df_2019 = df_2019.drop(columns=col_2019)

print(len(df_2016.columns))
print(len(df_2019.columns))

data_2016 = pd.read_csv("./Airbnb Datasets/airbnb-2016-data-organized.csv")
data_2019 = pd.read_csv("./Airbnb Datasets/airbnb-2019-data-organized.csv")

new_df = data_2016.append(data_2019)
new_df.drop_duplicates(subset="id")
new_df.to_csv("combined_data.csv", index=False)
