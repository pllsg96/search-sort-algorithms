def linear_search(array: list, value: int) -> int:
    for index, element in enumerate(array):
        if element == value:
            return index
    return -1


if __name__ == "__main__":
    example = [1, 2, 9, 4, 5]
    print(linear_search(example, 2))
    print(linear_search(example, 9))
    print(linear_search(example, 8))
