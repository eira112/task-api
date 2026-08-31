from task_manager import add_task, list_tasks, find_task, delete_task, complete_task
tasks=[]

menu=" 1. add a task \n 2. list all task \n 3. Complete Task \n 4. Delete task \n 5. Exit"
while True:
    print(menu)
    choice=input("select an option: ")
    if(choice=='1'):
        while(True):
            task_name=input("enter task name: ")
            add_task(tasks,task_name)
            user_choice=input("do you want to add another task(y/n): ")
            if(user_choice=='n'):
                break
    elif(choice=='2'):
        if not tasks:
            print("No task added yet!")
        else:
            list_tasks(tasks)
        input("Tap any btn to continue")
    elif(choice=='3'):
        task_id=int(input("enter a task id to mark it complete: "))
        task=find_task(tasks,task_id)
        if task:
            complete_task(task)
            print(f'task {task["title"]} was marked complete')
        else:
            print("no task found")
        input("Tap any btn to continue")
    elif(choice=='4'):
        task_id=int(input("Enter a task id to delete it: "))
        task=find_task(tasks,task_id)
        if task:
            delete_task(tasks,task)
            print("The task was deleted")
            input("Tap any btn to continue")
        else:
            print("No task found")
    elif(choice=='5'):
        print("Thank you. See you later!")
        break
    else:
        print("Invalid Input. Try Again!")
        input("Tap any btn to continue")
