def mask_account_card(info: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах."""
    if "Счет" in info:
        # Маскировка счета: замена всех символов, кроме последних 4
        return "Счет " + "*" * (len(info.split()[1]) - 4) + info.split()[1][-4:]
    elif "Visa" in info or "Maestro" in info:
        # Маскировка карт: замена всех символов, кроме последних 4
        return info.split()[0] + " " + "*" * (len(info.split()[1]) - 4) + info.split()[1][-4:]
    else:
        raise ValueError("Неизвестный тип информации")


def get_date(date_string: str) -> str:
    """Функция, которая принимает на вход строку с датой """
    from datetime import datetime

    date_obj = datetime.fromisoformat(date_string)

    return date_obj.strftime("%d.%m.%Y")
