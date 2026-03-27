import socket
import threading
from lanit.discovery.broadcast import respond


def start_server(port=5001):
    # Start discovery responder in background
    threading.Thread(target=respond, daemon=True).start()

    s = socket.socket()
    s.bind(("0.0.0.0", port))
    s.listen(1)

    print(f"LAN-it listening on port {port}")

    conn, addr = s.accept()
    print(f"Connected from {addr}")

    return conn