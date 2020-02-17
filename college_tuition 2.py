#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:30:51 2020

@author: devinpowers
"""


# college tuition calculator



tuition_exit = 0

while tuition_exit == 0:
    
    #Bank of tition expenses
    
    Resident = True
    
    Grade_level = 0 # freshman = 1, grade
    
    Tuition = 0
    
    College = ''
    
    Credits = ''
    
    # find out if you're a resident of Michigan 
    
    ask_resident = str(input("Are you a resident of Michigan? (Yes or No?): "))
    
    ask_resident_lower = ask_resident.lower()
    
    if ask_resident_lower != 'yes':
        Resident = False
        
    # FInd out there grade level
    
    Grade_level = str(input("What is your grade level? (Freshman, Sophomore, junior, senior. or graduate? "))
    
    Grade_level_lower = Grade_level.lower()
    
    if Grade_level_lower == 'freshman':
        Grade_level = 1
    elif Grade_level_lower =='sophomore':
        Grade_level = 2
    elif Grade_level_lower =='junior':
        Grade_level = 3
    elif Grade_level_lower == 'senior':
        Grade_level = 4
    elif Grade_level_lower == 'graduate':
        Grade_level = 5
    else:
        print("Error: incorrect response")
        Grade_level = str(input("What is your grade level? (Freshman, Sophomore, junior, senior. or graduate? "))
        

    
    # What college are they in?
    
    if Grade_level == 3 or Grade_level == 4 or Grade_level == 5:
        College = str(input("What College are you in? (Business, Engineering, health, Science, or None?: "))
    
    
    # how Many Credits are you taking?
    
    Credits = int(input("How many Credits are you taking? "))
    
    
    # Calculating Tuition  per credit hou
    
    if Resident == True:
        
        if Grade_level == 1 or Grade_level == 2:
            Tuition += 468.75*Credits
        if Grade_level == 3 or Grade_level == 4:
            Tuition += 523.25*Credits
        if Grade_level == 5:
            Tuition += 698.50*Credits
            
    if Resident == False:
        
        if Grade_level == 1 or Grade_level == 2:
            Tuition += 1263*Credits
        if Grade_level == 3 or Grade_level == 4:
            Tuition += 1302.75*Credits
        if Grade_level == 5:
            Tuition += 1372*Credits
            
    
    print("The calculated Tuition based on their resident status is: ", Tuition)
    
        
    # special fees
    
    
    # APrt time student:
    if Credits <= 4:
        
        if College == 'business' and Grade_level == 3 or 4:
            Tuition += 109
        if College == 'engineering' and Grade_level == 3 or 4 or 5:
            Tuition += 387
        if College == 'health' and  Grade_level == 3 or 4:
            Tuition += 50
        if College == 'sciences' and Grade_level == 3 or 4:
            Tuition += 50
        if Grade_level == 5:
            Tuition += 37.50
    
    # Full time Student:
    if Credits > 4:
        
        if College == 'business' and Grade_level == 3 or 4:
            Tuition += 218
        if College == 'engineering' and Grade_level == 3 or 4 or 5:
            Tuition += 645
        if College == 'health' and  Grade_level == 3 or 4:
            Tuition += 100
        if College == 'sciences' and Grade_level == 3 or 4:
            Tuition += 100
        if Grade_level == 5:
            Tuition += 75
            
        
        
    # student Voted Taxes
            
    # FM Radio Tax for everyone
            
    Tuition += 3
    
    #ASMU TAX
    
    if Grade_level != 5:
        Tuition += 18
    
    # COGs tax
    
    if Grade_level == 5:
        Tuition += 11
    
    if Credits >= 6:
        Tuition += 5
        
    
    # calculating Final Shit:
    
    

    print("Are they a Resident", Resident)
    print('What is their grade level?: ', Grade_level)
    print("What is there College?: ", College)
    print("How Many Credits are they taking?", Credits)
    
    print("\n Tuition cost for this student is: ", Tuition)
    
    # ask if they wanna do another calc
    
    ask_again = str(input("Would you like to perform another Tuition Check (Yes or No): "))
    ask_again_lower = ask_again.lower()
    
    if ask_again_lower != 'yes':
        
        tuition_exit == 1
        break
    else:
        tuition_exit == 0
        continue
    


    
        
        
        
    
    
    
            
        