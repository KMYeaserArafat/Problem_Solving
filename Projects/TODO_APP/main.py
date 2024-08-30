import title_Option


todo = []
while(True):
    try:
        print("** TODO-APPLICATION **")
        title_Option.ShowTodo(todo)
        title_Option.Option()
        option = int(input("Choose Option : "))

        if(option==1):
            title_Option.AddTodo(todo)
        elif(option==2):
            title_Option.DeleteTodo(todo)
        elif(option==3):
            title_Option.SearchTodo(todo)
        elif(option==0):
            print("Exit!!")
            break
    except:
        print("Error!!")



