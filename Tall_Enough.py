# File: 2252_McnamaraJ_Lesson2#_InLab.py 
# Name: Python Rocks Amusement
# Author: Joseph McNamara 
# Date: March 29, 2021
# Purpose: Welcome guests to the amusement park, 
# determine the guest's height in inches, 
# and provide the entry tier and cost based on the height. 

print('Welcome to Python Rocks amusement. Please enter guest\'s height in inches:')
guest_height = float(input())
tier = ""
price = 0

if guest_height < 30:
    tier, price = 'Guppy', 'free'
elif 30 <= guest_height < 36:
    tier, price = 'Pollywog', '$2'
elif 36 <= guest_height < 42:
        tier, price = 'Apprentice', '$5'
elif  42 <= guest_height < 48:
    tier, price = 'Explorer', '$8'
elif  guest_height >= 48:
    tier, price = 'Adventurer', '$10'


print(f'Welcome {tier}. Your price is {price}.')

complete = input('\nPress enter when finished.')
