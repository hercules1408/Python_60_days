def get_todos(filepath='Files/Subfiles/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='Files/Subfiles/todos.txt'):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)


# todos = []

while True:
    user_action = input("Type add, show ,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}---{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()

            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Command Not Valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            removed_todo = todos[index].strip('\n')
            #   print(todos,index,removed_todo)
            todos.pop(index)
            write_todos(todos)

            message = f"todo {removed_todo} was removed from the list"
            print(message)
        except IndexError:
            print('No Item with that number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Command not valid')
print("bye")
