import json

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file_read:
            file_dict = json.load(file_read)
            last_id = file_dict["last_id"]
            todo_list = file_dict["tasks"]
            print(f"File opened successfuly. {len(todo_list)} tasks loaded")
    except(FileNotFoundError, json.JSONDecodeError):
        todo_list= []
        last_id = 0
    return (todo_list, last_id)

def cheak_double(name, todo_list):
    if any(item["text"]==name for item in todo_list):
        print("Item with this name alredy exists.")
        return True
    return False

def add_task (todo_list, last_id):
    name = input("Please, input the name \n >")
    if cheak_double(name, todo_list): return (last_id)
    item = {
        "id": last_id,
        "text": name,
        "done": False
    }                    
    last_id += 1
    todo_list.append(item)
    print("Item added") 
    return (last_id)

def list_tasks(todo_list):
    if not todo_list:
        print('No items found')
    else:
        for item in todo_list:
            if item["done"] == True:
                print("[x]", end=" ")
            else:
                print("[ ]", end=" ")
            print(item["id"], end=" ")
            print(item["text"])

def cheak_full(todo_list):
    if not todo_list:
        print("No items in list")
        return False
    else: return True

def get_user_id():
    user_id = input("Please, input the id \n >")
    try:
        user_id = int(user_id)
        return True, user_id
    except ValueError:
        print("Please, enter a number")
        return False, user_id

def status_change(status, user_id, todo_list):
    for item in todo_list:
        if item["id"] == user_id:
            item["done"] = status
            print("Status changed successfuly")
            return
    print("Item not found")
    return

def mark_done(todo_list):
    if cheak_full(todo_list):
        status, user_id = get_user_id()
        if not status:
            return
        status_change(True, user_id, todo_list)
    return

def mark_undone(todo_list):
    if cheak_full(todo_list):
        status, user_id = get_user_id()
        if not status:
            return
        status_change(False, user_id, todo_list)
    return

def print_help():
    print(" 1. add - adds new item (names should be uniq), \n " \
    "2. list - shows all items, \n 3. help - shows a list of commands \n " \
    "4. done - changes item status to done \n 5. undone - changes item status to undone \n " \
    "6. exit - closes the programm, 7. change - changes the name of a task, \n " \
    "8. remove - remove an item \n 9. clear - deletes all items with status done \n " \
    "10. stats - shows statistics")

def save_tasks(todo_list, last_id):
    tasks_data ={
        "last_id": last_id,                
        "tasks": todo_list
    }
    with open("tasks.json", "w", encoding="utf-8") as write_file:
        json.dump(tasks_data, write_file, indent=2)            
        print("Tasks saved successfuly.")
    
def edit_task(todo_list):
    if cheak_full(todo_list):
        status, user_id = get_user_id()
        if not status:
            return
        name = input("Please, input new name \n >")
        if cheak_double(name, todo_list): return 
        for item in todo_list:
            if item["id"] == user_id:
                item["text"] = name
                print("Name changed successfuly")
                return
        print ("No item with such id exists")
    return

def remove_task(todo_list):
    if cheak_full(todo_list):
        status, user_id = get_user_id()
        if not status: return
        for item in todo_list:
            if item["id"] == user_id:
                todo_list.remove(item)
                print("Item deleted successfuly")
                return
        print("No such item exists")
    return

def clear_done(todo_list):
    if cheak_full(todo_list):
        count = len(todo_list)
        for i in range(count-1, -1, -1):
            if todo_list[i]["done"]:
                todo_list.remove(todo_list[i])
        print(f"{count - len(todo_list)} tasks are deleted")
    return 

def list_stats(todo_list):
    count = len(todo_list)
    done = 0
    for item in todo_list:
        if item["done"]: done+=1
    print(f"Total: {count}, Done: {done}, Pending: {count-done}")
    return



def main():
    todo_list, last_id = load_tasks()
    while True:
        print("Waiting for your command")
        user_command = input(">").strip().lower()
        if user_command == "add":
            last_id = add_task(todo_list, last_id)    
        elif user_command == "help":
            print_help()
        elif user_command == "list":
            list_tasks(todo_list)
        elif user_command == "done":
            mark_done(todo_list)
        elif user_command == "undone":
            mark_undone(todo_list)
        elif user_command == "change":
            edit_task(todo_list)
        elif user_command == "remove":
            remove_task(todo_list)
        elif user_command == "clear":
            clear_done(todo_list)
        elif user_command == "stats":
            list_stats(todo_list)
        elif user_command == "exit":
            save_tasks(todo_list, last_id)
            print("Goodbye!")
            break
        else:
            print("Command not found. For the full list of commands use 'help'")

if __name__ == "__main__":
    main()