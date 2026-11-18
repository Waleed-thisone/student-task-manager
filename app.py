"""Console interface for the Student Task Manager."""

from task_manager import TaskManager


def display_tasks(manager):
    """Print all tasks currently stored in the manager."""
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['title']}")


def main():
    manager = TaskManager()
    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
            except ValueError as error:
                print(f"Could not add task: {error}")
            else:
                print(f"Task added with ID {task['id']}.")
        elif choice == "2":
            display_tasks(manager)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
