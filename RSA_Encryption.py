import random
import math
import ctypes
import time

# Load the C library
encryptionMath = ctypes.CDLL('/home/brady/Programs/Personal/SteganographyC/Steganography/encryptionMath.so')

# Seed the random number generator in the C library
encryptionMath.seed_random()

# Define argument and return types for the C functions
encryptionMath.generate_prime.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
encryptionMath.generate_prime.restype = ctypes.c_longlong
encryptionMath.mod_inverse.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
encryptionMath.mod_inverse.restype = ctypes.c_longlong

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

# GENERATING A RANDOM PRIME NUMBER IN A GIVEN RANGE USING THE PYTHON FUNCTION
def generate_prime_python(min_value, max_value):
    primes = sieve_of_eratosthenes(max_value)
    primes_in_range = [p for p in primes if p >= min_value]
    return random.choice(primes_in_range)

# USING THE EXTENDED EUCLIDEAN ALGORITHM TO CALCULATE THE MODULAR INVERSE IN PYTHON
def mod_inverse_python(a, m):
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

# GENERATING A RANDOM PRIME NUMBER IN A GIVEN RANGE USING THE C FUNCTION
def generate_prime_c(min_value, max_value):
    return encryptionMath.generate_prime(min_value, max_value)

# USING THE C FUNCTION TO CALCULATE THE MODULAR INVERSE
def mod_inverse_c(a, m):
    return encryptionMath.mod_inverse(a, m)

#------------------- End Of HELPER FUNCTIONS-------------------#

#------------------- RSA ENCRYPTION IMPLEMENTATION-------------------#
# n and e are the public key components, d and n is the private key component
# Returns public key then private key
def generate_keys():
    p, q = generate_prime_c(1000000, 5000000), generate_prime_c(1000000, 5000000)
    d = mod_inverse_c(65537, (p - 1) * (q - 1))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537 
    if math.gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime, choose different primes")
    return {"n":n,"e":e},{'n':n,'d':d}

# Encrypts a message using the public key
def encrypt(message, public_key):
    n = public_key['n']
    e = public_key['e']
    # converting the message to bytes
    encoded_message = message.encode('utf-8')
    # converting bytes to integers and encrypting
    encrypted_message = [pow(int.from_bytes(encoded_message[i:i+1], 'big'), e, n) for i in range(len(encoded_message))]
    return encrypted_message

# Decrypts a message using the private key
def decrypt(ciphertext, private_key):
    n = private_key['n']
    d = private_key['d']
    # decrypting the message using the private key
    decrypted_message = [pow(char, d, n) for char in ciphertext]
    # converting large integers to bytes and then decoding them
    decoded_message = b''.join([int.to_bytes(char, (char.bit_length() + 7) // 8, 'big') for char in decrypted_message])
    return decoded_message.decode('utf-8', errors='ignore')

#------------------- End Of RSA ENCRYPTION IMPLEMENTATION-------------------#

#------------------- EXAMPLE USAGE-------------------#

#------------------- End Of EXAMPLE USAGE-------------------#

