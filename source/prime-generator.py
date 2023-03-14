# Python 3.9
# Coding: utf-8
# Version: 2.0
##########################################################################################
# This program finds prime numbers between a beginning and an ending numbers. The prime  #
# numbers store in comma-seperated sring then it writes into file called, 'results.txt   #
##########################################################################################

from numba import jit # Import jit module from numba library
from functools import wraps # Import wraps module from functools library
from time import time # Import time module from time library
def timer(function):
    """
    This decorator function measures how long it takes to execute of a function.
    Usage: add '@timer', a line before the function.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        funcName = function.__name__
        startTime = time()
        value = function(*args, **kwargs)
        endTime = time()
        if (endTime - startTime) < 1:
            print(f"Function <{funcName}> execution took {(endTime - startTime) * 1000:.2f} ms ...")
        elif (endTime - startTime) > 60:
            print(f"Function <{funcName}> execution took {(endTime - startTime) / 60:.2f} ms ...")
        else:
            print(f"Function <{funcName}> execution took {(endTime - startTime):.2f} s ...")
        return value
    return wrapper

# Import library and module to identify working directories
import os
from pathlib import Path

directory_base = str(os.getcwdb())[2:-1]

if os.name == 'nt':
    directory_data = Path(directory_base + '/data')
    directory_source = Path(directory_base + '/source')
else:
    directory_data = directory_base + '/data'
    directory_source = directory_base + '/source'

@timer # Decorator to time this function
@jit(nopython = True) # Disadvantage: slow down by realtime compiling to C++ 
def getPrime(numberStart:int, numberEnd:int):
    """
    This function gets prime numbers between starting and ending numbers.
    """
    check_number = 2
    primes = []
    for i in range(1, numberEnd):
        for j in primes:
            if check_number % j == 0:
                break
        else:
            primes.append(check_number)
        check_number += 1
    
#    listPrime = filter(lambda i : i >= numberStart, primes) # Code can't be used with jit decorator
    listPrime = []
    for i in primes:
        if i >= numberStart:
            listPrime.append(i)
        else:
            pass
    
    return ','.join(map(str, listPrime))

def getNumbers(*args, **kargs):
    """
    This function gets the starting and ending number from user entry.
    """
    def entryNumbers(*args, **kargs):
        # User inputs integral numbers:
        strNum = input("Please enter the starting number: ")
        endNum = input("Please enter the ending number: ")
        return strNum, endNum

    # Get user entry and check both entries are integers greater than zero:
    startNumber, endNumber = entryNumbers()
    inputs = False
    while inputs == False:
        if startNumber.isdigit() and endNumber.isdigit():
            startNumber = int(startNumber)
            endNumber = int(endNumber)
            if startNumber > 0 and endNumber > 0:
                if startNumber < endNumber:
                    inputs = True
                else:
                    print(f"{startNumber} is greater than {endNumber}!")
                    startNumber, endNumber = entryNumbers()
            else:
                print(f"Either {startNumber} or {endNumber} is less than zero!")
                startNumber, endNumber = entryNumbers()
        else:
            print(f"Either {startNumber} or {endNumber} is not an integer!")
            startNumber, endNumber = entryNumbers()
    # Return integers:
    return startNumber, endNumber

def main():
    """
    This is the main function to run a program.
    """
    # Get user to input starting and ending numbers at terminal:
    print("Get prime numbers between a starting number and ending number")
    startNumber, endNumber = getNumbers()

    # Get prime numbers from 1 to 250
    prime_result = getPrime(startNumber, endNumber)
    print(f"...Found {len(prime_result.split(','))} prime numbers...")
#    print(prime_result)

    # Write results of prime numbers to text file
    with open(directory_data + '/results.txt', 'w') as fileText:
        fileText.write(prime_result)
    fileText.close()

if __name__ == '__main__':
    main()
