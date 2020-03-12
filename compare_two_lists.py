def compare_two_lists(list1: list, list2: list) -> None:
    '''Функция для сравнения 2-х списков. Выводит информацию о том, что добавилось в
    список, что ушло, на сколько позиций произошло смещение элемента в списке,
    сохраняя порядок. Ничего не возвращает.
    '''
    gone = []

    for i in range(len(list1)):
        if list1[i] in list2:
            movement = list2.index(list1[i]) - i
            if movement:
                print('Элемент {0} сместился в списке на {1}.'.format(list1[i], movement))
        else:
            gone.append(list1[i])
            # print('Элемент {0} ушел из списка'.format(list1[i]))

    added = [i for i in list2 if i not in list1]

    print('\nДобавились в список: {0}\nУшли из списка: {1}\n'.format(added, gone))


# ---------------------------------------- TESTS ----------------------------------------
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
b = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L']
compare_two_lists(a, b)

c = ['A', 'B', 'C', 'D']
d = ['A', 'B', 'C', 'D']
compare_two_lists(c, d)

e = []
f = ['A', 'B', 'C']
compare_two_lists(e, f)

g = ['A', 'B', 'C']
h = ['C', 'D']
compare_two_lists(g, h)
