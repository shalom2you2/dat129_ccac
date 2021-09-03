# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 08:29:31 2021

@author: nikki
"""
## Your desired program output is a formal greeting for individuals whose names exist
## in a text file in the order: first last. The output should look like this:
## output. The process of generating these greetings should take place in two 
## functions: one should read in a file given a file name (assumed to be in the 
## working directory) and extract the name in a single line. The second method 
## should receive a line of text (i.e. a name in the form first last) and generate 
## the greeting. Remember, you'll need to invert the string since we're using 
## string formatting, not string concatenation.

people = open("names.txt", "r")

name = people.readlines()
for person in name:
    greet = person.split()
    print("Good evening Dr." + greet[1] + ", Would you mind if I call you " + greet[0] + "?")
