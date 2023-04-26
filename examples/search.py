
# Алгарит последовательного поиска
# Написать функцию принимающую два аргумента:
# -список чисел
# -"искомое" число
#  Функция должна возвращать True - False

# Переменная list_num


def search(list_num, num):
    res = False

    for i in list_num:
        if i == num:
            res = True
            break
    return res

list_num = range(1000000,2000001)

num1 = search(list_num,1579354)
num2 = search(list_num,3596492)

# итератор, начало,конец ,счетчик 

print(num1)
print(num2)



