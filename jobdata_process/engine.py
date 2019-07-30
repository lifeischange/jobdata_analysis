# encoding:utf-8

from pandas import DataFrame,Series
import pandas.io.sql as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from fetchdata.fetchdata import fetchdata as f

def generate():

    fetch_data="select * from jobdata"

    data=f()
    jobs=data.fetchdata(fetch_data)
    datas=sql.read_sql(fetch_data,data.conn)
    data.close()
    return datas

def filters(dataframe):
    #strip unless address ,just remained the city name 
    temp=dataframe['address'].map(lambda x : x.split()[0])
    dataframe["address"]=temp
    #translate salary from string to int,devide into two columns,one is the buttom and the other is the top
    buttom=dataframe['salary'].map(lambda x : x.split('-')[0])
    top=dataframe['salary'].map(lambda x : x.split('-')[1].split('K')[0])
    dataframe['buttom']=buttom.map(lambda x: float(x))
    dataframe['top']=top.map(lambda x:process_type(x))
    return dataframe

#process the data can't convert to int
def process_type(x):
    try:
        return float(x)
    #suspect the salary is 100/day
    except:
        return 3



def separate(dataframe):
    dataframe['mean']=(dataframe['buttom']+dataframe['top'])/2
    city_salary=dataframe.loc['address','mean'].groupby("address")
    temp=city_salary
    print(temp)
    return dataframe.groupby('address').mean().iloc[0:5]
    #return city_salary
    




if __name__=="__main__":
    raw_data=generate()
    
    data_object=filters(raw_data)
    separate(data_object).boxplot(column='mean',by='address')
    plt.show()
    
    #print(raw_data[:5])
