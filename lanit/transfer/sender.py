import os
import time

from lanit.transfer.chunker import MB, next_chunk_size_from_throughput
from lanit.crypto.encryption import encrypt
from lanit.transfer.progress import ProgressBar


def send_file(sock, path):
    file_size = os.path.getsize(path)
    filename = os.path.basename(path)
    chunk_size = MB
    throughput_estimate = None

    # Send metadata as length-prefixed UTF-8 so binary payload bytes
    # cannot be accidentally parsed as text on the receiver side.
    metadata = f"{filename}|{file_size}".encode("utf-8")
    sock.sendall(len(metadata).to_bytes(4, "big"))
    sock.sendall(metadata)

    progress = ProgressBar(file_size, "Sending")

    with open(path, "rb") as f:
        sent = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            encrypted = encrypt(chunk)

            start = time.perf_counter()
            sock.sendall(len(encrypted).to_bytes(4, "big"))
            sock.sendall(encrypted)
            elapsed = time.perf_counter() - start

            sent += len(chunk)
            progress.update(sent)

            if elapsed > 0:
                sample_throughput = len(chunk) / elapsed
                if throughput_estimate is None:
                    throughput_estimate = sample_throughput
                else:
                    # Keep chunk-size changes stable with a simple EWMA.
                    throughput_estimate = (0.7 * throughput_estimate) + (0.3 * sample_throughput)
                chunk_size = next_chunk_size_from_throughput(throughput_estimate)

    progress.finish()
    print("File sent successfully")
