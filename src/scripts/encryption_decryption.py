import src.libs.rsa_algo as rsa
import src.libs.dh_algo as dh

input_message = input("Enter the message: ")

public_key, private_key = rsa.get_keys()

encrypted_message = rsa.message_encryption(input_message, public_key)

print(f'Encrypted message is {rsa.message_cipher_encoding(encrypted_message)}')
print(f'Original message is {rsa.message_decryption(encrypted_message, private_key)}')

# prime & generator random numbers to be shared by the client & server
p = rsa.returnPrime(300000, 400000)
g = dh.getPsuedoRandomNumber(100000, 200000)

# client private to be generated random
clientPrivate = dh.getPsuedoRandomNumber(300000, 400000)
clientPublic = dh.getPublicKey(g, clientPrivate, p)
# print(f'prime:{p}, generator:{g}, clientPrivate{clientPrivate}, clientPublic:{clientPublic}')

serverPrivate = dh.getPsuedoRandomNumber(200000, 300000)
serverPublic = dh.getPublicKey(g, serverPrivate, p)
# print(f'prime:{p}, generator:{g}, serverPrivate{serverPrivate}, serverPublic:{serverPublic}')

serverSharedSecret = dh.getSharedSecret(clientPublic, serverPrivate, p)
# print(serverSharedSecret)
clientSharedSecret = dh.getSharedSecret(serverPublic, clientPrivate, p)
# print(clientSharedSecret)

if serverSharedSecret == clientSharedSecret:
    print(f"Shared secrets match on both sides: \nclient_shared_key:{clientSharedSecret} \nserver_shared_key:{serverSharedSecret}")
else:
    print(f"Shared secrets do not match client_shared_key:{clientSharedSecret}, server_shared_key:{serverSharedSecret}")
