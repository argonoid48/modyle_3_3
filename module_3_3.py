# Галкин Андрей
# Задача "Распаковка"


def print_params(a = 1, b = 'строка', c = True):
    #return a, b, c
    print(a,b,c)

print_params( b = 25)
print_params(c = [1,2,3])


values_list=[2, 'список', (5,6,7)]
print_params(*values_list)

values_dict = {'a': 5, 'b': 'словарь','c':(8, 9, 10)}
print_params(** values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
