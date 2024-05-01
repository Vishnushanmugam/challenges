class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nPriority: {self.priority}\nStatus: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, task_id, title, description, priority, status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                task.priority = priority
                task.status = status
                break

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def view_all_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        for task in filtered_tasks:
            print(task)


# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()

    # Add tasks
    task_manager.add_task(Task(input("enter the tasks")))
   

    # View all tasks
    print("All Tasks:")
    task_manager.view_all_tasks()

    # Edit task
    task_manager.edit_task(2, "Updated Task 2", "Updated Description for Task 2", "High", "Completed")

    # View all tasks after editing
    print("\nAll Tasks after editing Task 2:")
    task_manager.view_all_tasks()

    # Delete task
    task_manager.delete_task(1)

    # View all tasks after deleting
    task_manager.view_all_tasks()

    # Filter tasks by priority
    task_manager.filter_tasks_by_priority("High")