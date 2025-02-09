#! /usr/bin/env python
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

key = b'wusnxhdyshdksiwy'
mode = AES.MODE_ECB
encryptor = AES.new(key, mode)


def encrypt(plaintext):
    while len(plaintext) % 16 != 0:
        n = 0
        n += 1
        plaintext += '\x00' * n

    cipher = encryptor.encrypt(plaintext.encode('utf-8'))
    return b2a_hex(cipher).decode('utf-8')


def decrypt(ciphertext):
    plain1 = encryptor.decrypt(a2b_hex(ciphertext))
    plain = plain1.rstrip(b'\x00')
    return plain.decode('utf-8')


if __name__ == '__main__':
    # code = encrypt('ITSF_vmware$1988')
    code = "59b1dfb13f1e87573de8bb3c8a951ab1"
    print(code)
    print(decrypt(code))