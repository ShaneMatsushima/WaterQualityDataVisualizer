# Parsing functions used for grabbing data from csv
# Created by: Shane Matsushima
# Date: 10/23/2020

#import to libraries used
import pandas as pd 
import numpy as np
from datetime import datetime
import csv
import matplotlib.pyplot as plt

def graph_value_over_time(filepath, element):
    df = pd.read_csv(filepath, delimiter=',', low_memory=False)
    sr = pd.Series(df['CharacteristicName'])
    df = pd.DataFrame(df)

    date = pd.to_datetime(df.loc[df['CharacteristicName'] == element, 'ActivityStartDate'])
    value = df.loc[df['CharacteristicName'] == element, 'ResultMeasureValue']

    combined = np.vstack((date, value)).T 
    feild = ['date', 'time']

    with open('.\\csv\\tempTime.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(feild)
        for i in combined:
            csvwriter.writerow(i)
    
    df2 = pd.read_csv('.\\csv\\tempTime.csv', delimiter=',', low_memory=False)
    df2['date'] = pd.to_datetime(df['date'])
    df2.sort_values(by='date')

    date = df2['date']
    value = df2['value']

    pd.plotting.register_matplotlib_converters()
    plt.xlabel('Date YYYY/MM/DD')
    plt.ylabel('Units')
    plt.title(element)
    plt.plot_date(date, value)
    plt.show()


    



