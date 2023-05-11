from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
import requests
import pandas as pd
df=pd.DataFrame()
import json
jsonApiData=requests.request('GET',"https://restcountries.com/v2/all")
jsonData = jsonApiData.json()
spark = SparkSession.builder.appName('REST').getOrCreate()
big_data =pd.DataFrame({'Country':[],'CallingCodes':[],'Region':[],'Population':[],'Timezones':[],'numericCode':[]})
for record in jsonData:
    dict_new = dict()
    dict_new['Country'] = record['name']
    dict_new['CallingCodes'] = record['callingCodes']
    # dict_new['Capital'] = record['capital']
    # print(record['capital'])
    dict_new['Region'] = record['region']
    dict_new['Population'] = record['population']
    dict_new['Timezones'] = record['timezones']
    dict_new['numericCode'] = record['numericCode']
    # for k in record['currencies']:
    #     dict_new['currency_Sym'] = k['symbol']
    df1 = pd.DataFrame(dict_new)
    big_data = pd.concat(big_data,df1)
print(big_data)






