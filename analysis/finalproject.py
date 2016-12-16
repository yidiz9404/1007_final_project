'''
Created on Dec 15, 2016

@author: twff
'''
from Date import *
import sys
import pandas as pd
from overallplot import *
from geomap import *
from correlation import *

def main():
    """main program to run by user"""
    weather = pd.read_csv("/Users/twff/Downloads/1007 project/weather.csv")
    data = pd.read_csv("/Users/twff/Downloads/1007 project/clean_data.csv")
    dayplot = pd.read_csv("/Users/twff/Downloads/1007 project/dayplot.csv")
    bar_data = pd.read_csv('/Users/twff/Downloads/clean_data.csv')   
    
    while True:
        print("Welcome to our program.")
        print('************************************************')
        print("1. Overall Collision Visualized in a year")
        print("2. Collision vs Weather in Daily/Monthly Basis")
        print("3. Location")
        print("4. Summary")
        print('************************************************')
        try:
            menu = input("Please input a number for further information:")
            #user choose overall collision in a year
            if int(menu) == 1:
                while True: 
                    print('----------------------------------------------------------')
                    print('Please select one kind of graph you want to have a look: ')
                    print('1. Bar Plot')
                    print('2. Line Plot of A Year')
                    print('3. Pie Chart of Borough')
                    print('---------------------------------------------------------')
                    try:
                        option = input("Please select one kind of graph you want to have a look:\n Enter 'back' to go back to menu")
                        if option.lower() == 'back':
                            break
                        if option.lower() == 'quit':
                            sys.exit(0)
                        if option == '1':
                            #print(bar_data.head(3))
                            contributing_fator_bar(bar_data,0.35,47)
                            vehicle_type_bar(bar_data,0.35,16)
                        if option == '2':
                            data['date'] = data['DATE'].map(lambda x:turn_date_to_int(x)) 
                            #print(data.head(3))
                            plot_month_total_line(data)
                            data['days'] = data['DATE'].map(lambda x:turn_day_to_int(x))
                            #print(data.head())
                            plot_whole_year(data)
                        if option == '3':
                            pie_borough(data)  
                    except ValueError:
                        print("ok")
                        
            #user choose collision vs weather
            if int(menu) == 2:
                while True: 
                    try:
                        day = input("Please input a date in numerical format mm/dd/yyyy or mm/yyyy: \n The date needs to be within Nov.2015 till Oct.2016 \n Enter 'back' to go back to menu")
                        if day.lower() == 'back':
                            break
                        if day.lower() == 'quit':
                            sys.exit(0)
                        check(day)
                        weatheroutput(weather)
                        collisionoutput(day, data, dayplot)   
                    except ValueError:
                        print()
                        
            if int(menu) == 3:
                while True: 
                    try:
                        zipcode = input("Please input a zip code in 5 numbers \n The input needs to be within New York area \n Enter 'back' to go back to menu")
                        if zipcode.lower() == 'back':
                            break
                        if zipcode.lower() == 'quit':
                            sys.exit(0)
                        zip_code = int(zipcode)
                        a = [   11219.,  10033.,  11235.,  11216.,  10467.,  11222.,
                                11364.,  11201.,  11378.,  10010.,  11691.,  11209.,  10022.,
                                11434.,  11236.,  11203.,  10456.,  11001.,  11238.,  11354.,
                                10305.,  11207.,  10035.,  10029.,  10023.,  11208.,  11223.,
                                10001.,  11413.,  10011.,  11692.,  11204.,  10017.,  11103.,
                                11374.,  11385.,  11375.,  11435.,  10453.,  11368.,  10314.,
                                11215.,  10459.,  10009.,  10024.,  10031.,  10032.,  11428.,
                                11432.,  10468.,  10469.,  10457.,  11415.,  10030.,  10065.,
                                11416.,  11419.,  11214.,  11239.,  11229.,  10016.,  10018.,
                                10312.,  11234.,  10012.,  11366.,  11221.,  10474.,  10028.,
                                11420.,  11101.,  10027.,  10466.,  11217.,  11377.,  10454.,
                                10304.,  10013.,  10458.,  10036.,  10002.,  11220.,  10301.,
                                10452.,  10308.,  10039.,  11426.,  11233.,  10005.,  11212.,
                                10019.,  11433.,  10455.,  10460.,  11231.,  11105.,  11218.,
                                11213.,  11356.,  10007.,  10021.,  11423.,  11104.,  10069.,
                                10465.,  10473.,  11429.,  11226.,  11230.,  10026.,  11040.,
                                10128.,  10306.,  11358.,  11205.,  11421.,  11355.,  11210.,
                                11360.,  11372.,  10169.,  11373.,  10463.,  10461.,  11418.,
                                10310.,  10038.,  11237.,  11412.,  10040.,  10004.,  11436.,
                                10307.,  11379.,  10451.,  11224.,  11211.,  11206.,  10462.,
                                11361.,  11225.,  10472.,  10034.,  10470.,  11367.,  11417.,
                                10025.,  11249.,  10003.,  10309.,  11363.,  11106.,  11228.,
                                10172.,  11427.,  11365.,  10014.,  11370.,  11362.,  11422.,
                                11411.,  10075.,  11369.,  11357.,  10037.,  11414.,  11430.,
                                11004.,  10475.,  11232.,  11693.,  11694.,  11102.,  10471.,
                                10006.,  10020.,  11697.,  10000.,  10123.,  10048.,  10119.,
                                10281.,  10280.,  10302.,  10464.,  11109.,  11005.,  10282.,
                                10111.,  11359.,  10303.,  10153.,  10803.,  11251.,  10105.,
                                11242.,  11695.]#This is an unique NYC zip code data set  in our system
                        a = list(map(int,a))
                        if zip_code not in a:
                            raise ValueError
                        plot_geomap(zip_code, bar_data )
                        
                    #day = date(day)
                    #function identify input is valid?????
                    #print(day)
                        weatheroutput(weather)
                        collisionoutput(day, data, dayplot)   
                    except ValueError:
                        print("Invalid zipcode input. Please input zipcode within NYC area.")
                        
            if int(menu) == 4:
                while True:
                    print('something')
                    print('---------------------------')
                    print('1. weather corr')
                    print('2. weather and car collision corr')
                    print('3. bonus') 
                    print('---------------------------')
                    
                    try:
                        option = input("Please select which one you want to see \n Enter 'back' to go back to menu")
                        if option.lower() == 'back':
                            break
                        if option.lower() == 'quit':
                            sys.exit(0)
                        if int(option) == 1:
                            corr = correlation(rangen = 13)
                            corr.weather_corr(weather, data)
                        if int(option) == 2:
                            collision_data = data.drop(['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND','MaxFactor','MaxVehicle'],1)
                            corr = correlation(label='DATE')
                            corr.weather_collision_corr(weather, collision_data)  
                        if int(option) == 3:
                            print('Bonus!')
                    except ValueError:
                        print("ok")
        except ValueError:
            print("Please input an integer from 1 to 4")
        except KeyboardInterrupt:
        # Exit if the user enters Ctrl+C
            sys.exit(0)
        except EOFError:
        # Exit if the user enters Ctrl+D
            sys.exit(0)
            
if __name__ == "__main__":
    main()
