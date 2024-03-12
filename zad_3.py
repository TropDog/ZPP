def is_even(number: int) -> bool:
    return bool(number % 2 == 0)


test_number = 6
result = is_even(test_number)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
