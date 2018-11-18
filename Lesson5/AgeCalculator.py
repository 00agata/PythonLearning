'''
Age calculator - write a program that for given list of people's ages
calculate the average age of adults (age >= 18)
and count the children (age < 18). Use list comprehensions.
'''


list_of_ages = [5, 6, 8, 19, 50, 89]


def count_average_age_for_adult_and_child(list):
    adults = [age for age in list if age >= 18]
    children = [age for age in list if age < 18]
    adults_average = 0
    children_average = 0
    if len(adults) > 0:
        adults_average = sum(adults)/len(adults)
    if len(children) > 0:
        children_average = sum(children)/len(children)
    return (adults_average, children_average)


print('{:6.2f}, {:6.2f}'.format(
    count_average_age_for_adult_and_child(list_of_ages)[0],
    count_average_age_for_adult_and_child(list_of_ages)[1]))
