print("\n1- Add a new task\n2- View the tasks list\n3- Delete a current task\n4- Exit the program and view current list\n ")
user_choice = int(input("Choose a number from the above: "))
tasks_list = []

while user_choice != 4:
    if user_choice == 1:
        new_task = input("Add a new task: ")
        tasks_list.append(new_task)
        user_choice = int(input("\nChoose a number from the above: "))

    if user_choice == 2:
        print(f"The currents tasks are:\n{"\n".join(tasks_list)}")
        user_choice = int(input("\nChoose a number from the above: "))
        
    if user_choice == 3:
        print(tasks_list)
        place_of_task = int(input("\nChoose the number of the task you wish to remove: "))
        tasks_list.pop(place_of_task-1)
        print("\n".join(tasks_list))
        user_choice = int(input("\nChoose a number from the above: "))

    
print(f"Your tasks list is: {tasks_list}")






