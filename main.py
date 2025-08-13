import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if not os.path.exists(FILE_NAME):
        return tasks
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    task = {
                        'id': int(parts[0]),
                        'title': parts[1],
                        'status': parts[2]
                    }
                    tasks.append(task)
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

# Save tasks to file
def save_tasks(tasks):
    try:
        with open(FILE_NAME, 'w') as file:
            for task in tasks:
                line = f"{task['id']},{task['title']},{task['status']}\n"
                file.write(line)
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Display tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"{task['id']}: {task['title']} [{task['status']}]")

# Add a task
def add_task(tasks, title):
    task_id = 1 if not tasks else tasks[-1]['id'] + 1
    task = {'id': task_id, 'title': title, 'status': 'Pending'}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

# Mark task as done
def mark_done(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Done'
            save_tasks(tasks)
            print("Task marked as done.")
            return
    print("Task not found.")

# Delete task
def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            print("Task deleted.")
            return
    print("Task not found.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: list, add, done, delete, exit")
        choice = input("Enter command: ").strip().lower()
        if choice == "list":
            list_tasks(tasks)
        elif choice == "add":
            title = input("Enter task title: ").strip()
            add_task(tasks, title)
        elif choice == "done":
            try:
                task_id = int(input("Enter task ID to mark done: "))
                mark_done(tasks, task_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == "delete":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
