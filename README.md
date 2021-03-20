## Bitcoin Merchant (BTCM)

### seed

This could literally just been some DNS entries or a hosted JSON file.

The seeds are verified merchant nodes. Anybody can create a merchant node and promote
it but to be a verified merchant you have to be trusted. There should be some sort of
minimum requirements to become a verified merchant.

### merchant node

A merchant node is a node which acts as escrow and temporary custodian of committed bitcoins
the merchant node listens to transactions from clients. It also handles commitments and withdrawls

- commitments: are when clients send funds to a merchant address in order to make microtransaction
- withdrawls: are when a client withdraws their bitcoins from the merchant address.

It is the responsibility of the merchant node to validate transaction and track balances of connected
clients.

A merchant node will basically be a SPV node (electrum) plus some code to do microtransaction
validation and balance tracking.

Merchant nodes make a small fee by charging transaction fees

### client

Clients connect to merchant nodes. In order to make micro transaction they must commit their bitcoins
into escrow into a merchant address. They can then make as many microtransactions to any clients connected
to the same merchant for free and instantly.
Once they are done making microtransactions they can then withraw their bitcoins from the merchant address.
