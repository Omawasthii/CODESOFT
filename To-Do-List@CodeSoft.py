import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        pass

def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        new_task = entry.get()
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, new_task)
        entry.delete(0, tk.END)
    except IndexError:
        pass

def complete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        if not task.startswith("✓ "):
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, "✓ " + task)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for input and buttons
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Entry widget for adding and updating tasks
entry = tk.Entry(frame_input, width=40)
entry.grid(row=0, column=0, padx=5)

# Add Task button
add_button = tk.Button(frame_input, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

# Update Task button
update_button = tk.Button(frame_input, text="Update Task", command=update_task)
update_button.grid(row=0, column=2, padx=5)

# Create a frame for the task list
frame_list = tk.Frame(root)
frame_list.pack()

# Tasks Listbox for displaying tasks
tasks_listbox = tk.Listbox(frame_list, height=10, width=50)
tasks_listbox.pack(pady=5)

# Create a frame for task management buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack()

# Remove Task button
remove_button = tk.Button(frame_buttons, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=0, padx=5)

# Complete Task button
complete_button = tk.Button(frame_buttons, text="Complete Task", command=complete_task)
complete_button.grid(row=0, column=1, padx=5)

# Start the main event loop
root.mainloop()
