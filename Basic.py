todos = []

while True:
    user_action = input("Type add, show ,complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index+1}---{item}"
                print(row)
        case 'edit':
            number = int(input("number of the todo to edit: "))
            number = number - 1
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("number of the todo to complete: "))
            todos.pop(number)
        case "exit":
            break
print("bye")
