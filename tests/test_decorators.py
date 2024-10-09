from typing import Any

import pytest

from src.decorators import log


@log()
def test_log(capsys: Any) -> None:
    """Тестируем декоратор @log на корректность вывода в консоль с помощью фикстуры capsys и тест на ошибку """
    my_function()
    captured = capsys.readouterr()
    assert captured.out == "my_function ок\n\n"
    assert result == 2

    with pytest.raises(Exception, match="my_function error: ZeroDivisionError Inputs: (1, 0), {}"):
        my_function()


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> Any:
    return x / y


result = my_function(4, 2)
assert result == 2
