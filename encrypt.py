import rsa

def generate_key_pair():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as f:
        f.write(key.save_pkcs1())

def load_key_from_file(filename):
    # Load a private key from a file in PEM format
    with open(filename, 'rb') as f:
        key_data = f.read()
        key = rsa.PrivateKey.load_pkcs1(key_data)
        return key
    
def load_pkey_from_file(filename):
    # Load a public key from a file in PEM format
    with open(filename, 'rb') as f:
        key_data = f.read()
        key = rsa.PublicKey.load_pkcs1(key_data)
        return key

def encrypt_file(input_file, output_file, public_key):
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = rsa.encrypt(data, public_key)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

# ENABLE THE FOLLOWINGS IF THERE IS NO EXISTING KEYS
# 1. Generate a key pair
public_key, private_key = generate_key_pair()
# 2. Save the keys to files
save_key_to_file(public_key, 'public_key.pem')
save_key_to_file(private_key, 'private_key.pem')

public_key = load_pkey_from_file('public_key.pem')
# private_key = load_key_from_file('private_key.pem')

# encrypt_file('input.txt', 'encrypted_file.txt', public_key)
# encrypt_file('input.zip', 'encrypted_file.zip', public_key) # works
# encrypt_file('input.txt', 'input.txt', public_key) # works
# encrypt_file('source/*.txt', 'source/*.txt', public_key) # NOK
