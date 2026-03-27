import socket

def connect(ip, port=5001):
    s = socket.socket()
    s.connect((ip, port))
    print(f"Connected to {ip}:{port}")
    return s