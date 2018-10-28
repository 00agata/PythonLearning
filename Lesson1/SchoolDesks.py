'''
A school decided to replace the desks in three classrooms.
Each desk sits two students.
Given the number of students in each class,
print the smallest possible number of desks that can be purchased.
'''


studentsA = int(input('Please provide amount of students in class A: '))
studentsB = int(input('Please provide amount of students in class B: '))
studentsC = int(input('Please provide amount of students in class C: '))


def calculateAmountOfDesks (students):
    oneDesk = 2
    allDesks = students//oneDesk
    if(students%oneDesk > 0):
        allDesks+=1
    return allDesks


print('For class A we need {} desks'.format(calculateAmountOfDesks(studentsA)))
print('For class B we need {} desks'.format(calculateAmountOfDesks(studentsB)))
print('For class C we need {} desks'.format(calculateAmountOfDesks(studentsC)))
