
lst = []
line = "-----------------------------"


def display_inbox():
    for todo in lst:
        print(todo)
        print(line)


def add_todo(todo):
    lst.append(todo)
    print("Todo successfully added.")


def complete_todo():
    pass


def delete_todo():
    pass


todo = {"Undone": input("Input your new todo:\n")}

print(todo)
