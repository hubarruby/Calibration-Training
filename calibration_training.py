#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 08:54:27 2022

@author: harrison gietz
"""
#this is based on the calibration excersize in 
#Julia Galef's "The Scout Mindset" (pg 80)

import pandas as pd
import matplotlib.pyplot as plt

#input csv files has:
    #col 0 = my guesses
    #col 1 = my percentage confidence corresponding to each guess
    #col 3 = the correct answer (must be typed out exactly the same as col 0)
    
df = pd.DataFrame(pd.read_csv('self_calibration_data.csv',  header = None))

fifty_five = df[df[1]==55]
sixty_five = df[df[1]==65]
seventy_five = df[df[1]==75]
eighty_five = df[df[1]==85]
ninety_five = df[df[1]==95]

percentage_list = [fifty_five,sixty_five,seventy_five,eighty_five,ninety_five]

x_vals = []
y_vals = []

def calibrate(df):
    tot_correct= 0
    for i in range(len(df)):
        if df.iloc[i,0] == df.iloc[i,2]:
            tot_correct += 1
    tot_wrong = len(df)-tot_correct
    perc_correct = tot_correct/(tot_correct+tot_wrong)
    x_vals.append(df.iloc[0,1])
    y_vals.append(perc_correct*100) 
    
for i in percentage_list:
    calibrate(i)

plt.scatter(x = x_vals, y = y_vals)
plt.axline((50, 50), (100, 100))
plt.xlabel('When I feel ___% sure of my answer')
plt.ylabel('I am right ___% of the time')
plt.show()