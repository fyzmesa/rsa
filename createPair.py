import rsa
from base64 import b64encode, b64decode

# print("1. Creation of encryption pair of keys")
public_key, private_key = rsa.newkeys(2048)

public_pem = public_key.save_pkcs1().decode()
print("\nPublic key:\n", public_pem)
private_pem = private_key.save_pkcs1().decode()
print("\nPrivate key:\n", private_pem)
