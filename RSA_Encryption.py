import random
import time
import math

#--------------------- HELPER FUNCTIONS---------------------#

# GENERATING PRIME NUMBERS USING THE SIEVE OF ERATOSTHENES ALGORITHM
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]
# GENERATING A RANDOM PRIME NUMBER IN A GIVEN RANGE USING THE SIEVE OF ERATOSTHENES ALGORITHM
def generate_prime(min_value, max_value):
    primes = sieve_of_eratosthenes(max_value)
    primes_in_range = [p for p in primes if p >= min_value]
    return random.choice(primes_in_range)
# USING THE EXTENDED EUCLIDEAN ALGORITHM TO CALCULATE THE MODULAR INVERSE
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

#------------------- End Of HELPER FUNCTIONS-------------------#

# n and e are the public key components, d and n is the private key component
# Returns public key then private key
def generate_keys():
    p, q = generate_prime(1000000, 5000000), generate_prime(1000000, 5000000)
    n = p * q
    phi = (p - 1) * (q - 1)
    #65537 is a common value for e in practice because it makes the encryption faster and is secure
    #I left it as a interchangable value in the function for the sake of flexibility 
    e = 65537 
    if math.gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime, choose different primes")
    d = mod_inverse(e, phi)
    return {"n":n,"e":e},{'n':n,'d':d}
def encrypt(message, public_key):
    n = public_key['n']
    e = public_key['e']
    encoded_message = [ord(char) for char in message]
    return [pow(char, e, n) for char in encoded_message]
def decrypt(ciphertext, private_key):
    n = private_key['n']
    d = private_key['d']
    decrypted_message= [pow(char, d, n) for char in ciphertext]
    return ''.join([chr(char) for char in decrypted_message])


public_key, private_key = generate_keys()
encrypted_message = encrypt("Hello, World!", public_key)
decrypted_message = decrypt(encrypted_message, private_key)
print(decrypted_message)

