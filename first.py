# Simple To-Do List Program

tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            task_num = int(input("Enter task number to remove: "))
            
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")