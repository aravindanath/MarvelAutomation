marks = int(input("Enter ur marks "))

if marks < 35:
    print("Fail")
elif marks >=35 and marks <45:
    print("pass class")
elif marks >=45 and marks <60:
    print("second class")
elif marks >= 60  and marks <85:
    print("first class")
elif marks >=85 and marks <=100:
    print("Top class")
else:
    print("contact admin")


print("out of condition")