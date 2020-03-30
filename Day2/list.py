students = ["Arvind","Raj","Vijaya","Vijaya"]
print(type(students))
print(students)
students.append("Ravi")
print(students)

students.insert(8,"Raju")

print("5th ",students[5])
for ref in students:
    print(ref)

print("total no of students: ",len(students))
print(students[::-1])


std1=students.copy()
print("Copy",std1)

std1.pop(2)
print("pop",std1)

std1.remove("Vijaya")
print("remove",std1)