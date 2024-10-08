import pytest

from src.decorators import log

def test_log(capsys):
    @log()
    def my_function(x, y):
        return x / y

    result = my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ок\n\n'
    assert result == 2

@log()
def my_function():
    with pytest.raises(Exception, match='my_function error: ZeroDivisionError Inputs: (1, 0), {}'):
        my_function()

@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

result = my_function(4, 2)
assert result == 2

