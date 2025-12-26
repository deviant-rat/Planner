todo_list= []
id = 0
while True:
    print("Waiting for your command")
    user_command = input(">")
    if (user_command == "add"):
        name = input("Please, input the name \n >")
        if id == 0:
            item = {
                    "ID": id,
                    "Name": name,
                    "Status": False
            }
            id += 1
            todo_list.append(item)
            continue
        for item in todo_list:
            if item["Name"] == name:
                print("Item with this name alredy exists.")
                continue
            else:
                item = {
                    "ID": id,
                    "Name": name,
                    "Status": False
                }
                id += 1
                todo_list.append(item)
    elif(user_command == "help"):
        print("1. add - adds new item, \n help 2. list - shows all items, \n 3. help - shows a list of commands \n 4. done - changes item Status to done \n 5. exit - closes the programm")
    elif(user_command == "list"):
        for item in todo_list:
            if item["Status"] == True:
                print("[x]", end=" ")
            else:
                print("[ ]", end=" ")
            print(item["ID"], end=" ")
            print(item["Name"])
    elif(user_command == "done"):
        name = input("Please, input the name \n >")
        for item in todo_list:
            if item["Name"] == name:
                item["Status"] = True
    elif(user_command == "exit"):
        print("Goodbye!")
        break
    else:
        print("Command not found. For the full list of commands use 'help'")