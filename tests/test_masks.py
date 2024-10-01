import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def nums_1():
    return "1234567890123456"


def test_get_mask_card_number(nums_1):
    assert get_mask_card_number(nums_1) == '1234 56** **** 3456'
    with pytest.raises(ValueError):
        get_mask_card_number('123')
    with pytest.raises(ValueError):
        get_mask_card_number('')
    with pytest.raises(ValueError):
        get_mask_card_number('qwertyuyryryryrr')
    with pytest.raises(ValueError):
        get_mask_card_number('55e2tyuy2yryryr1')

@pytest.fixture
def num_account():
    return '12345678912345122345'


def test_get_mask_account(num_account):
   assert get_mask_account(num_account) == "**2345"

@pytest.mark.parametrize('account_number, expected', [('1', ValueError),
                                                      ("", ValueError),
                                                      ('1234567889098777788888', ValueError),
                                                      ('gggggggggggggggggggk', ValueError),
                                                      (12345678923456345647, ValueError)])

def test_get_mask_account_invalid(account_number, expected):
    with pytest.raises(expected):
        get_mask_account(account_number)












