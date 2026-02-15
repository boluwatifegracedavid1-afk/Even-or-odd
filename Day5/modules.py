"""
import random

coin= random.choice([1,2,3,4,"tail","head",7]) # the list also accept integers.
number= random.randint(1,2)
print(number, number +1 )
"""

"""
import sys
print ("how far,",sys.argv[1])

for arg in sys.argv :
    print (arg)
"""

"""
import sys

if len(sys.argv)>2:
    print ("too many argument")
elif len(sys.argv)<2:
    print ("too few argument")
else:
    print ("how far,",sys.argv[1])
"""


import sys
print ("how far,",sys.argv[1:])