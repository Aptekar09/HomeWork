import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def nums_1():
    return 'Visa Platinum 7000792289606361'
def test_mask_account_card(nums_1):
    assert mask_account_card(nums_1) == 'Visa Platinum 7000 79** **** 6361'

@pytest.mark.parametrize('account_cart, expected', [('', ValueError),
                                                    ('f', ValueError),
                                                    (1234, ValueError), ('hhhhh jjjj 8787879', ValueError),
                                                    ("Visa 7000792289606361", ValueError)
                                                ] )
def test_mask_account_card_invalid(account_cart, expected):
    with pytest.raises(expected):
        mask_account_card(account_cart)

@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"

def test_get_date(date):
    assert get_date(date) == '11.03.2024'

@pytest.mark.parametrize('date_num, expected', [(0, ValueError),
                                                ("", ValueError ),
                                                ('2024-03-11D02:26:18.671407', ValueError ),

                                        ])
def test_get_date_invalid(date_num, expected):
    with pytest.raises(ValueError):
        get_date(date_num)
