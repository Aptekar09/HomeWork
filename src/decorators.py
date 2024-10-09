from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который автоматически регистрирует детали выполнения функций,
 результат выполнения и информация об ошибках, передает в файл или выводит на консоль если файла нет"""
    def decorate(func: Any) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    result = func(*args, **kwargs)
                    log_message = f"{func.__name__} ок\n"
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{log_message}")
                    return result
                else:
                    result = func(*args, **kwargs)
                    log_message = f"{func.__name__} ок\n"
                    print(f"{log_message}")
                    return result
            except Exception as e:
                if filename:
                    log_message = f"{func.__name__} error: {e.__class__.__name__} Inputs: {args}, {kwargs}\n"
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{log_message}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__} Inputs: {args}, {kwargs}\n")

        return wrapper

    return decorate


@log()
def my_function(x: int, y: int) -> Any:
    return x / y


print(my_function(1, 0))
