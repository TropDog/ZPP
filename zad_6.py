def list_transformation(lista: list, lista2: list) -> list:
    unique = set(lista + lista2)
    unique = [number**3 for number in unique]
    return unique


lista = [1, 2, 3]
lista2 = [1, 2, 4]

print(list_transformation(lista, lista2))
