
lst = []
line = "-----------------------------"


def display_inbox(lst):
    for todo in lst:
        print(f"todo number {lst.index(todo)}:\n {todo[1]}")
        print(line)


def add_todo(todo):
    lst.append(todo)
    print("Todo successfully added.")


def complete_todo():
    pass


def delete_todo():
    pass


display_inbox(lst)
command = input("Do you want to complete a todo (c)? Delete a \
todo (d)? or create a new todo (n)? input 'c', 'd', or 'n':\n")
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


# todo = ["Undone", input("Input your new todo:\n")]

print(todo)
