def funkcja_2(numbers):
    lista_for = []
    if not isinstance(numbers, list):
        return 'pass list of numbers'
    if len(numbers) != 5:
        return 'pass list of 5 numbers'
    for numb in numbers:
        if not isinstance(numb, int):
            return 'elements must be numbers'
    for numb in range(len(numbers)):
        lista_for.append(numbers[numb] * 2)
    return lista_for


def funkcja_2b(numbers):
    lista_skladana = []
    if not isinstance(numbers, list):
        return 'pass list of numbers'
    if len(numbers) != 5:
        return 'pass list of 5 numbers'
    for numb in numbers:
        if not isinstance(numb, int):
            return 'elements must be numbers'
    lista_skladana = [number * 2 for number in numbers]
    return lista_skladana


lista = [1, 2, 3, 4, 5]
print(funkcja_2(lista))
print(funkcja_2b(lista))
