from typing import List


def binary_search_using_bounds(value: int, array: List[int]) -> int:
    """
    Тут я использовал левую и правую границы, в центре которых ищется ответ, границы изменяют значение,
    в зависимости от того меньше искомое число, чем число в центре массива или больше.
    Я встретил 4 ошибки:
    1) Не учел пустых массивов
    2) Не учел массивов с нечетным числом элементов
    3) Не учел, что искомое число может отсутствовать
    4) Не учел, что в каком-то случае может быть бесконечный цикл
    """
    if len(array) == 0:
        return - 1
    left: int = 0
    right: int = len(array)
    i = left + (right - left) // 2
    while array[i] != value:
        if left - right == 0:
            return -1
        if array[i] > value:
            right = i
        else:
            left = i
        prev_i: int = i
        i = left + (right - left) // 2
        if prev_i == i:
            return -1
    return i
