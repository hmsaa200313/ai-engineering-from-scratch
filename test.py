from sys import argv
from math import gcd

print("2 is prime")
primes = [2]
n = 3
while n <= int(argv[1]):
    is_prime = True
    for k in primes:
        if n % k == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
        print(f"{n} is prime")
    n += 2
