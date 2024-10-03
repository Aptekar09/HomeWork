import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def nums_1() -> str:
    return "Visa Platinum 7000792289606361"


def test_mask_account_card(nums_1: str) -> None:
    assert mask_account_card(nums_1) == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize(
    "account_cart, expected",
    [
        ("", ValueError),
        ("f", ValueError),
        (1234, ValueError),
        ("hhhhh jjjj 8787879", ValueError),
        ("Visa 7000792289606361", ValueError),
    ],
)
def test_mask_account_card_invalid(account_cart: str, expected: type[ValueError]) -> None:
    with pytest.raises(expected):
        mask_account_card(account_cart)


@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(date: str) -> None:
    """Тестирование правильности преобразования даты."""
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize(
    "date_num, expected",
    [
        ("", ValueError),
        ("2024-03-11T02", ValueError),
        ("20240311D022618671407", ValueError),
        ("jhghjguyuyujkhjkgjhgjhgj", ValueError),
    ],
)
def test_get_date_invalid(date_num: str, expected: type[ValueError]) -> None:
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
    Проверка работы функции на различных входных форматах даты,
    включая граничные случаи и нестандартные строки с датами.
    """
    with pytest.raises(expected):
        get_date(date_num)
