'''
Created on Dec 5, 2016

@author: twff
'''
import pandas as pd
import collections as col
import numpy as np
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import matplotlib.pyplot as plt
from plottools import *

if __name__=='__main__':
    collision_data = pd.read_csv('/Users/twff/Downloads/clean_data.csv').dropna()
    collision_data['date'] = collision_data['DATE'].map(lambda x:turn_date_to_int(x))
    month = col.Counter(collision_data['date'])# count the number of collision of each month
    months = pd.DataFrame.from_dict(month, orient='index')
    months = months.sort()
    plot_month_pltt(months)
    
    collision_data['days'] = collision_data['DATE'].map(lambda x:turn_day_to_int(x)) 
    day = col.Counter(collision_data['days'])
    days = pd.DataFrame.from_dict(day, orient='index')
    days = days.sort()
    days = days.rename({0:'count'})
    plot_days_pltt(days)
    
    



