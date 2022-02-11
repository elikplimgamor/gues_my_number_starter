#!/usr/bin/env python
# coding: utf-8

# # This is a program file for a guess game 

# In[ ]:


# importing library of code to generate random integer between 1 and 99
import random

number = random.randint(1, 99)

# asking user to type his name
name = input('Enter your name  : ')
print('\nHello ' + name + ' ,  you are welcome to the guess_my_number_starter game  ')

# asking users to input a number
guess = int(input('guess a number between 1 and 99'))

#Loop
while guess != number:
    if guess > number:
        print('PROMPT : Your guess is too higher 👆 . \nTry again ')
        print('You have entered  ' +str(guess) + ' here')
        print('But the correct answer is '+ str(number))
        guess = int(input('\n Guess a number between 1 and 99  \n'))
        
    else:
        print('PROMPT : Your guess is too lower than the expected number  . \nTry again ')
        print('You entered  ' + str(guess)  + ' here')
        print('But the correct answer is '+ str(number))
        guess = int(input('\n Guess a number between 1 and 99  \n'))

print('your guess is right \n congrats ' + name)


# In[ ]:




