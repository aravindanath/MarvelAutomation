
"""
AN exception is a event which occurs during exectuion of
 program that disrupts the normal flow of the program instructions.


https://docs.python.org/3/library/exceptions.html

"""

class skipexcetion(Exception):
    pass

print("Starting...")
try:
    i = 10
    z = 0
    print(i/z)

except Exception:
    print("exception occured")

    raise skipexcetion

else:
    print("else part Exception not occured")

finally:

    print("Mandatory excution")

print("ending...")
