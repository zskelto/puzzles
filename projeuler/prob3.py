'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
6857
'''
import math

def isPrime(num):
    for i in range(2,math.floor(num/2)):
        if num%i==0:
            return False

    return True

def primeSieve(sieveSize):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieveSize
    sieve[0] = False # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

     # compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes


def prob3(num):
    i = math.floor(math.sqrt(num))+1
    nums = primeSieve(i)
    ans = -1

    for i in nums:
        print(i)
        if isPrime(i):
            if num%i==0:
                ans = i

    return ans

def prob3a(num):
    for i in range(2,int(math.sqrt(num))):
        if num%i==0:
            if isPrime(i):
                print(i)

prob3a(600851475143)
