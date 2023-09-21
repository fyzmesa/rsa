import rsa

def load_key_from_file(filename):
    with open(filename, 'rb') as f:
        key_data = f.read()
        key = rsa.PrivateKey.load_pkcs1(key_data)
        return key

def decrypt_file(input_file, output_file, private_key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = rsa.decrypt(encrypted_data, private_key)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

private_key = load_key_from_file('private_key.pem')

decrypt_file('encrypted_file.txt', 'decrypted_file.txt', private_key)
# decrypt_file('encrypted_file.zip', 'decrypted_file.zip', private_key)
