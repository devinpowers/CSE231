#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:35:49 2019

@author: devinpowers
"""

# Lab 1 in CSE 231
#Quadratic Formula
# Find the roots in the Quadratic Formula
    
import math

a = float(input("Enter the coeddicient a: "))
b = float(input("Enter the coeddicient b: "))
c = float(input("Enter the coeddicient c: "))

print (" Coefficients:")
print( " Coefficient of a = ", a)
print( " Coefficient of b = ", b)
print( " Coefficient of c = ", c)

root_1 = (-b+(b**2-4*a*c)**(0.5))/(2*a)
root_2 = (-b-(b**2-4*a*c)**(0.5))/(2*a)

print("The roots of the equation:")
print( " Root 1 =", root_1)
print( " Root 2 =", root_2)
