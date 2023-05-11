from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
# import requests
import json
# jsonapidata=requests.request('GET',"https://api.github.com/users/hadley/orgs")
# jsondata=jsonapidata.json()
# print(len(jsondata))
spark = SparkSession.builder.appName('REST').getOrCreate()
# file=open("C:/Users/Raj_Kumar/PycharmProjects/pycharm_Epam/REST_API-DF/file","a")
# for record in jsondata:
#     file.write("%s\n" %record)

df_json = spark.read.format("json").load("C:/Users/Raj_Kumar/PycharmProjects/pycharm_Epam/REST_API-DF/file")
df_json.count()
df_json.show()
