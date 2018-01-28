'''
Created on 28 sty 2018

@author: agata.wiewiora
'''


def count_tables_amount (students_amount):
    table_students = 2 
    temp = students_amount % table_students
    if temp > 0:
        tables_amount = (students_amount // table_students) + 1
    else:
        tables_amount = students_amount // table_students
    return tables_amount

students = {}


try:
    # Reads how many students:
    students_a = raw_input("Please, provide amount of students in class a: ")
    students_a = int(students_a)
    students['students_A'] = students_a
    students_b = raw_input("Please, provide amount of students in class b: ")
    students_b = int(students_b)
    students ["students_B"] = students_b
    students_c = raw_input("Please, provide amount of students in class c: ")
    students_c = int(students_c)
    students ["students_C"] = students_c
    
    for students_ in students:
        tables_amount = count_tables_amount(students[students_])
        print ("For group {} you need {} tables").format(students_, tables_amount)
        
except ValueError:
    print ("Provided value is invalid. Program finished.")
    