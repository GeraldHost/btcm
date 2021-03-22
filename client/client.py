import requests
import json
import argparse
import crypto
import binascii
from hashlib import sha1

rpc_url = "http://localhost:4000/"

def request_address(public_key):
	print("[*] request address")

	payload = {
		"method": "request_address",
		"params": {"public_key":public_key},
		"jsonrpc": "2.0",
		"id": 0,
	}

	values = "".join([value for _, value in payload["params"].items()])
	signature = crypto.sign(bytes(values, encoding="utf8"))
	signature_str = binascii.unhexlify(signature).hex()

	print(values)

	payload["params"] = dict(payload["params"], **{"signature":signature_str})

	response = requests.post(rpc_url, json=payload).json()
	print(response)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Arguments')
	parser.add_argument('function')
	parser.add_argument('--method')

	args = parser.parse_args()

	if args.function == "generate_keys":
		crypto.generate_keys()
	elif args.function == "request" and args.method != None:
		public_key = crypto.public_key_from_pem()

		if args.method == "request_address":
			request_address(public_key)