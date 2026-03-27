import os
from lanit.crypto.encryption import decrypt


def receive_file(sock):
    metadata = sock.recv(1024).decode()
    filename, filesize = metadata.split("|")
    filesize = int(filesize)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    directory = os.path.join(project_root, "FILES")
    os.makedirs(directory, exist_ok=True)
    output = os.path.join(directory, f"received_{filename}")

    with open(output, "wb") as f:
        received = 0

        while received < filesize:
            size_data = sock.recv(4)
            if not size_data:
                break

            chunk_size = int.from_bytes(size_data, "big")

            data = b""
            while len(data) < chunk_size:
                packet = sock.recv(chunk_size - len(data))
                if not packet:
                    break
                data += packet

            chunk = decrypt(data)
            f.write(chunk)
            received += len(chunk)

            print(f"{received}/{filesize} bytes", end="\r")

    print(f"\nSaved as {output}")