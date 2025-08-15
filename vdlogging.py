import os
import time
from sys import exit
from datetime import datetime

class Logging:
    """
    A simple logging class for error tracking with automatic file versioning.

    Creates timestamped log files with automatic version numbers to avoid
    overwriting existing logs.

    Example:
        >>> L = Logging("my_program")
        >>> L.log_event(404, "File not found")
        >>> L.log_event(500, "Databse connection failed")
    """

    def __init__(self, name: str, location: str = "/tmp/"):
        """
        Initialize the logger with program name and optional location.

        Args:
            name     (str): Name of the program/log file (without extension)
            location (str): Directory to store log files. Defaults to "/tmp/"

        Example:
            >>> logger = Logging("my_app", "/var/log/")
            >>> # Creates /var/log/my_app_1.log (or next available version)
        """
        self.progstart = datetime.now()
        self.location = location
        self.name = name
        self.log_path = self._get_log_version()
        # Redundant, but make sure `/tmp/` exists
        os.makedirs(self.location, exist_ok=True)

    def _get_log_version(self):
        """
        Find the next available version for the log file.

        Returns:
            str: Full path to the next available log file

        Example:
            If /tmp/myapp_1.log exists, returns /tmp/myapp_2.log
        """
        version = 1
        while True:
            filename = f"{self.name}_{version}.log"
            full_path = os.path.join(self.location, filename)
            if not os.path.exists(full_path):
                return full_path
            version += 1

    def _get_delta(self) -> str:
        """
        Get time elapsed since program start as a formatted string.

        Returns:
            str: Formatted time delta (HH:MM:SS)

        Example:
            "0:01:23" (1 minute, 23 seconds since program start)
        """
        timestamp = datetime.now() - self.progstart
        return str(timestamp).split('.')[0]

    def log_event(self, errno: int, prompt: str):
        """
        Log an error event with timestamp and error number.

        Args:
            errno (int): Error number/code for categorization
            prompt (str): Description of the error that occurred

        Example:
            >>> L = Logging("myapp")
            >>> try:
            ...     open("nonexistent.txt", "r")
            ... except FileNotFoundError as e:
            ...     L.log_event(404, f"File access failed: {e}")

        Note:
            Logs are appended to file in format:
            "[ERROR {errno} @ {timestamp}]: {prompt}"
        """
        timestamp = self._get_delta()

        try:
            with open(self.log_path, 'a') as f:
                f.write(f"[ERROR {errno} @ {timestamp}]: {prompt}\n")
        except Exception as e:
            print(f"Catastrophic Error during logging: {e}")
            exit(255)  # Catastrophic Error

# Usage examples for help():
# help(Logging)           - Shows class docstring and overview
# help(Logging.__init__)  - Shows constructor help
# help(Logging.log_event) - Shows log_event method help
#
# Quick start:
# L = Logging("prog_name")
# L.log_event(404, "File not found")
