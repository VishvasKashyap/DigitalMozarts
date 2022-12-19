import pandas as pd
data=pd.read_csv(r"data.csv")
dt=data[['ad_id','campaign_id','reporting_start','age']]
dt["Datetime"]=pd.to_datetime(dt["reporting_start"])
dt["reporting_start"].between('17-08-2017','22-08-2017')
dt["age"].between('30','34')
print(dt)
