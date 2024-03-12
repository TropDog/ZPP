def funkcja_4(numbers):
    if not isinstance(numbers, list):
        return 'pass list of numbers'
    if len(numbers) != 10:
        return 'pass list of 10 numbers'
    for numb in numbers:
        if not isinstance(numb, int):
            return 'elements must be numbers'
    for numb in range(len(numbers)):
        if numb % 2 == 0:
            print(numbers[numb])


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

funkcja_4(lista)
