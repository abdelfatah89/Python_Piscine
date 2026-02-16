from typing import Any


def decorator(func: callable) -> callable:
    def enhanced_func(*arg, **kwarg) -> Any:
        # code ...
        result = func(*arg, **kwarg)
        # code ...
        return result
    return enhanced_func
