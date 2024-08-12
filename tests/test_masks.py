import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(valid_card_number):
    result = get_mask_card_number(valid_card_number)
    expected = "1234 56** **** 5678"
    assert result == expected

def test_get_mask_account(valid_account_number):
    result = get_mask_account(valid_account_number)
    expected = "**3456"
    assert result == expected

def test_get_mask_card_number_short():
    card_number = "1234"
    result = get_mask_card_number(card_number)
    expected = "1234 ** **** 1234"
    assert result == expected

def test_get_mask_account_short():
    account_number = "123"
    result = get_mask_account(account_number)
    expected = "**123"
    assert result == expected
