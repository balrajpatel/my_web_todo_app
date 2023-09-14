import streamlit as st
import functions

todo = functions.open_fn()

st.title("My Todo app")
st.subheader("This is my todo app")
st.write("This app is to increase productivity")

for index, todos in enumerate(todo):
    try:
        checkbox = st.checkbox(todos, key=todos)
        if checkbox:
            todo.pop(index)
            functions.write_todo(todo)
            del st.session_state[todo]
            print(todo)
            st.rerun()
    except KeyError:
        break

def add_todo():
    todos = st.session_state["new_todo"] + "\n"
    todo.append(todos)
    functions.write_todo(todo)


st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")

