
files = {}


def check_access(files, file, actions):
    if file in files.keys():
        for action in actions.split(','):
            if action not in files[file].split(','):
                print('Access denied')
            else:
                print('Access granted')


M = int(input('Please, provide amount of files in the system'))
for i in range(M):
    files_key = str(input('Provide file name: '))
    files_value = str(input('Provide allowed actions, e.g. W,R: '))
    files[files_key] = files_value

if len(files.keys()) > 0:
    N = int(input('Please, provide amount of requested operations: '))
    for i in range(N):
        file = str(input('Provide file name: '))
        actions = str(input('Provide requested actions, e.g. W,R: '))
        check_access(files, file, actions)
