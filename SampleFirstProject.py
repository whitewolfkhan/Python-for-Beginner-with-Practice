# Create Command line task manager
# --------------------------------
# store task in a dictionary with unique id

import os
import csv
import json
# File to store task
FileName = "task.txt"

# load task from file
def loadTask():
    tasks = {} # dictionary
    if os.path.exists(FileName): # check task
        with open(FileName, "r") as file:
            for line in file:   # each line is a task
                taskId , title, status = line.strip().split(" | ")
                tasks[int(taskId)] = {"title": title, "status": status}   # convert taskId into int
    return tasks

# save tasks to file
def saveTask(tasks):
    with open(FileName, "w") as file:
        for taskId, task in tasks.items():
            file.write(f"{taskId} | {task['title']} | {task['status']} \n")  # add one task and goes next line and keeps on writing task
            
            
# add a new task
def addTask(tasks):
    title = input("Enter task title : ")
    taskId = max(tasks.keys(), default=0) + 1   # taking the task and looking keys and getting the max value from the task
    tasks[taskId] = {"title": title, "status": "incompleted"}
    print(f"Task '{title}' added.")
    

# view all task
def viewTask(tasks):
    if not tasks:
        print("No task available")
    else:
        for taskId, task in tasks.items(): # go through each and every item inside task and get the task id task and print that
            print(f"[{taskId}] {task['title']} - {task['status']}")
            

# mark task as complete
def markTaskComplete(tasks):
    taskId = int(input("Enter the task ID to mark as completed :"))
    if taskId in tasks:
        tasks[taskId]["status"] = "Complete"
        print(f"Task '{tasks[taskId]['title']}' mark as complete.")
    else:
        print("Task ID not found.")
        
# delete a task
def deleteTask(tasks):
    taskId = int(input("Enter the task ID to delete :"))
    if taskId in tasks:
        deletedTask = tasks.pop(taskId)
        print(f"Task '{deletedTask['title']}' is deleted.")
    else:
        print("Task ID not found.")
 
# add json file       
def export_to_json(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks exported to {filename}")
    
    
# add csv file
def export_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Task ID", "Title", "Status"])  # header
        for taskId, task in tasks.items():
            writer.writerow([taskId, task["title"], task["status"]])
    print(f"Tasks exported to {filename}")
    
    
       
# main menu
def main():
    tasks = loadTask()
    while True:
        print("\n Task Manager Team ")
        print("1. Add task ")
        print("2. View task ")
        print("3. Mark task as Complete ")
        print("4. Delete task ")
        print("5. Export to JSON ")
        print("6. Export to CSV ")
        print("7. Exit ")
        choice = input("Enter your choices : ")
        
        if choice == "1":
            addTask(tasks)
        elif choice == "2":
            viewTask(tasks)
        elif choice == "3":
            markTaskComplete(tasks)
        elif choice == "4":
            deleteTask(tasks)
        elif choice == "5":
            export_to_json(tasks)
        elif choice == "6":
            export_to_csv(tasks)
        elif choice == "7":
            saveTask(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid Choice, try again")
            
if __name__ == "__main__":
    main()