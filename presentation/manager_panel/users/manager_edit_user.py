from presentation.manager_panel.users.members.edit_member import edit_member
from presentation.manager_panel.users.trainers.edit_trainer import edit_trainer
from infrastructure.user_repository import UserRepository


user_repository = UserRepository()

def manage_edit_user():
    
    print('-' * 8)
    print("1.Edit Member")
    print("2.Edit Trainer")

    while True:
        try:
            users_choice = int(input("Which Kind Of User Want To Add: (1-2) "))
        except:
            raise ValueError("please enter number choice")

        if users_choice == 1:
            edit_member(user_repository)

        elif users_choice == 2:
            edit_trainer(user_repository)

        else:
            print("Please enter 1, 2")
        

