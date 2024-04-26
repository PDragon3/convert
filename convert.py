import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256


def generate_key_from_int(int_key):
    key_str = str(int_key).encode()
    hasher = SHA256.new(key_str)
    return hasher.digest()


def cypher(cypher_key, plain_message):
    key = generate_key_from_int(cypher_key)
    data = plain_message.encode()
    data = pad(data, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(data)
    iv = cipher.iv
    return iv + ct_bytes


def decypher(cypher_key, cyphered_message):
    key = generate_key_from_int(cypher_key)
    iv = cyphered_message[:AES.block_size]
    ct = cyphered_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mode = int(sys.argv[1])
        input_key = int(sys.argv[2])
        message = sys.argv[3]
    else:
        mode = int(input("1 for cypher, 2 for decypher: "))
        input_key = int(input("Key : "))
        message = input("Message: ")

    if mode == 1:
        encrypted = cypher(input_key, message)
        print(encrypted.hex())
    elif mode == 2:
        encrypted_data = bytes.fromhex(message)
        try:
            print(decypher(input_key, encrypted_data))
        except:
            print("Wrong key or message.")
