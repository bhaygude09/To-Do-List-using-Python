tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found!")

def complete_task(task):
    if task in tasks:
        print("Task completed:", task)
        tasks.remove(task)
    else:
        print("Task not found!")

def display_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            complete_task(task)
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
