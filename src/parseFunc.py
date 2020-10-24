# Parsing functions used for grabbing data from csv
# Created by: Shane Matsushima
# Date: 10/23/2020

#import to libraries used
import pandas as pd 
import numpy as np
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Graphs data based on the time it was taken (Needs to be redone without temp csv file)
def graph_value_over_time(filepath, element):
    df = pd.read_csv(filepath, delimiter=',', low_memory=False)
    sr = pd.Series(df['CharacteristicName'])
    df = pd.DataFrame(df)

    date = df.loc[df['CharacteristicName'] == element, 'ActivityStartDate']
    value = df.loc[df['CharacteristicName'] == element, 'ResultMeasureValue']

    combined = np.vstack((date, value)).T 
    feild = ['date', 'value']

    with open('.\\src\\csv\\tempTime.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(feild)
        for i in combined:
            csvwriter.writerow(i)
    
    
    df2 = pd.read_csv('.\\src\\csv\\tempTime.csv', delimiter=',', low_memory=False)
    df2['date'] = pd.to_datetime(df2['date'])
    df2 = df2.sort_values(by='date')

    date = df2['date']
    value = df2['value']

    pd.plotting.register_matplotlib_converters()
    plt.xlabel('Date YYYY/MM/DD')
    plt.ylabel('Units')
    plt.title(element)
    plt.plot_date(date, value)
    plt.show()

# Graphs data using a boxplot w/ average indicator 
def box_plot(filepath, element, unit):
    df = pd.read_csv(filepath, delimiter=',', low_memory=False)
    dr = pd.Series(df['CharacteristicName'])
    df = pd.DataFrame(df)

    valueElement = df.loc[((df['CharacteristicName'] == element) & (df['MeasureUnitCode'] == unit)), 'ResultMeasureValue']

    valueElement = np.array(valueElement, dtype=np.float64)

    boxPlotData = [valueElement]

    fig = plt.figure(1, figsize=(9,6))

    ax = fig.add_subplot(111)

    bp = ax.boxplot(boxPlotData, showmeans=True, meanline=True, patch_artist=True, labels=[element], autorange=True)

    plt.ylabel(unit)
    plt.show()



    



