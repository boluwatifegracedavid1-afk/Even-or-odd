from datetime import datetime
year = int(input ("What year were you born: "))
currentYear= datetime.now().year
currentAge= currentYear- year
print(f"You will be {currentAge} this year")