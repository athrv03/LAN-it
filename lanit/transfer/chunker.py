def read_chunks(file, size=1024 * 1024):  # 1MB default
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk