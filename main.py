from base64 import b64decode, b64encode
from Crypto.PublicKey.RSA import construct
from Crypto.Cipher import PKCS1_v1_5

def generate_rsa_key_to_base64(modulus, exponent, password):

    password = password.encode()

    print(f"Encoded string: {password}")

    # decode base64 string to be used as modulus(n) and exponent(e) components for
    # constructing the RSA public key object
    modulus = b64decode(modulus)
    exponent = b64decode(exponent)

    # generate bytes 4 contruction key
    n = int.from_bytes(modulus, byteorder="big")
    e = int.from_bytes(exponent, byteorder="big")

    # Generate RSA key
    pubkey = construct((n, e))
    pubkey = PKCS1_v1_5.new(pubkey)
    encrypted1 = pubkey.encrypt(password)

    print(b64encode(encrypted1))
    return b64encode(encrypted1)


if __name__ == "__main__":
    modulus = "IZzyaDQczS5LCqx+zFGPlC3w3NmvJZiz2TmOkbmgN3BoZx90sU1WU/Y0quMfvE6kBnmwsfaKPD9VwE4/w0B5vfev/N4e0RaemjB3mngMwSy/KgXZo6163xPvMAdEF/vCivDnrReJDCFqehjkTIPz+ty4YNHhjBJvLYtoeIWH72o="
    exponent = "AQAB"
    password = "hdjsaiu&22"
    generate_rsa_key_to_base64(modulus, exponent, password)
