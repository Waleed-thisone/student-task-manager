"""Console interface for the Student Task Manager."""

from task_manager import TaskManager


def display_tasks(manager):
    """Print all tasks currently stored in the manager."""
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{status} {task['id']}. {task['title']}")


def main():
    manager = TaskManager()
    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")
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
            raw_id = input("Enter the ID of the task to complete: ").strip()
            if not raw_id.isdigit():
                print("Please enter a valid numeric task ID.")
            elif manager.complete_task(int(raw_id)):
                print(f"Task {raw_id} marked as completed.")
            else:
                print(f"No task found with ID {raw_id}.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
