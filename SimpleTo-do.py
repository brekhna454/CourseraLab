# Simple To-Do List App in Python (Terminal Based)

tasks = []  # List to store all tasks

# Function to add a new task
def add_task():
    task = input("Enter the task description: ")
    tasks.append({"task": task, "done": False})
    print(f"Added: '{task}'")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
    print()

# Function to mark a task as done
def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task {task_num} marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted task: '{deleted['task']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
