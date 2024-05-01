class Task:
    def __init__(self, id, title, description, priority, status):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, task_id, new_title, new_description, new_priority, new_status):
        task = self.get_task_by_id(task_id)
        if task:
            task.title = new_title
            task.description = new_description
            task.priority = new_priority
            task.status = new_status
            return True
        return False

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        return filtered_tasks

    def switch_case(self, choice):
        options = {
            1: self.add_task,
            2: self.edit_task,
            3: self.delete_task,
            4: self.view_all_tasks,
            5: self.filter_tasks_by_priority,
        }
        return options.get(choice, lambda: print("Invalid choice"))


# Example usage
task_manager = TaskManager()

while True:
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting...")
        break

    task_operation = task_manager.switch_case(choice)
    if choice in [1, 2]:
        task_id = int(input("Enter task ID: "))
        if choice == 1:
            title = input("Enter title: ")
            description = input("Enter description: ")
            priority = input("Enter priority: ")
            status = input("Enter status: ")
            new_task = Task(task_id, title, description, priority, status)
            result = task_operation(new_task)
        else:
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            new_priority = input("Enter new priority: ")
            new_status = input("Enter new status: ")
            result = task_operation(task_id, new_title, new_description, new_priority, new_status)
    elif choice == 3:
        task_id=int(input("Enter the i'd:"))
        result = task_operation(task_id)
        if result:
            print("Task deleted successfully")
        else:
            print("Task not found")
    elif choice == 4:
        task_operation()

    elif choice == 5:
        priority = input("Enter priority to filter: ")
        filtered_tasks = task_operation(priority)
        print("\n Filtered tasks:")
        for task in filtered_tasks:
            print(task)
    else:
        task_operation()
