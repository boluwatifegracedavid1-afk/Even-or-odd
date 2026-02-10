x= float(input ("Type a value for x: "))
y= float(input ("Type a value for y: "))
opr= input ("Type a value for operator: ")

if opr == "+":
    print (x+y)
elif opr == "-":
    print (x-y)
elif opr == "*":
    print (x*y)
elif opr == "/":
    if y != 0: 
        print (x/y)
    else:
        print("Not possible")
else:
    print ("Wrong input")
       
      

