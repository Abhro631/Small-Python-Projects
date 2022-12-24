import random

#range of the output values of a dice
minimum_val = 1
maximum_val = 6

#to loop the rolling cursor as per user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Coming or output Values are :")
    
    #generating and printing 1st random integer from 1 to 6
    print(random.randint(minimum_val, maximum_val))
    
    #generating and printing 2nd random integer from 1 to 6
    print(random.randint(minimum_val, maximum_val))
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?") 
    
