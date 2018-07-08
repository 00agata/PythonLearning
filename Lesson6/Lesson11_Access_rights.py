'''
The virus attacked the filesystem of the supercomputer and broke
the control of access rights to the files.
For each file there is a known set of
operations which may be applied to it:

write W
read R
execute X


 The first line contains the number N — the number of files
 contained in the filesystem. The following N lines contain
 the file names and allowed operations with them, separated by spaces.
 The next line contains an integer M — the number of operations
 to the files. In the last M lines specify the operations
 that are requested for files. One file can be requested many times.

You need to recover the control over the access rights to the files.
For each request your program should return OK if the
requested operation is valid or Access denied if the operation is invalid.
'''


file_system = {
    'file1': ['W', 'X'],
    'file2': ['R'],
    'file3': ['W']
}


def file_explorer():
    while True:
        # take the file name or exit command:
        file_name = str(input('File name: '))

        if file_name == "help":
            print("exit - in order to finish the program\
            \r\nhelp - in order to help\r\n")
            file_explorer()

        if file_name == "exit":
            break

        if file_name in file_system.keys():
            file_actions = file_system[file_name]

            # take the action
            file_action = str(input('Action: '))

            if file_action in file_actions:
                print('OK')
            else:
                print('Access denied')

        else:
            print('Access denied')


# print available files:
print('File system content: ')
for file in file_system.keys():
    print(file)
file_explorer()
