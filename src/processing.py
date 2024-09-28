def filter_by_state(dict_list: list[dict], state_1: str='EXECUTED') -> list[dict]:
    """Функция, которая фильтрует словари"""
    new_dict_list = []
    for dict in dict_list:
        if dict.get("state") == state_1:
            new_dict_list.append(dict)
    return new_dict_list