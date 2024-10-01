import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_dicts() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state(list_dicts: list[dict], state: str ="EXECUTED") -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(list_dicts, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "list_dict, state, expected",
    [
        ([], "EXECUTED", []),
        ([{"id": 41428829, "state": "EXECUT", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED", []),
        (
            [{"id": 41428829, "state": "PEDING", "date": "2019-07-03T18:35:29.512364"}],
            "PEDING",
            [{"id": 41428829, "state": "PEDING", "date": "2019-07-03T18:35:29.512364"}],
        ),
    ],
)
def test_filter_by_state_invalide(list_dict: list[dict], state: str, expected: list[dict]) -> None:
    """Параметризация тестов для различных возможных значений статуса state,
           Проверка работы функции при отсутствии словарей с указанным статусом
    state в списке."""
    assert filter_by_state(list_dict, state) == expected


@pytest.fixture
def dict_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date(dict_date: list[dict]) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""
    assert sort_by_date(dict_date, reverse=True) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "lists_dict, expected",
    [
        ([], []),
        (
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_sort_by_date_invalid(lists_dict: list[dict], expected: list[dict]) -> None:
    """Проверка на пустой список одинаковые даты"""
    assert sort_by_date(lists_dict, reverse=True) == expected
