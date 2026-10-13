def show_menu():
    print("\n" + "=" * 34)
    print("          TO-DO LIST APP")
    print("=" * 34)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour task list is empty.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{number}. [{status}] {task['title']}")

def get_task_number(tasks, prompt):
    try:
        number = int(input(prompt))
        if 1 <= number <= len(tasks):
            return number - 1
        print("That task number does not exist.")
    except ValueError:
        print("Please enter a valid whole number.")
    return None

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter the task: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                index = get_task_number(tasks, "Enter task number to complete: ")
                if index is not None:
                    tasks[index]["completed"] = True
                    print("Task marked as completed!")

        elif choice == "4":
            view_tasks(tasks)
            if tasks:
                index = get_task_number(tasks, "Enter task number to delete: ")
                if index is not None:
                    removed = tasks.pop(index)
                    print(f"Deleted task: {removed['title']}")

        elif choice == "5":
            print("Thanks for using the To-Do List App. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 5.")

if __name__ == "__main__":
    main()
