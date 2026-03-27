import os
import time

from lanit.transfer.chunker import MB, next_chunk_size_from_throughput
from lanit.crypto.encryption import encrypt


def send_file(sock, path):
    file_size = os.path.getsize(path)
    filename = os.path.basename(path)
    chunk_size = MB
    throughput_estimate = None

    # send metadata
    sock.sendall(f"{filename}|{file_size}".encode())

    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            encrypted = encrypt(chunk)

            start = time.perf_counter()
            sock.sendall(len(encrypted).to_bytes(4, "big"))
            sock.sendall(encrypted)
            elapsed = time.perf_counter() - start

            if elapsed > 0:
                sample_throughput = len(chunk) / elapsed
                if throughput_estimate is None:
                    throughput_estimate = sample_throughput
                else:
                    # Keep chunk-size changes stable with a simple EWMA.
                    throughput_estimate = (0.7 * throughput_estimate) + (0.3 * sample_throughput)
                chunk_size = next_chunk_size_from_throughput(throughput_estimate)

    print("File sent successfully")
