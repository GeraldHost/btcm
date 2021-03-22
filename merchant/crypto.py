# Every request that comes into the merchant node must be signed
# by the address making the request.
import ecdsa
from hashlib import sha256


def verify_request(public_key, signature, request_str):
    vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key),
                                        curve=ecdsa.SECP256k1)
    return vk.verify(bytes.fromhex(signature), bytes(request_str, encoding="utf8"))
