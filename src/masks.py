def get_mask_card_number(cart_nums: str) -> str:
    """Маскировка номера карты"""
    mask_card = f"{cart_nums[0:4]} {cart_nums[4:6]}** **** {cart_nums[12:]}"
    return mask_card


#if __name__ == "__main__":
  #  print(get_mask_card_number("1234567896541236"))


def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета"""
    mask_account = f"**{account_number[-4:]}"
    return mask_account


#if __name__ == "__main__":
  #  print(get_mask_account("12547896255222"))
def get_mask_accoun():
    return None