#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:17:19 2020

@author: devinpowers
"""


#Bank Application


WELCOME = "Welcome to the vending machine change maker program"

STOCK_MSG = "Stock contains:"

#Stock

Quarters = 10
Dimes = 10
Nickels = 10
Pennies =10

print(WELCOME)

print(STOCK_MSG)

print("  ", Pennies, "pennies")
print("  ", Nickels, "nickels")
print("  ", Dimes, "dimes")
print("  ", Quarters, "quarters")

# Enter Price of Product

price_response = input("Please enter the price (xx.xx) or 'q' to quit: ")

# loop begins

while price_response != 'q':
    
    
    #convert float to int
    price = int((float(price_response)*100))
    #check if price is negative!
    if price < 0:
        print("Illegal number: The number you have entered must be positive! ")
     #ASK for the price of the number again
        price_response = input("Pelease enter the price (xx.xx) or 'q' to quit ") 
        continue
    
    # ask for dollars entered
    dollars_entered = int(input("Please enter the number of dollars paid: ")) *100

    # check if the number of dollars entered > the price of the item
    
    if  dollars_entered < price:
        print("not enough money was entered, please try again! ")
        continue
    else:
       change = dollars_entered - price
       print("\nThe amount owed back in change is (cents): ", change)
       
        
           
 # Gve change back       
         
       quarter_count = 0
       Dimes_count = 0
       nickel_count = 0
       pennie_count = 0
        
       while change >= 25 and Quarters > 0:
           change = change - 25
           Quarters -= 1
           quarter_count += 1
           
       while change >= 10 and Dimes >0:
           change = change - 10
           Dimes -= 1
           Dimes_count += 1
               
               
       while change >= 5 and Nickels >0:
           change = change - 5
           Nickels -=1
           nickel_count +=1
                   
       while change >=1 and Pennies >0:
           change = change -1
           Pennies -= 1
           pennie_count += 1
           
       if change == 0:
           print("No Change.")
                       
       if change > 0:
           print("\nDont have enough change left")
           price_response = 'q'
           
           continue
          
                       
    print("\nNew Change left over : ", change)
    
    print("\nQuarters Given Back:   ", quarter_count)
    print("Dime Given Back:       ", Dimes_count)
    print("Nickels Given Back:    ", nickel_count)
    print("Pennies Given Back:    ", pennie_count)
    
    print("\n Stock:")
    print("  ", Pennies, "pennies")
    print("  ", Nickels, "nickels")
    print("  ", Dimes, "dimes")
    print("  ", Quarters, "quarters")

   
   

    
    price_response = input("Press 'q' to quit or type the price (xx.xx) for another calc: ")
    
                           
                           
            

    
        




    
    
      