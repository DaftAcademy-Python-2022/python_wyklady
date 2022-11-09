def list_declaration():
    # Zadeklaruj listę skłądającą się z 4 elementów określonych typów,
    # kolejno: `string`, `int`, `float` i `bool`
    result: list = ...
    return result


def list_indexing(a: list):
    # Do zmiennych zadeklarowanych poniżej przypisz pierwszy (zmienna `first`)
    # i ostatni (zmienna `last`) element listy przekazanej jako argument `a`
    first: int = ...
    last: int = ...

    return first, last


def list_sum(a: list):
    # Przypisz do zmiennej `result` sumę wszystkich elementów listy `a`
    result: int = ...
    return result


def dict_declaration():
    # Zadeklaruj słownik, który pod kluczem `line_length` będzie miał wartość 42
    my_dict: dict = ...

    return my_dict


def dict_retrieving_values(mapping: dict):
    # Zsumuj ze sobą wartości spod kluczy `a` i `b` ze słownika `mapping`
    sum: int = ...
    return sum


def dict_pass_values(dict_a, dict_b):
    # Przepisz wartość spod klucza "variable" ze słownika `dict_a` do `dict_b`

    ...  # Tutaj wstaw kod do przepisania wartości

    return dict_b


def set_declaration():
    # Zadeklaruj zbiór składający się z samych liczb typu `int`
    my_set: set = ...

    return my_set


def set_operations(set_a: set, set_b: set):
    # Korzystając ze zbiotów `set_a` i `set_b` stwórz zbiory będące kolejno przecięciem, sumą i różnicą
    # tych dwóch zbiorów. Wyniki powyższych operacji przypisz do odpowiadających im zmiennych zadeklarowanych
    # poniżej
    intersection: set = ...
    union: set = ...
    difference: set = ...

    return intersection, union, difference


def set_add_list(values_set: set, values_list: list):
    # Uzupełnij zbiór `values_set` o wartości z listy `values_list`
    result: set = ...
    return result
