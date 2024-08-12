from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, 'EXECUTED')
    expected = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-09-30'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-03'},
    ]
    assert result == expected

def test_filter_by_state_default(sample_data):
    result = filter_by_state(sample_data)
    expected = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-09-30'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-03'},
    ]
    assert result == expected

def test_filter_by_state_no_matches(sample_data):
    result = filter_by_state(sample_data, 'UNKNOWN')
    expected = []
    assert result == expected

def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    expected = [
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-10-04'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-03'},
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-10-02'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-09-30'},
    ]
    assert result == expected

def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data, descending=False)
    expected = [
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-09-30'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-10-02'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-03'},
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-10-04'},
    ]
    assert result == expected
