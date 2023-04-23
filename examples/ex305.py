def bottles_of_beer(bob):
    


    if bob < 1:
        print("""no""")
        return
    tmp = bob
    bob -= 1
    print("""{} банок,{},{}бутылок сока на стене
        """.format(tmp,
                   tmp,
                   bob))
    bottles_of_beer(bob)
bottles_of_beer(99)