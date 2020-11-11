#!/bin/env python3

def prnum(number):
    """this is function can be printing your number with private color"""
    try:
        number = int(number)
    except ValueError:
        print(f"this is {number} not a number! but recomend = 2")
        number = 2

    if number == 0:
        #printing a number with black font color
        print('\033[30m'+str(number) , end = "\t")
    if number == 2:
        #printing a number with lightgreen font color
        print('\033[92m'+str(number) , end = "\t")
    if number == 2**2:
        #printing a number with green font color
        print('\033[32m'+str(number) , end = "\t")
    if number == 2**3:
        #printing a number with cyan font color
        print('\033[36m'+str(number) , end = "\t")
    if number == 2**4:
        #printing a number with orange font color
        print('\033[33m'+str(number) , end = "\t")
    if number == 2**5:
        #printing a number with blue font color
        print('\033[34m'+str(number) , end = "\t")
    if number == 2**6:
        #printing a number with purple font color
        print('\033[35m'+str(number) , end = "\t")
    if number == 2**7:
        #printing a number with lightblue font color
        print('\033[94m'+str(number) , end = "\t")
    if number == 2**8:
        #printing a number with lightgrey font color
        print('\033[90m'+str(number) , end = "\t")
    if number == 2**9:
        #printing a number with lightcayn font color
        print('\033[96m'+str(number) , end = "\t")
    if number == 2**10:
        #printing a number with lightred font color
        print('\033[91m'+str(number) , end = "\t")
    if number == 2**11:
        #printing a number with red font color
        print('\033[31m'+str(number) , end = "\t")

def plist(numbers):
    """this function can be printing the numbers with private colors"""
    for i in range(numbers):
        prnum(numbers[i])

def prmat(mat):
    """this is function can be priting matrix"""
    for i in range(len(mat)):
        plist(mat[i])
        print("\n")