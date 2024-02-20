def funkcja_1 (names):
    if type(names) != list:
        return 'pass list of names'
    if len(names) != 5:
        return 'pass list of 5 names'
    for name in names:
        print(name)

lista = ['mateusz', 'ada', 'adam', 'karol', 'tomek']
print(funkcja_1(lista))