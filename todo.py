
lst = []
line = "-----------------------------"


def display_inbox(lst):
    for todo in lst:
        print(f"todo number {lst.index(todo)}:\n {todo[1]}")
        print(line)
exit = False
while not exit:
    display_inbox(lst)
    command = input("Do you want to complete a todo (c)? Delete a todo (d)? \
    Create a new todo (n) or exit the program (e)? input 'c', 'd', 'n' or 'e':\n")
    if command == "c":
        n = input("input the desired todo number:\n")
        todo = lst[n]
        if todo[0] == 1:
            print("The todo is already done!\n")
        elif todo[0] == 0:
            todo[0] = 1
            print(f"todo {n} is now done!")
        else:
            print("Invalid todo number.")
    elif command == "d":
        n = input("Enter the soon to be deleted todo number:\n")
        todo = lst[n]
        if todo:
            lst.pop(n)
        else:
            print("Invalid todo number.")
    elif command == "n":
        todo = input("What needs to be done?\n")
        lst.append(["undone", todo])
        print("New todo added.")
    elif command == "e":
        exit = True
    else:
        "Invalid command."