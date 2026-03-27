MB = 1024 * 1024
MIN_CHUNK_SIZE = 64 * 1024
MAX_CHUNK_SIZE = 16 * MB
TARGET_CHUNK_SECONDS = 1.0


def _clamp_chunk_size(size):
    return max(MIN_CHUNK_SIZE, min(MAX_CHUNK_SIZE, int(size)))


def next_chunk_size_from_throughput(throughput_bps, target_seconds=TARGET_CHUNK_SECONDS):
    if throughput_bps <= 0:
        return MB
    return _clamp_chunk_size(throughput_bps * target_seconds)


def read_chunks(file, size=MB):
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk
