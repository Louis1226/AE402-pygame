#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:08:27 2020

@author: emilywu
"""
class Human():
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
       

    def bmi(self):
        return self.weight//((self.height/100)**2)
    
    def perfectBmi():
        if me.bmi >= 24:
            return print ("too high")
        elif me.bmi <= 18:
            return print ("too low")
        else:
            return print ("normal")

    
me = Human('Louis',32,149)
print("name",me.name)
print("weight", me.weight)
print("height", me.height)
print("bmi", me.bmi()) 


