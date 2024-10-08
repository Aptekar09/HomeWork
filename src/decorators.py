
from typing import Optional, Callable
from functools import wraps


def log(filename: Optional[str]=None) -> Callable:
    def decorate(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
             try:
                result = func(*args, **kwargs)
                if filename:
                    result = func(*args, **kwargs)
                    log_message = f'{func.__name__} ок\n'
                    with open (filename, "a",encoding='utf-8') as file:
                        file.write(f'{log_message}')
                    return result
                else:
                    result = func(*args, **kwargs)
                    log_message = f'{func.__name__} ок\n'
                    print(f'{log_message}')
                    return result
             except Exception as e:
                if filename:
                    log_message = f'{func.__name__} error: {e.__class__.__name__} Inputs: {args}, {kwargs}\n'
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{log_message}')
                else:
                    print(f'{func.__name__} error: {e.__class__.__name__} Inputs: {args}, {kwargs}\n')

        return wrapper
    return decorate


@log()
def my_function(x, y):
    return x / y

print(my_function(1, 0))
