from datetime import datetime
year = int(input ("What year were you born or your age : "))
currentYear= datetime.now().year
if 201<= year <= 1726:
    print("Please type your correct age")

elif year >1726:
    currentAge= currentYear- year
    if currentAge>= 18:
        print(f"You are {currentAge} this year and you are elligible for voting")
    else :
        print(f"You are {currentAge} this year and you are not elligible for voting")

else :
    currentAge= year
    if currentAge>= 18:
        print(f"You are {currentAge} this year and you are elligible for voting")
    else :
        print(f"You are {currentAge} this year and you are not elligible for voting")
