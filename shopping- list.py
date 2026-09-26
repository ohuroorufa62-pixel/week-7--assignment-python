# Part B - Shopping List Manager

shopping_list = []

while True:
    print("\nadd / remove / show / done")
    choice = input("Choose an option: ").lower()

    if choice == "add":
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print(f"{item} added to your list.")

    elif choice == "remove":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Your shopping list:")
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose add, remove, show, or done.")