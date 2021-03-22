import os
import asyncio

from electrum.simple_config import SimpleConfig
from electrum import constants
from electrum.daemon import Daemon
from electrum.wallet import create_new_wallet
from electrum.util import create_and_start_event_loop

loop, stopping_fut, loop_thread = create_and_start_event_loop()
config = SimpleConfig({"testnet":
                       True})  # to use ~/.electrum/testnet as datadir
constants.set_testnet()  # to set testnet magic bytes

daemon = Daemon(config, listen_jsonrpc=False)
network = daemon.network
assert network.asyncio_loop.is_running()

wallet_dir = os.path.dirname(config.get_wallet_path())
wallet_path = os.path.join(wallet_dir, "test_wallet")
if not os.path.exists(wallet_path):
    create_new_wallet(path=wallet_path, config=config)
# open wallet
wallet = daemon.load_wallet(wallet_path,
                            password=None,
                            manual_upgrades=False)
wallet.start_network(network)


def create_new_address():
    return wallet.create_new_address(False)


def stop_electrum():
    stopping_fut.set_result(1)
