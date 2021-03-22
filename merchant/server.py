from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

import merchant
import crypto


@dispatcher.add_method
def request_address(**kwargs):
    request_str = "".join([value for key, value in kwargs.items() if key != "signature"])
    signature = kwargs["signature"]
    public_key = kwargs["public_key"]

    valid = crypto.verify_request(public_key, signature, request_str)
    print(valid)

    address = merchant.create_new_address()
    return {"address": address}


# Send transaction to other address connected to this merchant node
# transactions must provide a signature and public key for verification
@dispatcher.add_method
def send_transaction(**kwargs):
    return 0


# Find address on this network by address
@dispatcher.add_method
def find_address(**kwargs):
    return 0


# search for address by nicname
@dispatcher.add_method
def search_addresses_by_nicname(**kwargs):
    return 0


# Create nicname for address. This request must be sign by public key
# so we can verify to change
@dispatcher.add_method
def add_nicname(**kwargs):
    return 0


@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


def start():
    print("[*] Starting JSON RPC server")
    run_simple('localhost', 4000, application)
