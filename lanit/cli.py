import sys
from lanit.discovery.broadcast import discover
from lanit.network.client import connect
from lanit.transfer.sender import send_file
from lanit.network.server import start_server
from lanit.transfer.receiver import receive_file
from lanit.crypto.encryption import init_cipher


def run():
    if len(sys.argv) < 2:
        print("Usage: lanit [discover|send|receive]")
        return

    cmd = sys.argv[1]

    if cmd == "discover":
        devices = discover()
        for i, (name, ip) in enumerate(devices):
            print(f"[{i}] {name} ({ip})")

    elif cmd == "send":
        if len(sys.argv) < 5:
            print("Usage: lanit send <ip> <file> <password>")
            return

        ip = sys.argv[2]
        path = sys.argv[3]
        password = sys.argv[4]

        init_cipher(password)

        sock = connect(ip)
        send_file(sock, path)

    elif cmd == "receive":
        if len(sys.argv) < 3:
            print("Usage: lanit receive <password>")
            return

        password = sys.argv[2]

        init_cipher(password)

        conn = start_server()
        receive_file(conn)

    else:
        print("Unknown command")