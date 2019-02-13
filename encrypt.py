import math
import random
import sys


# pgcd method
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# test if a number is prime or not


def is_prime(n):
    if n > 1:
        if n == 0:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    else:
        print("nombre invalide")

# get all the prime numbers under 50


def get_primes():
    primes = list()
    for i in range(2, 50):
        if is_prime(i):
            primes.append(i)
    return primes

# generate a random prime number under 100


def get_random_prime():
    r = random.randint(0, len(get_primes()))
    return get_primes()[r]

# calcluate n and phy


def get_phy_n():
    p = get_random_prime()
    q = get_random_prime()
    while(p == q):
        p = get_random_prime()
        q = get_random_prime()
    n = p*q
    phy = (p-1)*(q-1)
    return [phy, n]


# calculate d
def get_d(e,  phy):
    e = e % phy
    for d in range(1, phy):
        if (e*d) % phy == 1:
            return d

# calculate e


def get_e(phy):
    if (phy > 2):
        e = random.randint(1, phy)
        g = gcd(phy, e)
        while g != 1:
            e = random.randint(1, phy)
            g = gcd(phy, e)
        return e

msg = str(sys.argv[1])

# switch to ascii code
def get_ascii(message):
    ascii_ = list()
    for i in range(0, len(message)):
        ascii_.append(ord(message[i]))
    return ascii_

# crypter the message


def crypter(code_ascii, N, E):
    n=int(N)
    e=int(E)
    crypted = list()
    message = str()
    for i in range(0, len(code_ascii)):
        cry = int((code_ascii[i] ** e) % n)
        crypted.append(cry)
        message += str(cry)
    return crypted


# variables
values = get_phy_n()
phy_n = values[0]
n = values[1]
e = get_e(phy_n)
d = get_d(e, phy_n)

print("public key : ("+str(n)+","+str(e)+")")
print("private key : ("+str(n)+","+str(d)+")")

print(crypter(get_ascii(msg),n,e))

sys.stdout.flush()