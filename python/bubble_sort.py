def bubble_sort(array: list):
    has_swipped = True
    n_of_iterations = 0

    while has_swipped:
        has_swipped = False
        for i in range(len(array) - n_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swipped = True
            n_of_iterations += 1

    return array


if __name__ == "__main__":
    example = [1, 90, 3, 6, 2]
    print(bubble_sort(example))

