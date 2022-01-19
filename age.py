# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:45:06 2022

@author: user
"""

driving = input('have you ever drien a car?')
if driving != 'Yes' and driving != 'No':
   print('only Yes or No is allowed')
   raise SystemExit
age = input('what is your age? ')
age = float(age)
if driving == 'Yes':
    if age >= 18:
        print('You have a license')
    else:
        print('why you have a license')
elif driving == 'No':
    if age >= 18:
        print('You are allowed to participate car test')
    else:
        print('You are allowed to participate car test in a few years')
else:
    print('You keyed in a wroing answer')