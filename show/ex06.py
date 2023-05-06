
# присвоение аргумента 
types_of_people = 10
# -
x = f"Существует {types_of_people} типов людей."
# пприсвоение аргумента
binary = "Python"
# -
do_not = "нет"

y = f" Те, кто понимает {binary}, и те, кто -{do_not}."
# печатать x
print(x)
# печатать у
print(y)

print(f"Я сказал: {x}")
print(f"А еще я сказал: '{y}'")

hilarious = False
joke_evaluation = "Разве это не смешно?!{}"

print(joke_evaluation.format(hilarious))

w =  "Это часть строки слева..."
e = "а жто справа."

print(w + e)
