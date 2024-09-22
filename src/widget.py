from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_cart: str) -> str:
    """Маскировка номера карты или счета"""

    list_account_cart = account_cart.split()
    part = list_account_cart[-1]
    if len(part) == 16:
        mask_card = get_mask_card_number(list_account_cart[-1])
        result = f"{list_account_cart[0]} {list_account_cart[1]} {mask_card}"
    else:
        mask_account = get_mask_account(list_account_cart[-1])
        result = f"{list_account_cart[0]} {mask_account}"
    return result


# if __name__ == "__main__":
# print(mask_account_card('Visa Platinum 70007922896063611'))


def get_date(date_num: str) -> str:
    """изменение форматы даты дня, месяца, года"""
    list_date_num = date_num.split("T")
    list_date = list_date_num[0].split("-")
    return f"{list_date[2]}.{list_date[1]}.{list_date[0]}"


# if __name__ == "__main__":
# print(get_date("2024-03-11T02:26:18.671407"))
