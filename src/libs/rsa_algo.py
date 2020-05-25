import random

def isPrime(x):
    """
    :param x: Number which needs to be determined whether it is prime or not
    :return: True if it is prime, False otherwise
    """
    count = True
    for i in range(2,int(x/2)):
        if x % i == 0:
            count = False
            break
    return count

def returnPrime(startRange, endRange):
    """
    :param startRange: Initial range of the number
    :param endRange: End range of the number
    :return: a prime number
    """
    while True:
        num = random.randint(startRange, endRange)
        if isPrime(num):
            return num

def prime_product(prime1, prime2):
    """
    :param prime1: prime number1
    :param prime2: prime number2
    :return: product of the two prime numbers
    """
    return prime1 * prime2

def coefficient_primes(prime1, prime2):
    """
    :param prime1: prime number1
    :param prime2: prime number2
    :return: product of the two prime numbers
    """
    return (prime1 - 1) * (prime2 - 1)

def gcd(a,b):
    """
    :param a: First number
    :param b: Second number
    :return: greatest common divisor between a & b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def modulo_multiplicative_inverse(number, inv):
    """
    :param number: number for which the inverse need to be productised
    :param inv: inverse
    :return: multiplicative modulo inverse of a number under inv, if exists, -1 if doesn't exist
    """
    # This will iterate from 0 to inv-1
    for i in range(1, inv):
        # If we have our multiplicative inverse then return it
        if (number * i) % inv == 1:
            return i
    # If we didn't find the multiplicative inverse in the loop above
    # then it doesn't exist for A under M
    return -1

def getRSAParameters():
    """
    :return: n, e, d
    """
    prime1 = returnPrime(100, 200)
    prime2 = returnPrime(300, 500)

    n = prime_product(prime1, prime2)

    coeff = coefficient_primes(prime1, prime2)

    e = exponent(coeff)

    d = modulo_multiplicative_inverse(e, coeff)

    return n, e, d

def get_keys():
    n, e, d = getRSAParameters()
    public_key = (e, n)
    private_key =  (d, n)
    return public_key, private_key

def message_encoder(text_message):
    """
    :param text_message: message that needs to be encoded from text to ASCII
    :return: ASCII array
    """
    hex_string = []
    for i in range(len(text_message)):
        hex_string.append(ord(text_message[i]))
    return hex_string

def exponent(coeff):
    """
    :param coeff: coefficient of the primes
    :return: exponent required for computing the private key
    """
    for e in range(2, coeff):
        if gcd(e, coeff) == 1:
            return e


def message_cipher_encoding(ciphertext):
    """
    :param ciphertext: cipher text to be encoded
    :return: encoded value of the encrypted text
    """
    cipher_encoded_text = ""
    for item in ciphertext:
        cipher_encoded_text += chr((item % 32) + 64)

    return cipher_encoded_text

def message_encryption(message, pub_key):
    """
    :param message: message that needs to be encrypted(after encoding)
    :return: encrypted array
    """
    cipherText = []
    for encoded_item in message_encoder(message):
        cipherText.append((encoded_item ** pub_key[0]) % pub_key[1])
    return cipherText

def message_decryption(cipherText, priv_key):
    """
    :param cipherText: encrypted array
    :return: clear text
    """
    clearText = ""
    for element in cipherText:
        clearText += chr((element ** priv_key[0]) % priv_key[1])

    return clearText









