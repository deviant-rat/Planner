todo_list= []
id = 0
while True:
    print("Waiting for your command")
    user_command = input(">")
    if user_command == "add":
        double = False
        name = input("Please, input the name \n >")
        for item in todo_list:
            if item["Name"] == name:
                double = True
        if double == True:        
            print("Item with this name alredy exists.")
        else:
            item = {
                "ID": id,
                "Name": name,
                "Status": False
            }                    
            id += 1
            todo_list.append(item)
            print("Item added")         
    elif user_command == "help":
        print(" 1. add - adds new item, \n 2. list - shows all items, \n 3. help - shows a list of commands \n 4. done - changes item Status to done \n 5. exit - closes the programm")
    elif user_command == "list":
        if not todo_list:
            print('No items found')
        else:
            for item in todo_list:
                if item["Status"] == True:
                    print("[x]", end=" ")
                else:
                    print("[ ]", end=" ")
                print(item["ID"], end=" ")
                print(item["Name"])
    elif user_command == "done":
        name = input("Please, input the name \n >")
        found = False
        for item in todo_list:
            if item["Name"] == name:
                item["Status"] = True
                found = True
                break
        if found == True:
            print("Status changed successfuly")
        else:
            print("Item not found")
    elif user_command == "exit":
        print("Goodbye!")
        break
    else:
        print("Command not found. For the full list of commands use 'help'")