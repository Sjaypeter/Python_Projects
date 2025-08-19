
Option = input("Enter Option(1-5): ")   
is_running = True
Tasks = []
       
def add_task():
    Task = input("Enter the name of the task: ")
    Tasks.append(Task)
    print(f"Task : {Task} added successfully!")
        
def view_tasks():
    if not Tasks:
        print("No task available.")
    else:
        for i in Tasks:
            print(i)
                
def Delete_task():
    if not Tasks:
        print("No task available.")
    else:
        Task = input("Enter the name of the task to delete: ")
        Tasks.remove(Task)
        print(f"Task : {Task} succesfully removed")

def complete_task():
    pass                
        
                



def display_menu():
    print("1.Add task")
    print("2.View task")
    print("3.Delete task")
    print("4.Complete task")
    print("5.Quit")


while is_running: 
    if Option == "1":
        add_task()
            
    elif Option == "2":
        view_tasks()
        
    elif Option == "3":
        Delete_task()
        
    elif Option == "4":
        complete_task()
        
    elif Option == "5":
        is_running = False
print("Thank You")

display_menu()

        