import os
import functools
from datetime import datetime as dt

def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            
            file = open(log_file_path, "a")
            file.write("-"*20 + "\n")
            file.write('Action {} executed on {} on {}\n'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            #result = func(path)
            #file.write('Function returned {}\n'.format(result))
            file.close()

            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE CREATE', r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 5\file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")

@wrapper_with_log_file('FILE DELETE', r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 5\file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 5\dummy_file.txt')
delete_file(r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 5\dummy_file.txt')
create_file(r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 5\dummy_file.txt')
delete_file(r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 5\dummy_file.txt')