def return_int():
    # przypisz do zmiennej 'result' dowolna wartosc typu int
    result: int = 22
    return result


def return_string():
    # przypisz do zmiennej 'result' wartosc typu string dluzsza niz 4 znaki
    result: str = "Daftcode"
    return result


def return_float():
    # przypisz do zmiennej 'result' float z zakresu (-1, 1)
    result: float = -0.5
    return result


def return_false():
    # przypisz do ponizszej zmiennej 'result' wartosc bool o wartosci falszu
    result: bool = False
    return result


def convert_to_int(numeric_string: str):
    # przekonwertuj wartosc 'numeric_string' na int'a
    result: int = int(numeric_string)
    return result


def return_complex(real: int):
    # dodaj do zmiennej real dowolna wartosc tak aby powstala liczba urojona
    result: complex = real + 1j
    return result
