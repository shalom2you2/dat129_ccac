# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:13:15 2021

@author: nikki
"""
## Homework assignment: Study the following file contents. Generate a program in Python to 
## reproduce this structure. NOTE: You'll need to use two for() loops, nested. You can try 
## seeing if you can print the pattern out first to the console, then replace the calls to print() 
## with calles to yourfile.write().
## Write a text file and numbers in decending order.
## Use two "for" loops.
## First line has numbers 0-9.
## Last line is 0.

file = open("DAT129_Proj1_Ranges.txt", "w") 

y = 10

for i in range(10):
    x = ""
    for s in range(y):
        x = x + str(s)
    y = y - 1
    file.write(x)
    file.write("\n")
    
file.close()