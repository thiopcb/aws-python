# Python 3.9
# Coding: utf-8
# Version: 1.0
##########################################################################################
# This program finds prime numbers between a beginning and an ending numbers. The prime  #
# numbers store in comma-seperated sring then it writes into file called, 'results.txt   #
##########################################################################################

from functools import wraps # Import wraps function from functools library
from time import time # Import time function from time library
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
            print(f"Function <{funcName}> execution took {(endTime - startTime) / 60:.2f} M ...")
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
def getPrime(numberStart:int, numberEnd:int):
    """
    This function gets prime numbers between starting and ending numbers.
    """
    # Get a list of all prime numbers until variable 'numberEnd':
    numberEnd += 1
    numbers = range(2, numberEnd)
    primes = []
    primes = list(filter(lambda i : all(i % j != 0 for j in range(2, int(i // 2))), numbers))

    listPrime = filter(lambda i : i >= numberStart, primes)

    return ','.join(map(str, listPrime))

def getNumbers():
    """
    This function gets the starting and ending number from user entry.
    """
    startNumber = input("Please enter the starting number: ")
    endNumber = input("Please enter the ending number: ")
    return startNumber, endNumber

def main():
    """
    This is the main function to run a program.
    """
    # Get user to input starting and ending numbers at terminal:
    print("Get prime numbers between a starting number and ending number")
    startNumber, endNumber = getNumbers()

    # Check both inputted numbers are integers greater than zero:
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
                    startNumber, endNumber = getNumbers()
            else:
                print(f"Either {startNumber} or {endNumber} is less than zero!")
                startNumber, endNumber = getNumbers()
        else:
            print(f"Either {startNumber} or {endNumber} is not an integer!")
            startNumber, endNumber = getNumbers()

    # Get prime numbers from 1 to 250
    prime_result = getPrime(startNumber, endNumber)
    print(f"...There're {len(prime_result.split(','))} prime numbers between {startNumber} and {endNumber}...")
#    print(prime_result)

    # Write results of prime numbers to text file
    with open(directory_data + '/results.txt', 'w') as fileText:
        fileText.write(prime_result)
    fileText.close()

if __name__ == '__main__':
    main()
