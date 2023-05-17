# похоже на сценарии с argv
def print_two(*args):
argl, arg2 = args
print(f"argl: (argl), arg2: {arg2}")

# o k , здесь вместо *args мы делаем следующее
def print_two_again(argl, arg2):
    print(f"argl: {argl}, arg2: {arg2}")

# принимает только один аргумент
def print_one(argl):
print(f"argl: {argl}")

# не принимает аргументов
def print_none ():

    print("А я ничего не получаю.")


print_two("Михаил","Райтман")
print_two_again("Михаил","Райтман")
print_one("Первый!")
print_none()