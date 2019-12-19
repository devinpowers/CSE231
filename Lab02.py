#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:12:46 2019

@author: devinpowers
"""


odd_sum= 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count =0


n_str = input("Input an integer (0 terminates): ")

int_str = int(n_str)
# Good stuff goes here

while int_str != 0:
    
    if int_str > 0:
        positive_int_count += 1
        
        if int_str%2 == 0:
            even_sum += int_str
            even_count += 1
        else:  
            odd_count +=1
            odd_sum += int_str
    else:
        print("You have entered a negative number. It will not be recorded/")
        
    n_str = input("Input an integer (0 terminates): ")

    int_str = int(n_str)

        
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
