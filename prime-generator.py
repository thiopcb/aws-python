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
        else:
            print(f"Function <{funcName}> execution took {(endTime - startTime):.2f} s ...")
        return value
    return wrapper

@timer # Decorator to time this function
def getPrime(numberStart:int, numberEnd:int):
    """
    This function gets prime numbers between starting and ending numbers.
    """
    # This function checks whether number is a prime
    def isPrime(number):
        if number < 2:
            return False
        for index in range(2, int(number // 2 + 1)):
            if number % index == 0:
                return False
        return True

    # Initialize a list to store prime number:
    numbers = list(range(numberStart, numberEnd + 1))
    listPrime = []

    # Loop through starting and ending numbers to get prime numbers:
    for number in numbers:
        if isPrime(number) == True:
            listPrime.append(number)

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
    print(f"...There're {len(prime_result.split(','))} prime numbers...")
#    print(prime_result)

    # Write results of prime numbers to text file
    with open('results.txt', 'w') as fileText:
        fileText.write(prime_result)
    fileText.close()

if __name__ == '__main__':
    main()
