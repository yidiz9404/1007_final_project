'''
Created on Dec 5, 2016

@author: twff
'''
import matplotlib.pyplot as plt
from datetime import datetime
import collections as col
import pandas as pd

def turn_date_to_int(x):
    if type(x)==str:
        x = x[-4:-1]+x[-1]+x[0:2]
    return x

def plot_month_pltt(df):
    fig = plt.figure(color='skyblue')
    df.plot()
    plt.title("Monthly Number of Car Collision")
    plt.ylabel("Counts")
    plt.xlabel('Months')
    plt.grid(True)
    plt.show()
    fig.savefig('graphs/Monthly Number of Car Collision.pdf')
    plt.close()
    

def turn_day_to_int(x):
    '''
    plot collision linplot of days
    '''
    if type(x)==str:
        x = x[-4:-1]+x[-1]+x[0:2]+x[3:5]
    return x

def plot_days_pltt(df):
    fig = plt.figure()
    df.plot(color='skyblue')
    plt.title("Number of Car Collision in whole year")
    plt.ylabel("Counts")
    plt.xlabel('Days')
    plt.grid(True)
    plt.show()
    fig.savefig('graphs/Number of Car Collision in whole year.pdf')
    plt.close()
    
def plot_daily_pltt(date, df):
    picked = df.loc[df[date] == date]
    picked['clock'] = picked['TIME'].map(lambda x: datetime.strptime(x, '%H:%M'))
    time = col.Counter(picked['clock'])
    time = pd.DataFrame.from_dict(time, orient='index')
    time = time.sort()
    
    
    fig = plt.figure()
    time.plot(color='skyblue')
    plt.title("Daily Number of Car Collision")
    plt.ylabel("Counts")
    plt.xlabel('Days')
    plt.grid(True)
    plt.show()
    fig.savefig('graphs/Daily Number of Car Collision '+ str(date) +'.pdf')
    plt.close()
    

    
    
    
    
    