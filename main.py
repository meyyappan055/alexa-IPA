import pickle


# Define the Task class

class Task:
    def __init__(self, title, description, is_done=False):
        self.title = title  # Title of the task
        self.description = description  # Description of task
        self.is_done = is_done  # Whether the task is completed or not


# empty list to store tasks
task_list = []


# Function to add new task to the task_list
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task_list.append(Task(title, description))  # add the new task to the task list


# Function to display all tasks in the task list
def display_tasks():
    if not task_list:  # to check if the task list is empty
        print("No tasks to display.")
    else:
        index = 1
        for i in task_list:
            print(f"{index}:Title: {i.title}\n Description: {i.description}\n Completed: {i.is_done}")
            index += 1


# Function to mark a specific task as completed
def mark_task_completed():
    display_tasks()  # To see the available task and mark as completed
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        task_list[index].is_done = True  # Mark the selected task as completed
    except:
        print("enter correct input ")


# Function to delete a specific task from the task list
def delete_task():
    display_tasks()  # to Show the available tasks to the user
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        del task_list[index]
    except():
        print("invalid input ")

def save_tasks():
    with open("tasks.pickle", "wb") as f:  # Open the file in write-binary mode using pickle module
        pickle.dump(task_list, f)  # dump is like to write
    print("Tasks saved to file.")


# Function to load tasks from a file using the pickle module
def load_tasks():
    try:
        with open("tasks.pickle", "rb") as f:  # Open the file in read binary mode
            task_list = pickle.load(f)  # Load to read the file
        print("Tasks loaded from file.")
    except FileNotFoundError:
        print("File not found.")  # Handle the case when the file is not found



while True:
    print("\n1. Add a new task")
    print("2. Display all tasks")
    print("3. Mark a task as completed")  # Mark task as completed
    print("4. Delete a task")  # Delete a task
    print("5. Save tasks to a file")  # Save tasks to a file
    print("6. Load tasks from a file")  # Load tasks from a file
    print("7. Quit")

    choice = input("Enter your choice: ")  # Take user input for the choice

    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        save_tasks()
    elif choice == '6':
        load_tasks()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")  # Print a message for an invalid choice
