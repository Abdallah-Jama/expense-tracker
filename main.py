while True:
    
    print("1. Add expenses")
    print("2. View expenses" )
    print("3. Total spending")
    print("4. Category summary")
    print("5. Search expenses" )
    print("6. Exit ")

    user = input("choose: ")

    if user in ["1", "2", "3", "4", "5"]:
        print("Coming soon")
    elif user == "6":
        print("Goodbye.")
        break
    else:
        print("Invaild choice")



        