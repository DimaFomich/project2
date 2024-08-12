import pytest
from src.widget.widget import mask_account_card, get_date

def test_mask_account_card_account(valid_account_info):
    result = mask_account_card(valid_account_info)
    expected = "Счет ************3456"
    assert result == expected

def test_mask_account_card_card(valid_card_info):
    result = mask_account_card(valid_card_info)
    expected = "Visa ************5678"
    assert result == expected

def test_mask_account_card_unknown_type():
    with pytest.raises(ValueError):
        mask_account_card("Unknown type 1234")

def test_get_date(valid_date_string):
    result = get_date(valid_date_string)
    expected = "01.10.2023"
    assert result == expected

def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("invalid-date")
