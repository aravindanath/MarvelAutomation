'''
MODES IN PYTHON

1. r -- read
2. w -- write
3. w+ -- write n read
4. x --  create

'''

file = open("ReadWrite.txt","w+")


for i in range(10):
    file.write(str(i+1))
    file.write("This is a line %d\r\n"% (i+1))

file.close()