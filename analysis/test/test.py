'''
Created on Dec 16, 2016

@author: twff
'''
from geomap import *
from overallplot import *
import unittest
from Date import *
from correlation import correlation

#geomap = pd.read_csv('geomap - new.csv')
weather = pd.read_csv("/Users/twff/Downloads/1007 project/weather.csv")
data = pd.read_csv("/Users/twff/Downloads/1007 project/clean_data.csv")
dayplot = pd.read_csv("/Users/twff/Downloads/1007 project/dayplot.csv")
bar_data = pd.read_csv('/Users/twff/Downloads/clean_data.csv')

class testClass(unittest.TestCase):
    def testSetup(self):
        pass
    
    def testClass(self):
        correlation(rangen=10, label='da')
        correlation(rangen=5, label='A')
        correlation(rangen=5)
        correlation(label='A')
        correlation()
        
    def testEq(self):
        corr = correlation(rangen=10)
        self.assertEqual(corr.rangen, corr.rangen)
        self.assertEqual(len(corr.label), 4)
    
    def testinit(self):
        corr = correlation(rangen=5, label='A')
        self.assertEqual(corr.rangen, 5)
        self.assertEqual(corr.label, 'A')
        
    
#     def test_plot_geomap(self):
#         self.assertEqual(len(str(plot_geomap(10006, geomap))), 4)
        
#     def test_gro_input(self):
#         def assertValueError(zipcode):
#             with self.assertRaises(ValueError):
#                 plot_geomap(zipcode, geomap)
#         assertValueError("")
#         assertValueError(80000)
#         assertValueError(100000)
#         assertValueError(12345)
#         assertValueError(1234)
#         assertValueError(322)
#         assertValueError(23)
#         assertValueError(1)
#         assertValueError('10001')
#         assertValueError('qllyd')
#         assertValueError([10001])
#         assertValueError(10001.0)
    
    def testMerge(self):
        corr = correlation(rangen = 13)
        self.assertEqual(len(weather), len(corr.weather_collision_merge(weather, data)))
    
    def test_turn(self):
        self.assertEqual(len(turn_day_to_int('01/01/2016')), 8)
        self.assertEqual(len(turn_date_to_int('01/01/2016')),6)
        self.assertEqual(turn_day_to_int('01/01/2016'), '20160101')
        self.assertEqual(turn_date_to_int('01/01/2016'), '201601')
        self.assertEqual(turn_date_to_int('01/01/2016'), turn_date_to_int('01/02/2016'))
        
    
if __name__ == '__main__':
    unittest.main()