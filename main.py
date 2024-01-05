# todos = []

while True:
    user_action = input("Type add, show ,complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"
            # file = open('Files/Subfiles/todos.txt', 'r')
            with open('Files/Subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
                # file.close()
                todos.append(todo)

            with open('Files/Subfiles/todos.txt', 'w') as file:

                file.writelines(todos)

        case "show":
            with open('Files/Subfiles/todos.txt', 'r') as file:

                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}---{item}"
                print(row)
        case 'edit':
            number = int(input("number of the todo to edit: "))
            number = number - 1
            with open('Files/Subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n'

            with open('Files/Subfiles/todos.txt', 'w') as file:

                file.writelines(todos)

        case 'complete':
            number = int(input("number of the todo to complete: "))
            with open('Files/Subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            removed_todo = todos[index].strip('\n')
            #   print(todos,index,removed_todo)
            todos.pop(index)
            with open('Files/Subfiles/todos.txt', 'w') as file:

                file.writelines(todos)

            message = f"todo {removed_todo} was removed from the list"
            print(message)
        case "exit":
            break
print("bye")
