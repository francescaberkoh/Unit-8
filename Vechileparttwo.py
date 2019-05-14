'''
Created on May 2, 2019

@author: s271486
802
'''
class vehicle:
    def __init__(self):
        self.__licensePlate = "12F34"
        self.__colour = "Red"
        self.__num_doors = 4
        self.__speed = 0
        self.__maxspeed = 60
        
    def accelerate(self, speed_increase):
        self.__speed = self.__speed + speed_increase 
    
    def get_speed(self):
        return self.__speed
    
    def get_licensePlate(self):
        return self.__licensePlate
    
    def get_colour(self):
        return self.__colour
    
    def get_num_doors(self):
        return self.__num_doors
    
    def get_max(self):
        return self.__maxspeed
    
    def set_max(self, newmax):
        self.__maxspeeed = newmax
    
    def brakes(self, speed_decrease):
        self.__speed = self.__speed - speed_decrease
        
    def current_state(self):
        return_string = "Liceense Plate:" + str(self.__licensePlate) +" "+ "Colour:" + str(self.__colour) + "Number of car doors" + " " + str(self.__num_doors) + " " + "Speed" + str(self.__speed) + " " + "Max Speed" + str(self.__maxspeed)
        return return_string