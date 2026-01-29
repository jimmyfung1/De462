import streamlit as st

# TODO: Initialize 'todos' in session state as an empty list
if "todos" not in st.session_state:
    st.session_state.todos = []

# TODO: Initialize 'completed' in session state as an empty list
if 'completed' not in st.session_state:
    st.session_state.completed = []

st.title("✅ To-Do List Manager")

# TODO: Create a text input for new task
new_task = st.text_input("Add a new task:")

# TODO: Add button to add tasks to the list
if st.button("Add task to list"):
    if new_task:  # Only add if not empty
        st.session_state.todos.append(new_task)
        st.success(f"Added: {new_task}")

# TODO: Toggle to show/hide completed tasks
show_completed = st.checkbox("Show completed tasks", value=True)

# TODO: Display all tasks
st.subheader("Your Tasks:")
if st.session_state.todos:
    for i, task in enumerate(st.session_state.todos, 1):
        # Check if task is in completed list
        is_completed = task in st.session_state.completed
        
        # Only show based on toggle setting
        if show_completed or not is_completed:
            # TODO: Create checkbox for each task
            checked = st.checkbox(
                f"{i}. {task}",
                value=is_completed,
                key=f"task_{i}"
            )
            
            # TODO: Update completed list based on checkbox
            if checked and task not in st.session_state.completed:
                st.session_state.completed.append(task)
            elif not checked and task in st.session_state.completed:
                st.session_state.completed.remove(task)
else:
    st.info("No tasks yet. Add your first task above!")

# TODO: Show total count of tasks
st.write(f"Total tasks: {len(st.session_state.todos)}")
st.write(f"Completed: {len(st.session_state.completed)}")

# TODO: Add button to clear all tasks
if st.button("Clear All Tasks"):
    if st.session_state.todos:
        st.session_state.todos = []
        st.session_state.completed = []
        st.success("All tasks cleared!")
    else:
        st.warning("No tasks to clear")