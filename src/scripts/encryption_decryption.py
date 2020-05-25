import src.libs.rsa_algo as rsa

input_message = input("Enter the message: ")

public_key, private_key = rsa.get_keys()

encrypted_message = rsa.message_encryption(input_message, public_key)

print(f'Encrypted message is {rsa.message_cipher_encoding(encrypted_message)}')
print(f'Original message is {rsa.message_decryption(encrypted_message, private_key)}')