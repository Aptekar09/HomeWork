from collections.abc import Iterator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def list_dict():
    """ Фикстура"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def test_filter_by_currency(list_dict, currency="USD"):
    """тест на корректность работы"""
    generator = filter_by_currency(list_dict, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.mark.parametrize("list_dict, currency, expected", [([{}], "USD", ValueError), ([], "USD", ValueError)])
def test_fiter_by_currency_invalid(list_dict, currency, expected):
    """Тест на некорректный ввод"""
    generator = filter_by_currency(list_dict, "USD")
    with pytest.raises(expected):
        next(generator)


@pytest.mark.parametrize(
    "list_dict, expect",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "EUR"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            "Перевод организации",
        )
    ],
)
def test_transaction_descriptions(list_dict, expect):
    """Тест на корректность работы"""
    generator = transaction_descriptions(list_dict)
    assert next(generator) == expect


@pytest.mark.parametrize(
    "starts, end, expected", [(10, 11, "0000 0000 0000 0010"), (1000, 100005, "0000 0000 0000 1000")]
)
def test_card_number_generator(starts, end, expected):
    """Тест на корректность работы функции"""
    generator = card_number_generator(starts, end)
    assert next(generator) == expected


def test_cart_number_generator_invalid():
    """Тестирование на не корректный ввод"""
    generator = card_number_generator(0, 0)
    with pytest.raises(ValueError):
        next(generator)
