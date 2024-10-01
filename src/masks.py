def get_mask_card_number(cart_nums: str) -> str:
    """Маскировка номера карты"""
    if len(cart_nums) != 16:
        raise ValueError("Не корректный номер карты")
    if cart_nums.isdigit():
        mask_card = f"{cart_nums[0:4]} {cart_nums[4:6]}** **** {cart_nums[12:]}"
        return mask_card
    else:
        raise ValueError("Необходимо ввести цифры")


if __name__ == "__main__":
  print(get_mask_card_number("1234567896541237"))


def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета"""

    if isinstance(account_number, str) and len(account_number) == 20 and account_number.isdigit():
            mask_account = f"**{account_number[-4:]}"
            return mask_account
    else:
        raise ValueError('Не верный ввод')


if __name__ == "__main__":
    print(get_mask_account(12345612547896255228))
