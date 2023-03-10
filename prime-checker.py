# This function 1 checks whether number is a prime
def isPrime(number):
    if number < 2:
        return False
    for index in range(2, int(number // 2 + 1)):
        if number % index == 0:
            return False
    return True

def isPrime2(number):
    # Check for prime numbers: 2 and 3
    if number < 2:
        return False
    elif number <= 3:
        return True
    
    iterator = int(number // 2 + 1)
    # Is iterator a prime number?
    if iterator == 1:
        return True
    # Is number divisible by iterator?
    elif number % iterator == 0:
        return False
    
    elif number % (number // 2) == 0:
        return False
    
    return True

#number = 123457
number = 69

print(number % int(number // 2 + 1))
print(number % int(number // 2))

if isPrime2(number) == True:
    print(f"{number} is a prime number.")
else:
    print(f"{number} isn't a prime number.")
