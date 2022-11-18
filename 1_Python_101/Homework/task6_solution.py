def lazy_scribe(sources: list):
    # W tym zadaniu wcielisz sie w skrybe (a do tego lenia i plagiatora) ciagow znakowych
    # skryba dostal zadanie stworzenia nowego ciagu znakowego, nie chce mu sie poswiecac
    # zbyt duzo czasu na to zadanie wiec postanowil wykorzystac ciagi znakowe ze swojej
    # biblioteczki. Dziala metodycznie, przeglada dostepne mu ciagi w takiej kolejnosci
    # w jakiej znajduja sie w jego bilbioteczce, kopiuje z nich po jednym znaku i dokleja go do 
    # swojego nowotworzonego ciagu. Powtarza te czynnosc az do wyczerpania dostepnych mu ciagow
    # za kazdym razem kopiujac kolejny znak z ciagu. Dodatkowo, z racji tego, ze jest leniwy,
    # kompresuje powtarzajace sie znaki zastepujac je liczba kolejnych wystapien polaczona z
    # samym znakiem.
    #
    # Przyklad:
    # Skryba ma w swojej bilbioteczce (sources) nastepujace ciagi znakowe:
    # ['python', 'java', 'golang']
    # Jego genialna i nowatorska metoda tworzenia nowych ciagow zaowocuje nastepujacym ciagiem:
    # 'pjgyaotvlh2ao2ng'
    #  
    # Pomoz skrybie zautomatyzowac ten proces!
    
    # * W liscie sources znajduja sie ciagi znakowe ktore odpowiadaja bilbioteczce skryby.
    # * Ciagi znakowe w 'sources' skladaja sie wylacznie ze znakow a-z



    # make all strings fixed length, padded with space
    if len(sources) == 0:
        return ''
    elif len(sources) == 1:
        return sources[0]

    string_lengths = [len(s) for s in sources]
    longest_length: int = max(string_lengths)

    if longest_length == 0:
        return ''

    sources_with_fixed_length = [
        s + ' ' * (longest_length - len(s))
        for s in sources
    ]

    # zip all the strings together and remove spaces
    interweaving_string = ''

    for chars in zip(*sources_with_fixed_length):
        interweaving_string += ''.join(chars)
    
    interweaving_string = interweaving_string.replace(' ', '')


    # compress the result
    result = ''
    current_char = interweaving_string[0]
    current_counter = 0

    for char in interweaving_string[1:]:
        if char == current_char:
            current_counter +=1
            continue
    
        if current_counter == 0:
            result += current_char
            current_char = char
        else:
            result += (str(current_counter+1) + current_char)
            current_counter = 0
            current_char = char
    
    if current_counter == 0:
            result += current_char
    else:
        result += (str(current_counter+1) + current_char)


    return result


