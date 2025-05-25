import streamlit as st
import json
from pathlib import Path

TODO_FILE = Path("todo.json")

# --- Functions ---
def load_tasks():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# --- App Layout ---
st.set_page_config(page_title="Todo List Manager", page_icon="📝")
st.title("📝 Todo List Manager")
st.write("Add, view, and complete your tasks.")

tasks = load_tasks()

# Load custom CSS
try:
    with open("style/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom CSS file not found.")

# --- Add New Task ---
new_task = st.text_input("Enter a new task")
if st.button("Add Task"):
    if new_task.strip() != "":
        tasks.append({"task": new_task, "done": False})
        save_tasks(tasks)
        st.success("Task added!")
        st.rerun()  # Updated for latest Streamlit

# --- Display Tasks ---
if tasks:
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            done = st.checkbox("", value=task['done'], key=f"task_{i}")
        with col2:
            st.write(task["task"])
        task["done"] = done
    save_tasks(tasks)
else:
    st.info("No tasks found!")

# --- Clear Completed ---
if st.button("Clear Completed Tasks"):
    tasks = [task for task in tasks if not task["done"]]
    save_tasks(tasks)
    st.rerun()
