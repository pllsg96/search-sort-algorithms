def binary_search(
        array: list,
        lowest_index: int,
        highest_index: int,
        value: int) -> int:

    if (highest_index < lowest_index):
        raise ValueError(f"{value} is not in list")

    middle_index = (highest_index + lowest_index) // 2

    if (array[middle_index]) == value:
        return middle_index

    elif array[middle_index] > value:
        return binary_search(array, lowest_index, middle_index - 1, value)

    else:
        return binary_search(array, middle_index + 1, highest_index, value)


# to this algorithm work, we need first sort the array that we are using
if __name__ == "__main__":
    example = [1, 2, 3, 4, 5]
    print(binary_search(example, 0, 4, 1))
    print(binary_search(example, 0, 4, 4))
    print(binary_search(example, 0, 4, 5))
    print(binary_search(example, 0, 4, 8))
