def count_letters(string):
    count_dict = {}# конструктор пустого словаря
    for c in string:
        if c in count_dict:
            count_dict[c] += 1 
        else:
            count_dict[c] = 1
    print (count_dict)    

count_letters("Династия")

