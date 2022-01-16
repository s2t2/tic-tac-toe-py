
import time

class Timer:
    def __init__(self):
       self.start_at = None
       self.end_at = None

    def start(self):
        self.start_at = time.perf_counter()

    def end(self):
        self.end_at = time.perf_counter()

    @property
    def duration_seconds(self):
        try:
            return round((self.end_at - self.start_at), 4)
        except:
            return None

    @property
    def duration_mins(self):
        try:
            return self.duration_seconds / 60
        except:
            return None
