list_num =[23, -45, -54, 23, 54]
list_num2 =[]
def negative(list_num):
    for item in list_num:
        if item < 0:
            list_num2.append(abs(item))


negative(list_num)
print(list_num2)
































# def transform_negative_and_group(list_num):
#     index = 0
#     if list_num[index] < 0:
#         print("Число отрицательное")
#     else:
#         print("Положительное")
#     return 
 
# transform_negative_and_group(list_num)




# # Функция принимает некое количество чисел 
# #сортирует по признака 