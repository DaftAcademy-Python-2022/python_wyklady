def subsets_everywhere(elements: set):
    # Napisz program tworzący ze zbioru `elements` zbiór zawierający wszystkie
    # podzbiory `elements` (włącznie z pustym i `elements`).
    # UWAGA: w python zbiory (set) nie mogą być elementami innych zbiorów,
    # proszę użyć `frozenset` jako zbiorów wewnętrznych.
    # Wynik przypisz do zmienej `result`
    result: set = set({frozenset()})  # set with empty set

    for element in elements:
        partial_result = set()
        for s in result:
            partial_result.add(s.union({element}))
        result = result.union(partial_result)

    return result
