days = ('su', 'mo', 'tu')
a = list(days)

# print(a[2])
a.append("we")
print(a)

a.pop(0)
print(a)

a.insert(3, 100)
print(type(a))


print(type(days))