import json
try:
    with open("tasks.json", "r", encoding="utf-8") as file_read:
        file_dict = json.load(file_read)
        id = file_dict["last_id"]
        todo_list = file_dict["tasks"]
        print(f"File opened successfuly. {len(todo_list)} tasks loaded")
except(FileNotFoundError, json.JSONDecodeError):
    todo_list= []
    id = 0

while True:
    print("Waiting for your command")
    user_command = input(">")
    if user_command == "add":
        double = False
        name = input("Please, input the name \n >")
        for item in todo_list:
            if item["text"] == name:
                double = True
        if double == True:        
            print("Item with this name alredy exists.")
        else:
            item = {
                "id": id,
                "text": name,
                "done": False
            }                    
            id += 1
            todo_list.append(item)
            print("Item added")         
    elif user_command == "help":
        print(" 1. add - adds new item (names should be uniq), \n 2. list - shows all items, \n 3. help - shows a list of commands \n 4. done - changes item Status to done \n 5. exit - closes the programm")
    elif user_command == "list":
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
    elif user_command == "done":
        if not todo_list:
            print("No items in list")
        else:
            name = input("Please, input the id \n >")
            try:
                user_id = int(name)
            except ValueError:
                print("Please enter a number")
                continue
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
    elif user_command == "exit":
        print("Goodbye!")
        tasks_data ={
            "last_id": id,                
            "tasks": todo_list
        }
        with open("tasks.json", "w", encoding="utf-8") as write_file:
            json.dump(tasks_data, write_file)            
            print("Tasks saved successfuly.")
        break
    else:
        print("Command not found. For the full list of commands use 'help'")