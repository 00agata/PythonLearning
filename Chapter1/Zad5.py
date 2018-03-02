'''
Created on 28 sty 2018

@author: agata.wiewiora
'''


def count_tables_amount (students_amount):
    if students_amount % 2 != 0:
        return students_amount // 2 + 1
    else:
        return  students_amount // 2 


students = {}

try:
    # Reads how many students:
    students_a = raw_input("Provide amount of students in class a: ")
    students_a = int(students_a)
    students['students_A'] = students_a
    students_b = raw_input("Provide amount of students in class b: ")
    students_b = int(students_b)
    students ["students_B"] = students_b
    students_c = raw_input("Provide amount of students in class c: ")
    students_c = int(students_c)
    students ["students_C"] = students_c
    
    for class_students in students:
        tables_amount = count_tables_amount(students[class_students])
        print ("For group {} you need {} tables").format(class_students,
                                                         tables_amount)
        
except ValueError:
    print ("Provided value is invalid. Program finished.")
