import sys
from ppadb.client import Client as AdbClient

def connect_device():
    try:
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        
        if not devices:
            print("No devices found. Activate Bluetooth debugging or connect phone wirelessly.")
            input("Do you want to connect your phone over wireless debugging? [y/n]")
            if input == y