import ecdsa
import binascii

# signature = sk.sign(b"message")
# assert vk.verify(signature, b"message")

def generate_keys():
	print("[*] generate new keys")
	sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) # private key
	vk = sk.verifying_key # public key

	with open("private.pem", "wb") as f:
		f.write(sk.to_pem())

	with open("public.pem", "wb") as f:
		f.write(vk.to_pem())

def load_keys():
	print("[*] load keys")
	with open("private.pem") as f:
		sk = ecdsa.SigningKey.from_pem(f.read())
	signature = sk.sign(b"message")
	print(f"Signature: {binascii.hexlify(signature)}")
	