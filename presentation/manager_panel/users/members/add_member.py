from model.user import User

userClass = User

def add_member():
    #these must be in service logic not in presentation layer:
    userClass.name = input("Enter members name: ")
    userClass.username = input("Enter member username: ")
    userClass.password = input("Enter member user password: ")
    userClass.email = input("Enter user email: ")
    userClass.is_active = input("Enter user status (Active\Deactive): ")
