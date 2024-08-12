# Проект по банковским картам.

**Новая фича для личного кабинета клиента:** Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка

1. Клонируйте репозиторий:bash
   git clone https://github.com/вашеимя/вашрепозиторий.git
2. Установите зависимости, если есть (например, через pip):bash
   pip install -r requirements.txt 

## Использование

### Функции модуля `processing`

- **filter_by_state(data, state='EXECUTED')**
    - Фильтрует список словарей по значению ключа 'state'.
    - **Параметры:**
      - `data`: Список словарей.
      - `state`: Значение для фильтрации (по умолчанию 'EXECUTED').
    - **Пример:**
    filtereddata = filterbystate(datalist, 'EXECUTED')

- **sort_by_date(data, descending=True)**
    - Сортирует список словарей по дате.
    - **Параметры:**
      - `data`: Список словарей.
      - `descending`: Порядок сортировки (по умолчанию убывание).
    - **Пример:**
    sorteddata = sortbydate(datalist)

## Примеры работы с функциями
python
datalist = [
    {'state': 'EXECUTED', 'date': '2023-01-01'},
    {'state': 'PENDING', 'date': '2023-01-02'},
    {'state': 'EXECUTED', 'date': '2023-01-03'},
]

filtered = filterbystate(datalist)
sorteddata = sortbydate(datalist)

## Тесты для функций
1. test_mask_account_card_account: Проверяет, что функция mask_account_card возвращает правильную маску для счета.
2. test_mask_account_card_card: Проверяет, что функция mask_account_card правильно обрабатывает информацию о карте.
3. test_mask_account_card_unknown_type: Убедитесь, что функция вызывает исключение 
при передаче неизвестного типа информации.
4. test_get_date: Проверяет правильное форматирование даты.
5. test_get_date_invalid_format: Убедитесь, что функция вызывает исключение при передаче неправильного формата даты.
6. test_get_mask_card_number: Проверяет, что функция get_mask_card_number 
возвращает правильную маску для полного номера карты.
7. test_get_mask_account: Проверяет, что функция get_mask_account возвращает последние 4 цифры номера счета.
8. test_get_mask_card_number_short: Проверяет корректность обработки короткого номера карты.
9. test_get_mask_account_short: Проверяет корректность обработки короткого номера счета.
10. test_filter_by_state: Тестирует фильтрацию по состоянию EXECUTED.
11. test_filter_by_state_default: Тестирует фильтрацию по умолчанию.
12. test_filter_by_state_no_matches: Проверяет, что возвращается пустой список, если нет совпадений.
13. 1test_sort_by_date: Проверяет, правильно ли сортируется список по дате в порядке убывания.
14. test_sort_by_date_descending: Проверяет, правильно ли сортируется список по дате в порядке возрастания.

### Пояснения:
1. Фикстура sample_data: Создаёт тестовые данные, которые будут 
использоваться в тестах. Она возвращает список словарей,
представляющих различные транзакции с полями id, state и date.

### Запуск тестов
pytest test_masks.py
pytest test_masks_and_date.py
pytest <your_test_file_name.py>



