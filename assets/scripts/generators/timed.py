from time import perf_counter
from functools import wraps
from typing import Callable


def timed(func: Callable) -> Callable:
    @wraps(func)
    def wrap(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print(f"Вызов {func.__name__:30} занял {t2- t1:.3f} секунд. ", end="")
        print(f"(Параметры {args}, {kwargs}).")
        return result
    return wrap