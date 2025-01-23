# to_do_list.py
import tkinter as tk
import to_do_list

# Function to add a task to the to-do list using tkinter
def add_task_tk(todo_list, task_entry, listbox):
    task = task_entry.get()
    if task:
        todo_list.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a task from the to-do list using tkinter
def remove_task_tk(todo_list, listbox):
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        todo_list.pop(task_index)
        listbox.delete(task_index)

# Function to create the tkinter GUI
def create_gui(todo_list):
    root = tk.Tk()
    root.title("To-Do List")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox = tk.Listbox(frame, width=50, height=10)
    listbox.pack(side=tk.LEFT, padx=(0, 10))

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)

    task_entry = tk.Entry(root, width=50)
    task_entry.pack(pady=5)

    add_button = tk.Button(root, text="Add Task", command=lambda: add_task_tk(todo_list, task_entry, listbox))
    add_button.pack(pady=5)

    remove_button = tk.Button(root, text="Remove Task", command=lambda: remove_task_tk(todo_list, listbox))
    remove_button.pack(pady=5)

    root.mainloop()

# Run the tkinter GUI
create_gui([])


# Function to display the to-do list
def display_todo_list(todo_list):
    print("\nTo-Do List:")
    for idx, task in enumerate(todo_list, 1):
        print(f"{idx}. {task}")
    print()

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.\n")

# Function to remove a task from the to-do list
def remove_task(todo_list):
    display_todo_list(todo_list)
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(todo_list):
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task}' removed from the list.\n")
    else:
        print("Invalid task number.\n")

# Main function to run the to-do list application
def main():
    todo_list = []
    while True:
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

    