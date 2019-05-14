'''
Created on May 6, 2019

@author: s271486
803 program
'''
class vehicle:
    def __init__(self):
        self.__licensePlate = "12F34"
        self.__colour = "Red"
        self.__num_doors = 4
        self.__speed = 0
        self.__maxspeed = 60
        self.__manual = 1
        
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
    
    def get_manual(self):
        return self.__manual
    
    def set_manual(self, new_manual):
        if new_manual < 0 or new_manual >10:
            pass
        else:
            self.__manual_recalc(new_manual)
            self.__manual = new_manual
            
    def __manual_recalc(self, new_manual):
        old_manual = self.__manual
        
        if old_manual > new_manual:
            self.__speed = self.__speed - 5
        elif old_manual < new_manual:
            self.__speed = self.__speed + 5
        else:
            pass
            
    def brakes(self, speed_decrease):
        self.__speed = self.__speed - speed_decrease
        
    def current_state(self):
        return_string = "License Plate:" + str(self.__licensePlate) +" "+ "Colour:" + str(self.__colour) + "Number of car doors" + " " + str(self.__num_doors) + " " + "Speed" + str(self.__speed) + " " + "Max Speed" + str(self.__maxspeed) +"Manual" + " " + str(self.__manual)
        return return_string