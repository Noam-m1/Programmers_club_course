import hashlib

def correct_password(encrypted_password):
    decrypted_password = ""
    for i in range(1000000000):
        password = f"{i:06d}"
        if encrypted_password == hashlib.md5(password.encode()).hexdigest():
            decrypted_password = password
    return decrypted_password       

print(correct_password("3cc6520a6890b92fb55a6b3d657fd1f6"))        