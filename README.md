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