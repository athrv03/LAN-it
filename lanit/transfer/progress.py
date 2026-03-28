import time


def _format_bytes(num_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(num_bytes)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)}{unit}"
            return f"{value:.1f}{unit}"
        value /= 1024


class ProgressBar:
    def __init__(self, total, label, width=30):
        self.total = max(1, int(total))
        self.label = label
        self.width = width
        self.start_time = time.perf_counter()

    def update(self, current):
        current = max(0, min(int(current), self.total))
        fraction = current / self.total
        filled = int(self.width * fraction)
        bar = "#" * filled + "-" * (self.width - filled)
        percent = fraction * 100
        elapsed = max(1e-9, time.perf_counter() - self.start_time)
        speed = current / elapsed
        print(
            f"{self.label} [{bar}] {percent:6.2f}% "
            f"{_format_bytes(current)}/{_format_bytes(self.total)} "
            f"{_format_bytes(speed)}/s",
            end="\r",
        )

    def finish(self):
        self.update(self.total)
        print()
