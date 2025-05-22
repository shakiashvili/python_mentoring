from datetime import datetime


def decorator_func(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        time = end_time - start_time
        return time
    # print to get the time logged into console
    return wrapper
