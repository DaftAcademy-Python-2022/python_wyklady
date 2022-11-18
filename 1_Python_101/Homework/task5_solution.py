def concat_chars(chars: list):
    # uzupelnij wyrazenie w petli for tak, aby 'result' bylo polaczeniem wszystkich znakow z 'chars'
    result: str = ""

    for char in chars:
        result += char

    return result


def concat_chars_not_in_set(chars: list, forbidden_chars: set):
    # uzupelnij ponizsza petle tak, aby 'result' bylo polaczeniem znakow z 'chars' z pominieciem
    # znakow znajdujacych sie w 'forbidden_chars'
    result: str = ""

    for char in chars:
        if char in forbidden_chars:
            continue
        else:
            result += char

    return result


def sum_until(values: list, stop_value: int):
    # uzupelnij ponizsza petle tak, aby 'sum' bylo suma liczb z 'values' ktore znajduja sie w liscie
    # przed wartoscia 'stop_value'
    result: int = 0

    for value in values:
        if value == stop_value:
            break
        else:
            result += value

    return result


def double_until_value(a: int):
    # korzystajac z petli while, podwajaj liczbe 'a' az nie przekroczy wartosci 100
    # pamietaj o poprawnym warunku petli (obecnie False)
    result: int = a

    while result < 100:  # zastap False poprawnym wyrazeniem warunkowym
        result *= 2  # uzupelnij cialo petli
        print(result)

    return result


def for_else(values: list):
    # uzupelnij ponizsza petle for tak, aby value bylo False jesli w 'values' nie ma wartosc 10
    result: bool = True

    for value in values:
        if value == 10:
            break
    else:
        result = False

    return result


def list_comprehension_odd():
    # uzupelnij ponizsze wyrazenie tak, aby my_list zawieralo tylko liczby nieparzyste
    result: list = [x for x in range(10) if x % 2 != 0]
    return result


def list_comprehension_sets(set_a: set, set_b: set):
    # korzystajac z list comprehensions wygeneruj liste licz z zakresu 0 - 20 wlacznie,
    # ktore nie znajduje sie w set_a ani w set_b
    result: list = [x for x in range(21) if x not in set_a.union(set_b)]
    return result
