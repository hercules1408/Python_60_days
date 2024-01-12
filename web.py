import streamlit as st
import Functions

todos = Functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)





st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a Todo', placeholder="Add a new todo.....",
              on_change=add_todo, key='new_todo')

print("Hello")

st.session_state