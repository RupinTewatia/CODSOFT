import os

# Define the file where tasks will be stored
TASKS_FILE = "tasks.txt"

def display_menu():
    """Displays the main menu to the user."""
    print("\nTo-Do List Application")
    print("----------------------")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def load_tasks():
    """Loads tasks from the file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Saves tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def view_tasks(tasks):
    """Displays all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Prompts the user for a new task and adds it to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def mark_completed(tasks):
    """Marks a task as completed."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task_index = task_num - 1
            if not tasks[task_index].startswith("[COMPLETED]"):
                tasks[task_index] = f"[COMPLETED] {tasks[task_index]}"
                save_tasks(tasks)
                print("Task marked as completed.")
            else:
                print("This task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the application loop."""
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()