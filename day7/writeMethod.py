'''
MODES IN PYTHON

1. r -- read
2. w -- write
3. w+ -- write n read
4. x --  create
5. a -- append
6. t -- text mode
7. + -- Open the file for reading n writing mode

'''

def write():
    file = open("ReadWrite.txt", "w+")

    for i in range(10):
        file.write(str(i + 1))
        file.write("This is a line %d\r\n" % (i + 1))

    file.close()

def read():
    file = open("ReadWrite.txt", "r")
    print(file.readline())


def appendText():
    file = open("ReadWrite.txt", "a")
    for i in range(10):
        file.write(str(i + 1))
        file.write("Appended  line %d\r\n" % (i + 1))


def readAll():
    file = open("ReadWrite.txt", "r")
    if file.mode == 'r':
        contents =file.read()
        print(contents)


def readByLines():
    file = open("ReadWrite.txt", "r")
    file2 = open("writeToFile.txt", 'w+')
    f1 = file.readlines()
    for x in f1:
        print(x)
        file2.write(x)



if __name__ == "__main__":
    write()
    read()
    appendText()
    readAll()
    readByLines()