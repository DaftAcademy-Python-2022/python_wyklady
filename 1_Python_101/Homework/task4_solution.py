def simple_conditional(a: int):
    # uzupelnij ponizsze wyrazenie warunkowe tak, aby zmienna 'result' miala wartosc True
    # tylko wtedy gdy 'a' jest wieksze od 10

    result: bool = False

    if a > 10:
        result = True

    return result


def zero_comparision(a: int):
    # uzupelnij ponizsze wyrazenie warunkowe tak, aby zmienna result miala wartosc
    # 1 gdy a jest wieksze od 0, -1 gdy mniejsze niz 0 i 0 gdy rowne 0

    if a > 0:
        result = 1
    elif a < 0:
        result = -1
    else:
        result = 0

    return result


def list_searching(a: int, b: list):
    # uzupelnij ponizsze wyrazenie warunkowe tak, aby result miala wartosc True jesli
    # wartosc 'a' znajduje sie w liscie 'b'
    result: bool = False

    if a in b:
        result = True

    return result


def roman_numerals(a: int):
    # napisz instrukcje warunkowa ktora dla licz  z przedzialu 1 - 10 przypisze do zmiennej 'result'
    # jej odpowiednik w notacji rzymskiej np 3 - 'III', jesli liczba bedzie spoze tego przedzialu, wpisz pustego
    # stringa ''

    result: str = ""

    # tutaj wpisz odpowiednie wyrazenie warunkowe
    if a == 1:
        result = "I"
    elif a == 2:
        result = "II"
    elif a == 3:
        result = "III"
    elif a == 4:
        result = "IV"
    elif a == 5:
        result = "V"
    elif a == 6:
        result = "VI"
    elif a == 7:
        result = "VII"
    elif a == 8:
        result = "VIII"
    elif a == 9:
        result = "IX"
    elif a == 10:
        result = "X"
    

    return result
