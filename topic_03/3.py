def test_dict_functions():
    my_dict = {'a': 1, 'b': 2}

    print("Початковий словник:", my_dict)

    my_dict.update({'c': 3})
    print("Після update():", my_dict)

    del my_dict['a']
    print("Після del():", my_dict)

    my_dict.clear()
    print("Після clear():", my_dict)

    my_dict = {'a': 1, 'b': 2}
    print("Ключі:", my_dict.keys())
    print("Значення:", my_dict.values())
    print("Пари ключ-значення:", my_dict.items())

test_dict_functions()
