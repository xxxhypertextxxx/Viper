# Databases
# Version 1.0

import binascii

test = {
    "name": "Jeff",
    "password": "nope"
}


def createdatabase(dinput, filepath, key=None, encoding="utf-8"):
    """
    Takes in a dictionary and scrambles it, turning it into a database.
    It will then write that data to a file.
    """
    if key is not None:
        bits = bin(int(binascii.hexlify(str(dinput).encode(encoding)), 16))[2:]
        if str(key) == "reverse":
            # bits = bits[::-1]
            x = None
        with open(filepath + ".vidb", "w") as wt:
            wt.write(bits.zfill(8 * ((len(bits) + 7) // 8)))
    else:
        with open(filepath + ".vidb", "w") as wt:
            wt.write(str(dinput))


def decrypt(fpath, key=None, encoding='utf-8', errors='surrogatepass'):
    with open(fpath + ".vidb", "r") as de:
        re = de.read()
        if str(key) == "reverse":
            # re = re[::-1]
            x = None
        print(re)
        re = int(re, 2)
        print(re)
        print(re.to_bytes((re.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0')
