from infrastructure.user_repository import UserRepository
from presentation.manager_panel.users.members.add_member import add_member
from presentation.manager_panel.users.trainers.add_trainer import add_trainer


def manage_add_user(user_repository):
    
    while True:
        print("-" * 8)
        print("1.Add Member")
        print("2.Add Trainer")
        print("3.Return")
        
        try:
            users_choice = int(input("Which kind of user do you want to add? (1-2): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if users_choice == 1:
            add_member(user_repository)
            return

        elif users_choice == 2:
            add_trainer(user_repository)
            return
        
        elif users_choice == 3:
            return
        
        else:
            print("Please enter 1 or 2.")
