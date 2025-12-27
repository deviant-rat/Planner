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

def add_task (todo_list, last_id):
    name = input("Please, input the name \n >")
    if any(item["text"]==name for item in todo_list):
        print("Item with this name alredy exists.")
        return (last_id)
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

def mark_done(todo_list):
    if not todo_list:
        print("No items in list")
    else:
        name = input("Please, input the id \n >")
        try:
            user_id = int(name)
        except ValueError:
            print("Please enter a number")
            return
        found = False
        for item in todo_list:
            if item["id"] == user_id:
                item["done"] = True
                found = True
                break
        if found == True:
            print("Status changed successfuly")
        else:
            print("Item not found")

def print_help():
    print(" 1. add - adds new item (names should be uniq), \n 2. list - shows all items, \n 3. help - shows a list of commands \n 4. done - changes item Status to done \n 5. exit - closes the programm")

def save_tasks(todo_list, last_id):
    tasks_data ={
        "last_id": last_id,                
        "tasks": todo_list
    }
    with open("tasks.json", "w", encoding="utf-8") as write_file:
        json.dump(tasks_data, write_file, indent=2)            
        print("Tasks saved successfuly.")
    

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
        elif user_command == "exit":
            save_tasks(todo_list, last_id)
            print("Goodbye!")
            break
        else:
            print("Command not found. For the full list of commands use 'help'")

if __name__ == "__main__":
    main()