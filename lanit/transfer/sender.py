import os
from lanit.transfer.chunker import read_chunks
from lanit.crypto.encryption import encrypt


def send_file(sock, path):
    file_size = os.path.getsize(path)
    filename = os.path.basename(path)

    # send metadata
    sock.sendall(f"{filename}|{file_size}".encode())

    with open(path, "rb") as f:
        for chunk in read_chunks(f):
            encrypted = encrypt(chunk)

            sock.sendall(len(encrypted).to_bytes(4, "big"))
            sock.sendall(encrypted)

    print("File sent successfully")