
"""
AN exception is a event which occurs during exectuion of
 program that disrupts the normal flow of the program instructions.




"""


print("Starting...")
try:
    i = 10
    z = 2
    print(i/z)
except:
    print("exception occured")
else:
    print("Exception not occured")
print("ending...")