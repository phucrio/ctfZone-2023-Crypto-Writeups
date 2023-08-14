from base64 import b64encode,b64decode
from Crypto.Util.number import long_to_bytes

enc_flag = "hOtHc2dafgWuv2nHQDGsoGoF+BmDhy3N0seYgY9kVnw="
d = 666346744999699025106284944294484928784936011745983290828277785363873598714
import base64
import hashlib

def decrypt(enc, priv):
    res = bytearray()
    data = base64.b64decode(enc)
    st = hashlib.sha256(priv).digest()
    for i, b in enumerate(data):
        res.append(b ^ st[i])
    return res

# Example usage:
enc_flag = "hOtHc2dafgWuv2nHQDGsoGoF+BmDhy3N0seYgY9kVnw="
key = b"AXkjjnNPqO/Mu8Tv6wdl8iCLC9CX6CKOOi1X3cktDPo="
print(decrypt(enc_flag, b64decode(key)).decode())
