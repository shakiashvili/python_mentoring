from datetime import datetime
import logging
from typing import Callable


def decorator_function_to_calculate_execution_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        time = end_time-start_time
        logging.info(f"Function name: {func.__name__} executed in time:{time}")
        return result
    return wrapper