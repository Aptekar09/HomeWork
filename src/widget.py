from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_cart: str) -> str:
    """Маскировка номера карты или счета"""

    if isinstance(account_cart, str) and len(account_cart) > 0:
        list_account_cart = account_cart.split()
        if 2 <= len(list_account_cart) <= 3 and list_account_cart[-1].isdigit() and list_account_cart[0].isalpha():
            part = list_account_cart[-1]
            if len(part) == 16 and len(list_account_cart) == 3:
                mask_card = get_mask_card_number(list_account_cart[-1])
                result = f"{list_account_cart[0]} {list_account_cart[1]} {mask_card}"
                return result
            elif len(part) == 20 and len(list_account_cart) == 2:
                mask_account = get_mask_account(list_account_cart[-1])
                result = f"{list_account_cart[0]} {mask_account}"
                return result
            else:
                raise ValueError("Не верный ввод")

        else:
            raise ValueError("Не верный ввод")
    else:
        raise ValueError("Не верный ввод")


if __name__ == "__main__":
    print(mask_account_card('Visa Master 7000798728906360'))


def get_date(date_num: str) -> str:
    """изменение форматы даты дня, месяца, года"""
    if isinstance(date_num, str) and len(date_num) == 26 and date_num[10:11] == "T":
        list_date_num = date_num.split("T")
        list_date = list_date_num[0].split("-")
        return f"{list_date[2]}.{list_date[1]}.{list_date[0]}"
    else:
        raise ValueError('Не корректный формат ввода')


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
