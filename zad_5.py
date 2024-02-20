def list_check(lista: list, numb: int) -> bool:
    return bool(numb in lista)

lista = [1,2,3]
numb = 5

print(list_check(lista,numb))