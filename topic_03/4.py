#Маючи відсортований список, написати функцію пошуку позиції для вставки нового елементу в список.
def find_insert_position(sorted_list, new_element):
    for index, element in enumerate(sorted_list):
        if new_element < element:
            return index
    return len(sorted_list)  

sorted_list = [1, 3, 5, 7]
new_element = 4
position = find_insert_position(sorted_list, new_element)
print(f"Позиція для вставки {new_element} в {sorted_list}: {position}")
