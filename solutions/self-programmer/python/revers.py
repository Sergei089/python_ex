str ='When you play a game of thrones you win or you die.'
reversedString=[]
index = len(str)
while index > 0:
    reversedString += str[index -1]
    index = index -1
print(reversedString)