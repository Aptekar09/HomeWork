from typing import Optional


def log(filename: Optional[str]):
    def decorate(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                if filename:
                    with open (filename, "a",encoding='utf-8') as file:
                        file.write(f'{func.__name__} ок')
                else:
                    print(f'{func.__name__} ок')
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {e.__class__.__name__} Inputs: {args}, {kwargs}')
                else:
                    print(f'{func.__name__} error: {e.__class__.__name__} Inputs: {args}, {kwargs}')

        return wrapper
    return decorate


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(1, 2))
