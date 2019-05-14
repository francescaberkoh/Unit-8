'''
Created on May 1, 2019

@author: s271486
801
'''
class vehicle:
    def __init__(self):
        self.__licensePlate = 0 
        self.__colour = " "
        self.__num_doors = 2
        self.__speed = 0
        self.__maxspeed = 60
        
    def accelerate(self, speed_increase):
        self.__speed= self.__speed + speed_increase
    
    def brakes(self, speed_decrease):
        self.__speed = self.__speed - speed_decrease
        
    def current_state(self):
        return_string = "License Plate:" + str(self.__licensePlate) +" "+ "Colour:" + str(self.__colour) + "Number of car doors" + " " + str(self.__num_doors) + " " + "Speed" + str(self.__speed) + " " + "Max Speed" + str(self.__maxspeed)
        return return_string