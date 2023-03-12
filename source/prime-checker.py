from time import time

# This function 1 checks whether number is a prime
def isPrime(number):
    if number < 2:
        return None
    elif number <= 3:
        return number
    else:
        iterator = range(2, int(number // 2 + 1))
        for index in iterator:
            if number % index == 0:
                return None
    return number

def getPrime(numberStr:int, numberEnd:int):
    
    if numberStr < 2:
        check_number = 2
    else:
        check_number = numberStr
    
    primes = []

#    primes.append(check_number)
    for i in range(check_number - 1, numberEnd + 1):
        for j in primes:
            if check_number % j == 0:
                break
        else:
            primes.append(check_number)
        check_number += 1
    return primes

num1 = 9999991
num2 = 123457
num3 = 69
num4 = 4
num5 = 2
num6 = 1
number = num3

str_time = time()
prime = isPrime(number)
if prime == number:
    print(f"{number} is a prime number.")
else:
    print(f"{number} isn't a prime number.")
end_time = time()
print(f"...Execution took {end_time-str_time} s...")

str_time = time()
strNumber, endNumber = num5, num2
primes = getPrime(strNumber, endNumber)
print(f"Found {len(primes)} prime numbers...")
#print(f"{primes}")
end_time = time()
print(f"...Execution took {round(end_time-str_time, 2)} s...")
