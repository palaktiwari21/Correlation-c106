import csv
import plotly.express as px
import numpy as np
import pandas as pd
def getDataSource(data_path):
    coffee=[]
    sleep_hours=[]
    with open (data_path) as csv_file:
     csv_reader=csv.DictReader(csv_file)
     for row in csv_reader:
         coffee.append(float(row['Marks In Percentage']))
         sleep_hours.append(float(row['Days Present']))
    return{'x':coffee,'y':sleep_hours}
def findCorelation(dataSource):
    correlation=np.corrcoef(dataSource['x'] ,dataSource['y'])
    print('Correlation between Marks and Days present is :- ',correlation[0,1])
def setup():
    data_path='Student Marks vs Days Present.csv'
    datasource=getDataSource(data_path)
    findCorelation(datasource)
setup()
