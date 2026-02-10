"""
#Printing numbers 1to 10 using for loop
for i in range(1,11):
    print (i)
    i+=1
"""

"""
#Printing numbers 1to 10 using while loop
i=1
while i< 11:
    print (i)
    i+=1
"""

"""
# multiplication table
x= int(input("mltiplication table for which number: "))
i=1
while i< 13 :
    print (x, "x", i,"=", x*i)
    i+=1
"""

"""
# password checker
password = input ("Your Password: ")
i=3
while i>0 :
    if password == "AdeOlu7":
        print ("Correct")
        i=0;
    else:
        if (i-1)!=0:
            print (f"Incorrect. {i-1} trials more")
            i-=1
            password = input ("Password: ")
        else:
            print ("Try again in 1 hour time")
            break
"""

"""
# Number guessing game

secreteNum= int(input ("guess the secrete integer: "))
i=7
x=0
while x==0:
    if secreteNum==i:
        print ("You are correct")
        x=1
    else:
        print ("You are wrong! Try again")
        secreteNum= int(input ("guess the secrete integer again: "))
"""
    