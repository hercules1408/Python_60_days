def get_todos(filepath='Files/Subfiles/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='Files/Subfiles/todos.txt'):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)
