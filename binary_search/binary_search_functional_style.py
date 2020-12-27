from typing import List, Union


def center(array: List[int]) -> Union[int, None]:
    """
    Возвращает элемент в центре массива
    """
    if len(array) == 0:
        return None
    else:
        return array[len(array) // 2]


def first_half(array: List[int]) -> List[int]:
    """
    Возвращает первую половину списка
    """
    return array[:len(array) // 2]


def second_half(array: List[int]) -> List[int]:
    """
    Возвращает вторую половину списка
    """
    return array[len(array) // 2:]


def find_value(value: int, array: List[int], start_index: int):
    """
    Бинарно рекурсивно ищет число
    """
    if len(array) == 1:
        if array[0] == value:
            return start_index
        else:
            return -1
    else:
        if value < center(array):
            return find_value(value, first_half(array), start_index)
        else:
            return find_value(value, second_half(array), start_index + len(array) // 2)


def binary_search_functional_style(value: int, array: List[int]) -> int:
    """
    Тут я писал в функциональном стиле, не хранил значения и использовал только вызовы функций и рекурсию
    Я допустил тут 0 ошибок!!!!!
    """
    if len(array) == 0:
        return -1
    return find_value(value, array, 0)
