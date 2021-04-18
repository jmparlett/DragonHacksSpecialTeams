
######################Timer##################################
import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self, running=False):
        self._start_time = None
        self.running = False

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()
        self.running = True

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        self._start_time = None
        self.running=False

    def getElaspedTime(self):
      elapsed_time = time.perf_counter() - self._start_time
      return elapsed_time

    def __str__(self):
      elapsed_time = time.perf_counter() - self._start_time
      return str(elapsed_time)

    def getStatus(self):
      '''returns true if running false otherwise'''
      return self.running