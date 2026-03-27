import socket

PORT = 9999
RESPONSE = "LANIT_DEVICE"


def discover():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(2)

    sock.sendto(b"DISCOVER_LANIT", ("255.255.255.255", PORT))

    devices = []

    try:
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode()

            if message.startswith(RESPONSE):
                name = message.split(":")[1]
                devices.append((name, addr[0]))
    except:
        pass

    return devices


def respond(device_name="LAN-it Device"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        if data == b"DISCOVER_LANIT":
            response = f"{RESPONSE}:{device_name}"
            sock.sendto(response.encode(), addr)