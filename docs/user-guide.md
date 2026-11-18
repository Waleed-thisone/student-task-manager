# Student Task Manager — User Guide

The Student Task Manager is a small console application for keeping track of tasks. This guide explains how to run it and what each menu option does.

## Starting the application

From the project folder, run:

```bash
python app.py
```

The main menu appears:

```
--- Student Task Manager ---
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of an option and press Enter.

## 1. Add task

Choose `1`, then type the task title and press Enter.

```
Enter task title: Study DevOps
Task added with ID 1.
```

Titles cannot be empty. If you press Enter without typing anything (or only spaces), the application shows `Could not add task: Task title cannot be empty.` and returns to the menu — no empty task is created.

## 2. View tasks

Choose `2` to see all tasks. Each line shows the completion status, the task ID and the title:

```
[ ] 1. Study DevOps
[x] 2. Finish lab report
```

`[ ]` means the task is still open and `[x]` means it is completed. If there are no tasks yet, the application prints `No tasks yet.`

## 3. Complete task

Choose `3`, then enter the ID of the task you finished:

```
Enter the ID of the task to complete: 1
Task 1 marked as completed.
```

If the ID does not exist, you will see `No task found with ID 99.` (with the ID you entered). Non-numeric input is rejected with a message asking for a valid numeric ID.

## 4. Delete task

Choose `4`, then enter the ID of the task to remove. Because deleting cannot be undone, the application asks for confirmation first:

```
Enter the ID of the task to delete: 2
Are you sure you want to delete task 2? (y/n): y
Task 2 deleted.
```

Type `y` to confirm or anything else to cancel (`Delete cancelled.`). Task IDs are never reused, so a new task added afterwards gets a fresh ID.

## 5. Exit

Choose `5` to close the application. Tasks are stored in memory only, so the list starts empty the next time you run the application.
