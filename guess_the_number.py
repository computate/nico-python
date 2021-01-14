'''
Created on Jan 9, 2021

@author: ctate
'''
import random

if __name__ == '__main__':
    low = 1
    high = 20
    number = random.randint(low,high)
    guess = int(input("I'm thinking of a number from %s to %s. What is it?" % (low,high)))
    while guess != number:
        if guess < number:
            print("Your number was too low...")
        else:
            print("Your number was too high...")
        guess = int(input("Please try again..."))
    print("Congratulations! Correct answer!")