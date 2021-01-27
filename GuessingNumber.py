#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:23:14 2021

@author: jeremy
"""

import random

rand_num = random.randint(1,10)

#print(rand_num)

#function greeting and returning name
def greeting():
    print('Welcome to the Guessing Number Game!')
    user_name = input('What is your name? ')
    print('Hello, ' + user_name.title())
    return user_name

#function asking if they would like to guess a number and returning value
def user_prompt(name):
    guess = int(input('Please choose a number between 1 and 10: '))
    print(name.title() + ' chose: ' + str(guess))
    return guess

#function comparing user_guess and rand_num
def result(user_guess, rand_number):
    if user_guess == rand_number:
        print('You win!')
        return False
    else:
        print('Nope')
        if user_guess > rand_number:
            print('too high')
            return True
        elif user_guess < rand_number:
            print('too low')
            return True
            
name = greeting()

res = True
count = 3

while res == True and count > 0:
    guess = user_prompt(name)
    res = result(guess, rand_num)
    if res == True:
        count -= 1
        print(str(count) + ' chances remaining.')
        if count == 0:
            print('Sorry! You lose.')