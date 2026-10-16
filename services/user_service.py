from model.user import User
from auth_service import *


def add_member():

    userClass = User()

    while True:
      print('-' * 8)
      print("Adding new user")

      userClass.name = input("Enter the name of the user: ")

      userClass.username = input("Enter the username of the user:(it must be unique!)")

      if not is_username_unique(username):
        print("Username already exists!")
        return
      
      userClass.password = input("Enter the password of the user: ")
      if not validate_password(password):
        print("Password must be at least 8 characters long and contain only english characters and @ or &!")
        return
      
      userClass.email = input("Enter the email of the user: ")
      if validate_email(email) is None:
        print("Email is not valid!")
        return
      
      userClass.role = input("Enter the role of the user:(memeber/trainer)")
      if role not in ['trainer', 'member']:
        print("role must be 'trainer' or 'member'")
        return
      Users_List.append(user)
      print("User added successfully!")
      break