from faker import Faker


myfaker = Faker()

# test names

list_of_fake_names = []
for i in range (0, 30):
    list_of_fake_names.append(myfaker.name())
    print('{}'.format(list_of_fake_names[i]))
