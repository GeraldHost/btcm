import requests
import json
import argparse
import crypto

rpc_url = "http://localhost:4000/"

def request_address():
	print("[*] request address")
	payload = {
		"method": "request_address",
		"params": [],
		"jsonrpc": "2.0",
		"id": 0,
	}

	response = requests.post(rpc_url, json=payload).json()
	print(response)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Arguments')
	parser.add_argument('--method', help='sum the integers (default: find the max)')

	args = parser.parse_args()

	if args.method == "request_address":
		request_address()
	elif args.method == "generate_keys":
		crypto.generate_keys()
	elif args.method == "load_keys":
		crypto.load_keys()