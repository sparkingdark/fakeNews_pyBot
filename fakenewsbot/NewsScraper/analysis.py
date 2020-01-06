import json
import pandas as pd 
import keras
import csv

import numpy as np 

with open('/home/debo/Desktop/fakenewsbot/NewsScraper/scraped_articles.json') as p:
    df=json.load(p)
    
df=pd.DataFrame(df)

#print(df.head())

df2=pd.DataFrame(df.newspapers.iloc[0])
df3=pd.DataFrame(df.newspapers.iloc[1])
df2.drop('link',inplace=True,axis=1)
df3.drop('link',inplace=True,axis=1)
df4=pd.DataFrame(df.newspapers.iloc[2])
df5=pd.DataFrame(df.newspapers.iloc[3])
df6=pd.DataFrame(df.newspapers.iloc[4])

frames=[df2,df3,df4,df5,df6]

final_df=pd.concat(frames)

with open('/home/debo/Desktop/fakenewsbot/NewsScraper/dataset/all.csv','w+') as f:
    mydict=final_df.articles  
    w = csv.DictWriter(f,fieldnames=['text','title','link','published'])
    w.writeheader()
    w.writerows(mydict)
