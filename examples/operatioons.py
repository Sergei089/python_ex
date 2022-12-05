# data = open("fil.txt","r")
# s = data.readline()
# data.close()

# print(s)

with open('inf/45.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

print(s1)
print(s2)

print(inf.read())
