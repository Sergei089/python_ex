import random as r

vars = ("Да", "Нет")

def get_random_vars(vars):
	# генератор 0,1 `g <- generator`
	g = (r.randint(range(0,1)))

	# функция должна рандомно выбирать да или нет!
	# random_index = random.randint(0,len(vars) -1)
	print(vars[g])
get_random_vars(vars)
