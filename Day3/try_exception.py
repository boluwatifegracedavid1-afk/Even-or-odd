def getInt():
    while True:
        try:
            x= int(input("Type any integer: "))
            return (f"x is {x}")
        except: 
            ValueError
            print ("Type an integer")


getInt()