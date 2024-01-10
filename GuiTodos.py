import PySimpleGUI as sg

import Functions

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
add_button = sg.Button("Add")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
