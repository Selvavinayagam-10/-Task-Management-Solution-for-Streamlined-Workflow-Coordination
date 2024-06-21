class Task:
    def __init__(self, title, description, status='To Do'):
        self.title, self.description, self.status = title, description, status

class TaskManager:
    def __init__(self): self.tasks = []
    def add(self, title, description): self.tasks.append(Task(title, description))
    def remove(self, title): self.tasks = [t for t in self.tasks if t.title != title]
    def update_status(self, title, status): [setattr(t, 'status', status) for t in self.tasks if t.title == title]
    def display(self): [print(f"Title: {t.title}\nDescription: {t.description}\nStatus: {t.status}\n") for t in self.tasks]

def main():
    tm = TaskManager()
    while True:
        print("1. Add Task\n2. Remove Task\n3. Update Status\n4. Display\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1': tm.add(input("Title: "), input("Description: "))
        elif choice == '2': tm.remove(input("Title to remove: "))
        elif choice == '3': tm.update_status(input("Title to update: "), input("New status: "))
        elif choice == '4': tm.display()
        elif choice == '5': break
        else: print("Invalid choice. Try again.")

if __name__ == "__main__": main()
