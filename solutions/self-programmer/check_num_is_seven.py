num = 8

# Проверка на соответсвие(что в переменной `num` хранится значение `7`)
def check_num_is_seven(num):
	if num is 7:
		print(num)
	else:
		""" Используем интерполяцию - 
			в строке, при помощи `f` помещаем `{num}`
		"""
		print(f"В переменной `num` нет значения 7. Там лежит {num}")

check_num_is_seven(4)

# Изменить код так, чтобы при передаче вызываемой функции 
# значения `7` - выдавалось бы сообщение:
# В переменной хранится 7. Проверено.