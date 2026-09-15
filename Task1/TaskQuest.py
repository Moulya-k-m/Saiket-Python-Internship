tasks=[]
import json

def savetasks():
        with open ("tasks.json","w") as file:
             json.dump(tasks,file)
   

def loadtasks():
    global tasks
    try:
        with open ("tasks.json","r") as file:
             tasks=json.load(file)
    except FileNotFoundError:
        tasks=[]

def addtask():
    print("--------------------------------")
    name=input("Enter the task name: ")
    date=input("Enter the date(DD-MM-YYYY): ")
    time=input("Enter the deadline time: ")
    priority=input("Enter the task priority: ").capitalize()
    if priority=="High":
        points=20
    elif priority=="Medium":
        points=10
    else:
        points=5
    status="Pending"
    print("--------------------------------")

    task={
        "name" :name,
        "date":date,
        "time":time,
        "priority":priority,
        "status":status,
        "points": points
    }
    tasks.append(task)
    savetasks()

def viewtask():
    print("--------------------------------")
    if not tasks:
        print("No Tasks found")
    else:
        for task in tasks:
            print("===========TASKQUEST============")
            print(f"Task: {task['name']}")
            print(f"Date: {task['date']}")
            print(f"Time: {task['time']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print(f"Points: {task['points']}")
            print("===========================")
            print("--------------------------------")

def completedtask():
    print("--------------------------------")
    for index,task in enumerate(tasks):
        print(index+1,task['name'])
    try:
         choice=int(input("Enter task no to be completed: "))
    except ValueError:
            print("Enter a number")
            return
    if choice<1 or choice>len(tasks):
                 print("Enter a num within valid range")
                 return
    choice-=1
    task=tasks[choice]    
    if  task['status']=="Completed":
                          print("Task already completed")
                            
    else:
         print("Task Completed")
    print("--------------------------------")
              
    task['status']="Completed"
    savetasks()

def earnpoints():
    print("--------------------------------")
    total=0
    for task in tasks:
         if  task['status']=="Completed":
              total+=task['points']                  
    print(f"Total points earned: {total}")
    print("--------------------------------")

def dashboard():
     total_tasks=len(tasks)
     completed = 0
     for task in tasks:
           if task['status'] == "Completed":
            completed+=1
     pending = total_tasks - completed
     if total_tasks==0:
          completion_percentage=0
     else:
      completion_percentage= completed/total_tasks *100
     print("----------DASHBOARD------------")
     print(f"Total tasks: {total_tasks}")
     print(f"Completed tasks: {completed}")
     print(f"Completion percentage: {completion_percentage}%")
     print(f"Pending tasks: {completed}")
     print("-------------------------------")
     

loadtasks()
while True:
    print("\n" )
    print("========== TaskQuest ===========")
    print("1) Add a task")
    print("2) View past tasks")
    print("3) Complete tasks ")
    print("4) View points earned")
    print("5) Dashboard")
    print("6) Exit")

    try:
         choice=int(input("Enter your choice: "))
         if (choice==1):
              addtask()
         elif(choice==2):
              viewtask()
         elif(choice==3):
              completedtask()
         elif(choice==4):
              earnpoints()
         elif(choice==5):
              dashboard()
         elif(choice==6):
              print("--------------------------------")
              print("Thank you for using Task Quest")
              print("\n")
              break
         else:
              print("--------------------------------")
              print("Invalid choice")
              print("\n")
    except ValueError :
         print("--------------------------------")
         print("Enter a number")
         print("\n")