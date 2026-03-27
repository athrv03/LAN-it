from lanit.transfer.chunker import MAX_CHUNK_SIZE, MB, MIN_CHUNK_SIZE, next_chunk_size_from_throughput


def test_next_chunk_size_from_throughput_example():
    # 10 MB/s -> target around 10 MB chunks.
    assert next_chunk_size_from_throughput(10 * MB) == 10 * MB


def test_next_chunk_size_from_throughput_clamps_low():
    assert next_chunk_size_from_throughput(1024) == MIN_CHUNK_SIZE


def test_next_chunk_size_from_throughput_clamps_high():
    assert next_chunk_size_from_throughput(10_000 * MB) == MAX_CHUNK_SIZE
