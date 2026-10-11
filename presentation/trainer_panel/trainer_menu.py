import main_menu 

def trainer_menu():

    print("1.view courses")
    print("2.manage member workout plan")
    print("3.Exit")

    while True:
        try:
            trainer_choice = int(input("Enter your choice: "))

        except:
            print("Please enter the number choice.")
            continue

        if trainer_choice == 1:
            print("goes to view courses")
        elif trainer_choice == 2:
            print("goes to manage member work out plan page")

        elif trainer_choice == 3:
            return main_menu.main_menu()
        