from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    n1, n2, n3 = "", "", ""
    if(name == ""):
        n1 = "missing name"
    if(description == ""):
        n2 = "missing description"
    if(due == ""):
        n3 = "missing due date"
    if((name == "") or (description == "") or (due == "")):
        print(f"Unable to add task: {n1} {n2} {n3}")
        return
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    task.update({"lastActivity" : datetime.now()})
    # set the name, description, and due date (all must be provided)
    task.update({"name":name, "description":description, "due":str_to_datetime(due)})
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    tasks.append(task)
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    print(f"Task added successfully!")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    save()

    """bag27:2/12/2023
    using datetime.now(), the lastActivity value is updated to the current time. 
    the function takes all of the user-input arguments and updates the associated 
    key-value pairs in the task with the input. the task is then appended to the 
    tasks list. finally, a message is printed letting the user know whetherthe task
    has been successfully added or not, depending on missing arguments"""

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if(index >= len(tasks)):
        print(f"No task at this index. There are only {len(tasks)} tasks!")
        return None
    elif(index < 0):
        print(f"No task at this index. Remember, index starts at 1!")
        return None
    task = tasks[index]
    taskname = task.get("name")
    taskdesc = task.get("description")
    taskdue = task.get("due")
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """bag27:2/12/2023
    function first checks if index is out of bounds. next it extracts the name, description, and 
    duedate of selected task. the values are displayed next to prompts. function then
    call update_task function to update the task"""

    name = input(f"What's the name of this task? ({taskname}) \n").strip()
    desc = input(f"What's a brief descriptions of this task? ({taskdesc}) \n").strip()
    due = input(f"When is this task due? (format: m/d/y H:M:S) ({taskdue}) \n").strip()
    update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    """out of bounds handled in process update function"""
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    s1, s2, s3 = "was not", "was not", "was not"
    if(name != ""):
        tasks[index].update({"name":name})
        s1 = "was"
    if(description != ""):
        tasks[index].update({"description":description})
        s2 = "was"
    if(due != ""):
        tasks[index].update({"due":str_to_datetime(due)})
        s3 = "was"
    # update lastActivity with the current datetime value
    tasks[index].update({"lastActivity":datetime.now()})
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    print(f"The task was successfully updated. Name {s1} updated, description {s2} updated, and due date {s3} updated.")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """bag27:2/12/2023
    the function updates the task values only if the user has input data. regardless of 
    any changes, the lastActivity value is always updated. finally, a print statement 
    tells the user which values have been changed"""
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if(index >= len(tasks)):
        print(f"No task at this index. There are only {len(tasks)} tasks!")
        return None
    elif(index < 0):
        print(f"No task at this index. Remember, index starts at 1!")
        return None
    # if it's not done, record the current datetime as the value
    task = tasks[index]
    if(task["done"] == False):
        tasks[index].update({"done":datetime.now()})
        print(f"Task completed!")
    else:
        print(f"Task already completed.")
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """bag27:2/12/2023
    first check if index is in bounds. next the done value of the task is
    evaluated. if it is not completed, it is marked as done. if it is
    already completed, a message saying show is shown"""
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if(index >= len(tasks)):
        print(f"No task at this index. There are only {len(tasks)} tasks!")
        return None
    elif(index < 0):
        print(f"No task at this index. Remember, index starts at 1!")
        return None
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = tasks[index]
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))

    """bag27:2/15/2023
    first checks that the index is in bounds. then assigns 
    task variable to the task at the index of the tasks list.
    the given print statement then displays information about the task"""

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if(index >= len(tasks)):
        print(f"No task at this index. There are only {len(tasks)} tasks!")
        return None
    elif(index < 0):
        print(f"No task at this index. Remember, index starts at 1!")
        return None
    del tasks[index]
    print(f"Successfully deleted")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """bag27:2/12/2023
    first made sure index was in bounds. then deleted task from list at
    given index using the del command"""
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    _tasks = []
    for i in tasks:
        if(i['done'] == False):
            _tasks.append(i)
    if(len(_tasks) == 0):
        print(f'There are no incomplete tasks!')
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """bag27:1/25/2023
    traverses the tasks dict using a for loop.
    for every task, determines if done = false. if
    done = false, task is added to _tasks which represents
    the incomplete tasks. finally, the _tasks list is passed to the 
    list_tasks function"""
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    _tasks = []
    for i in tasks:
        if((i['done']) == False) and (str_to_datetime(i['due']) < datetime.now()):
            _tasks.append(i)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    list_tasks(_tasks)
    """bag27:2/15/2023
    similar to get_incomplete_tasks, this function traverses the dict
    to find all the tasks that are not done and have a due date that
    is less than the current date. str_to_datetime converts the 'due' value
    for each task to a datetime, so that it can be easily compared to
    the current date using comparison operators"""

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if(index >= len(tasks)):
        print(f"No task at this index. There are only {len(tasks)} tasks!")
        return None
    elif(index < 0):
        print(f"No task at this index. Remember, index starts at 1!")
        return None
    task = tasks[index]
    dif = None
    # get the days, hours, minutes, seconds between the due date and now
    if(str_to_datetime(task['due']) >= datetime.now()):
        dif = str_to_datetime(task['due']) - datetime.now()
        days = dif.days #algorithm to get timedelta hours, minutes, and seconds from https://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes
        hours, r = divmod(dif.seconds, 3600)
        minutes, seconds = divmod(r, 60)
        print(f'Task is due in: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds')
    elif(str_to_datetime(task['due']) < datetime.now()):
        dif = datetime.now() - str_to_datetime(task['due'])
        days = dif.days
        hours, r = divmod(dif.seconds, 3600)
        minutes, seconds = divmod(r, 60)
        print(f'Overdue! Task is overdue by: {days} days, {seconds} hours, {minutes} minutes, and {seconds} seconds')
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """bag27:2/15/2023
    first makes sure index is in bounds. next compares current time to due date.
    if due date > current time, function gets the days, hours, mins, and seconds to due
    date simply using the subtraction operator. the data is then formatted using
    an algorithm to get the hours, minutes, and seconds in a readable format. if
    due date < current time, task is overdue. time past since due date is shown in 
    same format"""

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()