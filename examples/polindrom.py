def polindrom(word):

    if  word == list(reversed(word)):
        print("polindrom")
    elif word != list(reversed(word)):
        print("no polindrom")



polindrom("Mam")
