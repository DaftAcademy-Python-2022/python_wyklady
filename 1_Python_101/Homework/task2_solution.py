def basic_int_operations(a, b):
    # policz kolejno sume, roznice, iloczyn i iloraz liczb a i b
    sum: int = a + b
    difference: int = a - b 
    product: int = a * b
    quotient: int = int(a / b)

    return sum, difference, product, quotient


def string_length(a: str):
    # przypisz do zmiennej 'length' dlugosc ciagu znakow otrzymanego jako argument 'a'
    length: int = len(a)
    return length


def first_and_last_chars(a: str):
    # do zmiennych first i last przypisz kolejno pierwszy i ostatni znak
    # z otrzymanego ciagu znakow w argumencie 'a'
    first: str = a[0]
    last: str = a[-1]

    return first, last


def string_capitalization(a: str):
    # do zmiennych przypisz otrzymany w argumencie 'a' ciag znakow po przekonwertowaniu go
    # odpowiednio na same wielkie (upper) litery i same male (lower) litery
    upper: str = a.upper()
    lower: str = a.lower()

    return upper, lower


def add_exclamation_mark(a: str):
    # do zmiennej result przypisz ciag znakow otrzymany w argumencie 'a'
    # jesli ciag znakow 'a' nie posiada na koncu '!', dodaj go
    result: str = a + '!' if a[-1] != '!' else a
    return result


def cut_string(a: str):
    # do zmiennej 'result' przypisz ciag znakow 'a' po wycieciu z niego ciagu 'python'
    # JDSKJBGEpythonDD -> JDSKJBGEDD
    result: str = a.replace("python", "", 1)
    return result
