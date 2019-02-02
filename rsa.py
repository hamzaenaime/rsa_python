import math
import random
import sys

# array of primes numbers


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


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


def get_primes():
    primes = list()
    for i in range(2, 100):
        if is_prime(i):
            primes.append(i)
    return primes


def get_random_prime():
    r = random.randint(0, len(get_primes()))
    return get_primes()[r]


def get_phy_n():
    p = get_random_prime()
    q = get_random_prime()
    while(p == q):
        p = get_random_prime()
        q = get_random_prime()
    n = p*q
    phy = (p-1)*(q-1)
    return [phy, n]


def get_d(e,  phy):
    e = e % phy
    for d in range(1, phy):
        if (e*d) % phy == 1:
            return d


def get_e(phy):
    if (phy > 2):
        e = random.randint(1, phy)
        g = gcd(phy, e)
        while g != 1:
            e = random.randint(1, phy)
            g = gcd(phy, e)
        return e


def get_ascii(message):
    ascii_ = list()
    for i in range(0, len(message)):
        ascii_.append(ord(message[i]))
    return ascii_


values = get_phy_n()
phy_n = values[0]
n = values[1]
e = get_e(phy_n)
d = get_d(e, phy_n)

# public key (n,e)
# private ke (n,d)
# msg = int(75)
# print("message is : ", msg)
# cry = int((msg ** e) % n)
# print("message crypred is : ", cry)
# decry = int((cry ** d) % n)
# print("message decrypred is : ", decry)

message = raw_input("Enter Your Message : ")


def crypter(code_ascii, n, e):
    crypted = list()
    for i in range(0, len(code_ascii)):
        cry = int((code_ascii[i] ** e) % n)
        crypted.append(cry)
    print("cryptage end")
    return crypted


def decrypter(crypt, n, d):
    decrypt = list()
    for i in range(0, len(crypt)):
        decry = int((crypt[i] ** d) % n)
        decrypt.append(chr(decry))
    print("decryptage end")
    return decrypt


ascii_ = get_ascii(message)
crypt = crypter(ascii_, n, e)
decrypt = decrypter(crypt, n, d)
for c in range(0, len(decrypt)):
    print(decrypt[c])
