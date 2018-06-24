'''
Age calculator - write a program that for given list of people's
ages calculate the average age of adults (age >= 18)
and count the children (age < 18). Use list comprehensions.
'''


def average_age_of_adults(age_list):
    filter = 18
    if all(age >= 0 for age in age_list):
        filtered_list = [age for age in age_list if age >= filter]
        print reduce(lambda x, y: x + y, filtered_list) / len(filtered_list)
    else:
        print('Please provide correct values greater than 0')


average_age_of_adults([2, 18, 30])
