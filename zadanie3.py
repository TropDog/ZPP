def funkcja_3 (numbers):
    if type(numbers) != list:
        return 'pass list of numbers'
    if len(numbers) != 10:
        return 'pass list of 10 numbers'
    for numb in numbers:
        if type(numb) != int:
            return 'elements must be numbers'
    for numb in range(len(numbers)):
        if numbers[numb]%2 ==0:
             print(numbers[numb])
    
lista = [1,2,3,4,5,6,7,8,9,10]

funkcja_3(lista)