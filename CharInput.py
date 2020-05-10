""" 
    Provlem description: A scripts that returns a year when user will turn 100
    Difficulty Level: Easy
    @author: iCule10 
"""
from datetime import date
name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
today = date.today().year
year = str((today - age) + 100)
print(name + " will be 100 year older in " + year)