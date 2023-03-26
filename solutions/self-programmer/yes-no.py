import random
vars =("Да","Нет","Возможно")


def get_random_vars(vars):
	# генератор 0,1
	v = (random.randint(0,2))

	print(vars[v])

	# функция должна рандомно выбирать да или нет!
	# random_index = random.randint(0,len(vars) -1)
get_random_vars(vars)
