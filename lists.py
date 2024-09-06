todos = []

def home_menu():
    pass

def folder_adder():
    folder_name = input('Folder name: ')
    if folder_name in todos:
        print('Folder already exists')
    else:
        todos.append(folder_name)
        print('Folder added')
    return input('Would you like to add another? (Y/N): ')
    
def folder_adder_finished(add_another_folder):
    if add_another_folder in ('Y','y'):
        return True
    elif add_another_folder in ('N','n'):
        return False
    else:
        return folder_adder_finished(input('Please type \'Y\' or \'N\': '))
    
while True:
    add_another_folder = folder_adder()
    if not folder_adder_finished(add_another_folder):
        print(todos)
        break