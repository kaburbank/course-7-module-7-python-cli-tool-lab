# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:

    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

# TODO: Define the User class
# Each user has a name and a list of tasks
# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # TODO: Search for a task by its title in the user's task list
        # TODO: Return the matching task or None
        pass

import argparse

users = {}

def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")

parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser("add-task", help="Add a new task")
add_parser.add_argument("user")
add_parser.add_argument("title")
add_parser.set_defaults(func=add_task)

complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
complete_parser.add_argument("user")
complete_parser.add_argument("title")
complete_parser.set_defaults(func=complete_task)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()