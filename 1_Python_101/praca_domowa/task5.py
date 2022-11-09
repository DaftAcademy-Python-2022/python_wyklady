def concat_chars(chars: list):
    # Uzupełnij wyrażenie w pętli `for` tak, aby zmienna `result` zawierała w sobie
    # ciąg znaków będący połączeniem wszystkich znaków z listy `chars`
    result: str = ""

    for char in chars:
        ...

    return result


def concat_chars_not_in_set(chars: list, forbidden_chars: set):
    # Uzupełnij poniższą pętlę tak, aby `result` było połączeniem znaków z `chars`
    # z pominięciem znaków znajdujących się w zbiorze `forbidden_chars`
    result: str = ""

    for char in chars:
        ...

    return result


def sum_until(values: list, stop_value: int):
    # Uzupełnij poniższą pętlę tak, zmienna `result` przyjmowała wartość sumy elementów znajdujących
    # się w liście `values` przed pierwszym wystąpieniem wartości `stop_value`
    # Przykład:
    # Dla `values = [1, 1, 3]` i `stop_value = 3` zmienna `result` powinna przyjąć wartość `2`
    result: int = 0

    for value in values:
        ...

    return result


def double_until_value(a: int):
    # Korzystając z pętli `while`, podwajaj wartość zapisaną w zmiennej `a` aż
    # przekroczy wartość `100`, przypisz otrzymaną wartość do zmiennej `result`
    # Przykład: dla `a = 2` `result` powinno przyjąć wartość `128`
    # Pamiętaj o poprawnym warunku pętli (obecnie `False`)

    result: int = a

    while False:  # Zastąp `False` poprawnym wyrażeniem warunkowym
        ...  # Uzupełnij ciało pętli

    return result


def for_else(values: list):
    # Uzupełnij poniższą pętlę `for` tak, aby zmienna `result` przyjmowała wartość `False`
    # jeśli w liście `values` nie ma wartości 10
    result: bool = True

    for value in values:
        ...
    else:
        ...

    return result


def list_comprehension_odd():
    # Uzupełnij poniższe wyrażenie `list comprehension` tak, aby zmienna `result` była
    # listą zawierającą liczby nieparzyste z zakresu 1 - 9 włącznie
    result: list = [x for x in range(10)]
    return result


def list_comprehension_sets(set_a: set, set_b: set):
    # Korzystając z `list comprehension` wygeneruj listę liczb z zakresu 0 - 20
    # włącznie pomijając liczby znajdujące się w zbiorze `set_a` lub w zbiorze `set_b`
    result: list = [...]
    return result
