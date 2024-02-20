def funkcja_2 (numbers):
    if type(numbers) != list:
        return 'pass list of numbers'
    if len(numbers) != 5:
        return 'pass list of 5 numbers'
    for numb in numbers:
        if type(numb) != int:
            return 'elements must be numbers'
    for numb in range(len(numbers)):
        numbers[numb] = numbers[numb]*2
    return numbers
lista = [1, 2, 3, 4, 5]
print(funkcja_2(lista))