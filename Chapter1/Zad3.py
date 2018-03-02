'''
Created on 28 sty 2018

@author: agata.wiewiora

N students take K apples and distribute them among each other evenly. 
The remaining (the undivisible) part remains in the basket. 
How many apples will each single student get? 
How many apples will remain in the basket?

The program reads the numbers N and K. 
It should print the two answers for the questions above.

'''


apples_amount = 0
students_amount = 0

def divide_fruits (apples_amount, students_amount):
    # Checks, if each student will receive at least one apple
    if (apples_amount < students_amount):
        print ("There are not enough apples to divide for all students")
    else:
        # Divides apples for all students:
        apples_per_student = apples_amount // students_amount
        
        if (apples_per_student == 1):
            print ("Each student will receive %d apple".format(apples_per_student))
        else:
            print ("Each student will receive %d apples".format(apples_per_student))
             
        # Checks, how man apples are left in the basket
        apples_left = apples_amount % students_amount
        
        if (apples_left ==1):
            print ("%d apple is left in the basket".format(apples_left))
        else:
            print ("%d apples are left in the basket".format(apples_left))


try:
    # Read amount of students:
    students_amount = raw_input("How many students? Please, provide amount: ")
    students_amount = int(students_amount)
    # Read amount of apples in the basket:
    apples_amount = raw_input("How many apples? Please, provide amount: ")
    apples_amount = int(apples_amount)
    # Try to divide fruits for students
    divide_fruits()
    
except ValueError:
    print ("Provided value is invalid. Program finished.")

