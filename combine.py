import pandas as pd
data={"Name" :["sneha","vedika","shravani","diksha"],
      "age":[12,54,21,78],
      "salary":[45000,78000,12000,9000]
      }
df=pd.DataFrame(data)
print(df)
df.to_csv("created.csv")
