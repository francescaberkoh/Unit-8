'''
Created on May 1, 2019

@author: s271486
801 test page
'''
from  Vehicle import *

Vehicle = vehicle()


Vehicle.accelerate(30)
print(Vehicle.current_state())

Vehicle.brakes(40)
print(Vehicle.current_state())