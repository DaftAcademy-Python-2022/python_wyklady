def list_declaration():
    # zadeklaruj liste skladajaca sie z 4 elementow, kolejno: stringa, inta, floata i boola
    result: list = ['a', 1, 1.0, False]
    return result


def list_indexing(a: list):
    # zwroc pierwszy i ostatni element listy przekazanej jako argument 'a'
    first: int = a[0]
    last: int = a[-1]

    return first, last


def list_sum(a: list):
    # przpisz do zmiennej 'result' sume wszystkich elementow listy 'a'
    result: int = sum(a)
    return result


def dict_declaration():
    # zadeklaruj slownik ktory pod kluczem "line_length" bedzie mial wartosc 42
    my_dict: dict = {"line_length": 42}

    return my_dict


def dict_retrieving_values(mapping: dict):
    # zsumuj ze soba wartosci spod kluczy 'a' i 'b' ze slownika 'mapping'
    sum: int = mapping['a'] + mapping['b']
    return sum


def dict_pass_values(dict_a, dict_b):
    # przepisz wartosc spod klucza "variable" ze slownika "dict_a" do "dict_b"

    dict_b['variable'] = dict_a['variable']  # tutaj wstaw kod do przepisania wartosci

    return dict_b


def set_declaration():
    # zadeklaruj zbior skladajacy sie z samych liczb (int)
    my_set: set = {1}

    return my_set


def set_operations(set_a: set, set_b: set):
    # korzystajac ze zbiorow set_a i set_b stworz sety bedace kolejno przecieciem, suma i roznica tych dwoch zbiorow
    itersection: set = set_a.intersection(set_b)
    union: set = set_a.union(set_b)
    difference: set = set_a.difference(set_b)

    return itersection, union, difference


def set_add_list(values_set: set, values_list: list):
    # uzupelnij zbior values_set o wartosci z listy values_list
    result: set = values_set.union(values_list)
    return result
