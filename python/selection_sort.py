def selection_sort(array: list):
    for i in range(len(array)):
        minimum = i

        print('1º if - posição: ', minimum, 'valor: ', array[minimum])
        for j in range(i + 1, len(array)):
            if (array[j] < array[minimum]):
                print('PRÉ 2º if - posição: ',
                      minimum, 'valor: ', array[minimum])
                minimum = j
                print('PÓS 2º if - posição: ',
                      minimum, 'valor: ', array[minimum])

        array[minimum], array[i] = array[i], array[minimum]

    return array


if __name__ == "__main__":
    example = [1, 90, 3, 6, 2]
    print(selection_sort(example))

