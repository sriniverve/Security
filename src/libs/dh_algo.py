import src.libs.rsa_algo as rs
import random

def getPsuedoRandomNumber(startRange, endRange):
    """
    :param startRange: Initial range of the number
    :param endRange: End range of the number
    :return: psuedorandom number
    """
    return random.randint(startRange, endRange)

def getPublicKey(generator, privateKey, prime):
    """
    :param generator:
    :param private: private key chosen by the entity
    :param prime: Prime number
    :return: public key
    """
    return ((generator ** privateKey) % prime)

def getSharedSecret(pubicKey, privateKey, prime):
    """
    :param pubicKey: public key
    :param privateKey: private key chosen by the entity
    :param prime: prime number
    :return: shared secret from the computation
    """
    return ((pubicKey ** privateKey) % prime)


