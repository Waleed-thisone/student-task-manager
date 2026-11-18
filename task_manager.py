"""Core task management logic for the Student Task Manager."""


class TaskManager:
    """Stores tasks in memory and provides operations on them.

    Each task is a dictionary with an ``id``, a ``title`` and a
    ``completed`` flag. IDs are handed out from a counter so they are
    never reused, even after a task is deleted.
    """

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        """Create a new task with the given title and return it.

        Raises ValueError if the title is empty or only whitespace.
        """
        if title is None or not str(title).strip():
            raise ValueError("Task title cannot be empty.")
        task = {"id": self._next_id, "title": str(title).strip(), "completed": False}
        self._next_id += 1
        self.tasks.append(task)
        return task

    def complete_task(self, task_id):
        """Mark the task with the given ID as completed.

        Returns True if the task was found, otherwise False.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False

    def get_tasks(self):
        """Return the list of all tasks."""
        return self.tasks
