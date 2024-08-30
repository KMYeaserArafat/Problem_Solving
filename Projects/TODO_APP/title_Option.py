
def Option():
    print("1. Add Todo")
    print("2. Delete Todo")
    print("3. Search Todo")
    print("0. Exit")

def AddTodo(todo):
    id = int(len(todo)+1)
    note = input("Enter Todo Data : ")
    todoObj = {'id':id, 'note':note}
    todo.append(todoObj)

def DeleteTodo(todo):
    deleteId = int(input("Enter Todo Id : "))
    for x in range(len(todo)):
        if(deleteId==todo[x]['id']):
            todo.pop(x)
        else:
            print("Data is not found!!")


def SearchTodo(todo):
    searchId = int(input("Enter Search ID : "))
    for x in range(len(todo)):
        if(searchId==todo[x]['id']):
            print(f"Search ID {searchId} is Found!")
            print(f"Note : {todo[x]['note']}")


def ShowTodo(todo):
    for x in range(len(todo)):
        print("-----------------------------")
        print(f"ID : {todo[x]['id']}")
        print(f"Note: {todo[x]['note']}")
        print("-----------------------------")
    