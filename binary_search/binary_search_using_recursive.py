from typing import List


def recursive_chop(value: int, array: List[int], left: int, right: int) -> int:
    if left - right == 0:
        return -1
    i: int = left + (right - left) // 2
    if array[i] == value:
        return i
    if i == left or i == right:
        return - 1
    if array[i] > value:
        return recursive_chop(value, array, left, i)
    else:
        return recursive_chop(value, array, i, right)


def binary_search_using_recursive(value: int, array: List[int]) -> int:
    """
    В этой реализации я допустил 1 ошибку:
    1) Не учел, что когда середина между границами равна одной из гранц,
    получается бесконечная рекурсия
    """
    return recursive_chop(value, array, 0, len(array))


if __name__ == '__main__':
    binary_search_using_recursive(3, [1])
