import ecdsa
import binascii

def generate_keys():
	print("[*] generate new keys")
	sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) # private key
	vk = sk.verifying_key # public key

	with open("private.pem", "wb") as f:
		f.write(sk.to_pem())

	with open("public.pem", "wb") as f:
		f.write(vk.to_pem())

def sign(string):
	print("[*] load keys")
	with open("private.pem") as f:
		sk = ecdsa.SigningKey.from_pem(f.read())
	signature = sk.sign(string)
	return binascii.hexlify(signature)

def public_key_from_pem():
	with open("public.pem") as f:
		vk = ecdsa.VerifyingKey.from_pem(f.read())
	return vk.to_string().hex()
	