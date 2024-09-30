from typing import Dict, List

from src.widget import get_date


def filter_by_state(list_dict: List[Dict], state: "str" = "EXECUTED") -> List[Dict]:
    """Выводит список словарей в которых есть ключ state"""
    new_list_dict = list()
    for items in list_dict:
        if items.get("state") == state:
            new_list_dict.append(items)
    return new_list_dict


# if __name__ == "__main__":
#    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],state='EXECUTED' ))


def sort_by_date(lists_dict: list[dict], reverse: bool = True) -> list[dict]:
    """ "Сортирует в порядке убывания список словарей по дате"""
    return sorted(lists_dict, key=lambda dates: get_date(dates["date"]), reverse=True)


# if __name__ == '__main__':
#    print(sort_by_date())
