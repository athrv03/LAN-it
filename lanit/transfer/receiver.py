import os
from lanit.crypto.encryption import decrypt


def _recv_exact(sock, size):
    data = b""
    while len(data) < size:
        chunk = sock.recv(size - len(data))
        if not chunk:
            raise ConnectionError("Connection closed while receiving data")
        data += chunk
    return data


def receive_file(sock):
    metadata_size = int.from_bytes(_recv_exact(sock, 4), "big")
    metadata = _recv_exact(sock, metadata_size).decode("utf-8")
    filename, filesize = metadata.split("|")
    filesize = int(filesize)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    directory = os.path.join(project_root, "FILES")
    os.makedirs(directory, exist_ok=True)
    output = os.path.join(directory, f"received_{filename}")

    with open(output, "wb") as f:
        received = 0

        while received < filesize:
            chunk_size = int.from_bytes(_recv_exact(sock, 4), "big")
            data = _recv_exact(sock, chunk_size)

            chunk = decrypt(data)
            f.write(chunk)
            received += len(chunk)

            print(f"{received}/{filesize} bytes", end="\r")

    print(f"\nSaved as {output}")
