def list_tasks(tasks):
    for task in tasks:
        if task["completed"]:
            completion="Complete"
        else:
            completion="Incomplete"
        print(f'- {task["title"]} - {completion} -')

def add_task(tasks, title):
    task={
        "id":len(tasks)+1,
        "title":title,
        "completed":False
    }
    tasks.append(task)

def find_task(tasks,task_id):
    for task in tasks:
        if task["id"]==task_id:
            return task
    return None

def complete_task(task):
    task["completed"]=True

def delete_task(tasks,task):
    tasks.remove(task)