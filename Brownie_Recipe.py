# File: 2252_McnamaraJ_Lesson1#_InLab.py 
# Name: Brownie Recipe
# Author: Joseph McNamara 
# Date: March 22, 2021
# Purpose: This program provides the amount of ingredients needed per brownie. 
# Eggs are kept as integers to prevent the need of partial eggs. 
# Other ingredients are rounded to 2 decimal places. 

number_of_brownies = int(input('How many brownies would you like to make?'))

print('Your recipe calls for:')

print(round(((0.5/9) * number_of_brownies),2), '\tcups butter')
print(int((2/9) * number_of_brownies), '\teggs')
print(round(((1/9) * number_of_brownies),2), '\tteaspoon vanilla')
print(round(((1/9) * number_of_brownies),2), '\tcup sugar')
print(round(((0.5/9) * number_of_brownies),2), '\tcups flour')
print(round(((0.5/9) * number_of_brownies),2), '\tcups cocoa powder')
print(round(((0.25/9) * number_of_brownies),2), '\tteaspoons baking powder')
print(round(((0.25/9) * number_of_brownies),2), '\tteaspoons salt')

done = input("""Enoy your bronies!
press enter when finished with this recipe.""")
