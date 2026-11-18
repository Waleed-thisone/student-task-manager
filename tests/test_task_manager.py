"""Unit tests for the Student Task Manager core operations."""

import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """Tests for adding, completing and deleting tasks."""

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study DevOps")
        self.assertEqual(task["id"], 0)
        self.assertEqual(task["title"], "Study DevOps")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Finish lab report")
        result = self.manager.complete_task(task["id"])
        self.assertTrue(result)
        self.assertTrue(self.manager.get_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Buy groceries")
        result = self.manager.delete_task(task["id"])
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
