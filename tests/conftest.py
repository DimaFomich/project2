import pytest

@pytest.fixture
def valid_card_number():
    return "1234567812345678"

@pytest.fixture
def valid_account_number():
    return "1234567890123456"

@pytest.fixture
def valid_account_info():
    return "Счет 1234567890123456"

@pytest.fixture
def valid_card_info():
    return "Visa 1234567812345678"

@pytest.fixture
def valid_date_string():
    return "2023-10-01"

@pytest.fixture
def sample_data():
    """
    Фикстура для тестовых данных.
    """
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-10-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-09-30'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-03'},
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-10-04'},
    ]
