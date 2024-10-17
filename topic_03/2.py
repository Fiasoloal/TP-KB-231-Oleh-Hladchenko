def test_list_functions():
    my_list = [1, 2, 3]

    print("Початковий список:", my_list)

    my_list.extend([4, 5])
    print("Після extend():", my_list)

    my_list.append(6)
    print("Після append():", my_list)

    my_list.insert(0, 0)
    print("Після insert():", my_list)

    my_list.remove(3)
    print("Після remove():", my_list)

    my_list.clear()
    print("Після clear():", my_list)

    my_list = [3, 1, 2]
    my_list.sort()
    print("Після sort():", my_list)

    my_list.reverse()
    print("Після reverse():", my_list)

    copied_list = my_list.copy()
    print("Скопійований список:", copied_list)

test_list_functions()
