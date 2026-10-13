from presentation.manager_panel.users.members.add_member import add_member
from presentation.manager_panel.users.trainers.add_trainer import add_trainer



def manage_add_user():

    print('-' * 8)
    print("1.Add Member")
    print("2.Add Trainer")

    while True:
        try:
            users_choice = int(input("Which Kind Of User Want To Add: (1-2) "))
        except:
            raise ValueError("please enter number choice")

        if users_choice == 1:
            add_member()

        elif users_choice == 2:
            add_trainer()

        else:
            print("Please enter 1, 2")
        


        