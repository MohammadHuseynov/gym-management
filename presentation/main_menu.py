from presentation.manager_panel.manager_menu import manager_menu 
from presentation.trainer_panel.trainer_menu import trainer_menu
from presentation.member_panel.member_menu import member_menu

def main_menu():
    
    print('-' * 8)
    print("1.Gym Owner Login")
    print("2.Trainer Login")
    print("3.Member Login")

    while True:
        try:
            userLoginChoice = int(input("Enter your login choice (1 to 3): "))
        except ValueError:
            print("Please enter a number.")
            continue
        
        if userLoginChoice == 1:
            manager_menu()

        elif userLoginChoice == 2:
            trainer_menu()
        
        elif userLoginChoice == 3:
            member_menu()
        else:
            print("Please enter 1, 2, or 3.")