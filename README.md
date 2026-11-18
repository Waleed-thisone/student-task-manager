# Student Task Manager

A small Python console application to add, display, complete and delete tasks.

Project status: In Development (planning complete, implementation in progress)

This project was developed for the CSC418 DevOps Lab Assignment 4 to practice a complete Git and GitHub workflow: commits, branching, pull requests, merge conflict resolution, automated testing with GitHub Actions, and releases.

## Features

- **Add tasks** with input validation — empty or blank titles are rejected with a friendly error message.
- **Display tasks** in a list showing each task's ID, title and completion status (`[x]` / `[ ]`).
- **Complete tasks** by ID once the work is done.
- **Delete tasks** by ID, with a confirmation prompt so nothing is removed by accident.
- Task IDs are never reused, even after a task is deleted.

## Setup

You need Python 3.10 or newer. There are no third-party dependencies.

```bash
git clone https://github.com/Waleed-thisone/student-task-manager.git
cd student-task-manager
```

## Usage

Run the application:

```bash
python app.py
```

You will see a menu:

```
--- Student Task Manager ---
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
```

Choose an option by typing its number. See [docs/user-guide.md](docs/user-guide.md) for a full walkthrough with examples.

## Running the Tests

The project includes unit tests (Python `unittest`) covering adding, completing and deleting tasks:

```bash
python -m unittest discover -s tests -v
```

The same tests run automatically in GitHub Actions on every push to `main` and on every pull request that targets `main` (see `.github/workflows/python-tests.yml`).

## Project Structure

```
student-task-manager/
|-- app.py                  # Console interface (menu)
|-- task_manager.py         # Core TaskManager logic
|-- tests/
|   `-- test_task_manager.py
|-- docs/
|   `-- user-guide.md
|-- LAB-REPORT.md           # Lab report (Part G answers)
`-- .github/workflows/
    `-- python-tests.yml    # CI workflow
```

## License

Released under the MIT License — see [LICENSE](LICENSE).
