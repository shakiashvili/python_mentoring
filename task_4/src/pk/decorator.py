from datetime import datetime
from pk.logger import log_info
from typing import Callable


def decorator_function(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        time = end_time-start_time
        log_info(f"Function name: {func.__name__} executed in time: {time}")
        return result
    return wrapper