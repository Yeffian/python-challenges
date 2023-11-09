import os

def file_handler():
    print('You are currently in: ' + os.getcwd())
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    folders = [f for f in os.listdir(os.getcwd()) if os.path.isdir(f)]

    print('Folders:')
    for folder in folders:
        print('-' + folder)
    
    print('Files:')
    for file in files:
        print('-' + file)

file_handler()