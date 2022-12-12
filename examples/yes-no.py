import random
vars =("Да", 
	   "Нет"
	   )


def get_random_vars(vars):
	# генератор 0,1
	v = (range(0,1))

	print(vars[v])

	# функция должна рандомно выбирать да или нет!
	# random_index = random.randint(0,len(vars) -1)
get_random_vars(vars)
