#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:56:36 2020

@author: emilywu
"""
import random

class slayer:
    def __init__ (self, swordColor, level, bandage, HP, ATK, DEF):
        self.swordColor = swordColor
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.bandage = bandage
        
    def attack (self, level):
        if self.level = 1:
            return self.ATK = 200
        elif self.level = 2:
            return self.ATK = 500
        elif self.level = 3:
            return self.ATK = 1000
        elif self.level = 4:
            return self.ATK = 1300
        elif self.level = 5:
            return self.ATK = 1500 and self.DEF += 100
        elif self.level = 6:
            return self.ATK = 1700 and self.DEF += 100
        elif self.level = 7:
            return self.ATK = 2000 and self.DEF += 200
        elif self.level = 8:
            return self.ATK = 2300 and self.DEF += 200
        elif self.level = 9:
            return self.ATK = 2700 and self.DEF += 300
        else:
            return self.ATK = 3000 and self.DEF += 500
    
    def upgradeSword (self, swordColor):
        if self.swordColor = "black":
            print ("your level is the lowest")
        elif self.swordColor = "blue":
            print ("your level is 3 lower or higher")
        elif self.swordColor = "purple":
            print ("your level is normal")
        elif self.swordColor = "green":
            print ("your level is 7 lower or higher")
        else:
            print ("your skills are above all slayers!")
   
    def underAttack (self, DEF):
        if self.DEF >= 1000:
            return self.HP -= 0 and self.DEF -= 100
        elif self.DEF <= 800 and >= 500:
            return self.HP -= 200 and self.DEF -= 100
        elif self.DEF <= 500 and >= 300:
            return self.HP -= 400 and self.DEF -= 100
        elif self.DEF <= 300 and >= 100:
            return self.HP -= 700 and self.DEF -= 100
        else:
            return self.HP -= 1000
    
    def levelUpgrade (self, level):
        random.getrandbits(True, False)
        if True:
            return self.level += 1 
        else:
            return self.level += 0
    
    def useBandage (self, bandage):
       if self.bandage = 0:
           return self.HP + 0 and print ("there are no bandages left!")
       else:
           return self.HP + 500 and self.bandage -= 1
    def kill (self, ATK):
        random.getrandbits(True, False)
        if True:
            if ATK >= 2000:
                print ("you won!")
            elif ATK <= 2000:
                print ("you loss~ please press run and start again")
        else:
            if ATK >=1000 and <= 500:
                print ("you won!")
            if ATK <= 500:
                print ("you loss~ please press run and start again")
                
Louis = slayer ("black", 1, 5, 5000, 200, 800)
print ("Louis' sword color is " Louis.swordColor)
print ("Louis' level is " Louis.level)
print ("Louis' bandage left " Louis.bandage)
print ("Louis' HP is " Louis.HP)
print ("Louis' ATK is " Louis.ATK)
print ("Louis' DEF is " Louis.DEF)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    