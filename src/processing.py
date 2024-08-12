def filter_by_state(data, state='EXECUTED'):
    """
    Функция фильтрует список словарей по значению ключа 'state'.
    :param data: Список словарей.
    :param state: Значение для фильтрации, по умолчанию 'EXECUTED'.
    :return: Новый список словарей.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, descending=True):
    """
    Функция сортирует список словарей по дате.
    :param data: Список словарей.
    :param descending: Порядок сортировки, по умолчанию убывание.
    :return: Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
