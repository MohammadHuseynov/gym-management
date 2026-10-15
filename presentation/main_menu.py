from presentation.manager_panel.manager_menu import manager_menu
from presentation.trainer_panel.trainer_menu import trainer_menu
from presentation.member_panel.member_menu import member_menu
from services.users.login_user import handle_login
from infrastructure.user_repository import UserRepository
from infrastructure.hall_repository import HallRepository
from infrastructure.course_repository import CourseRepository


def main_menu():
    user_repository = UserRepository()
    hall_repository = HallRepository()
    course_repository = CourseRepository()

    while True:
        print("-" * 8)
        print("1.Gym Owner Login")
        print("2.Trainer Login")
        print("3.Member Login")
        print("4.Exit")

        user_choice = input("Enter your login choice (1 to 4): ").strip()

        if user_choice == "4":
            print("Goodbye!")
            break

        roles = {"1": "manager", "2": "trainer", "3": "member"}

        if user_choice not in roles:
            print("Please enter 1, 2, 3, or 4.")
            continue

        role = roles[user_choice]

        user = handle_login(user_repository, role)

        if user is None:
            continue

        if role == "manager":
            manager_menu(user_repository, hall_repository, course_repository)
        elif role == "trainer":
            trainer_menu(user_repository, hall_repository, course_repository)
        elif role == "member":
            member_menu(user_repository, hall_repository, course_repository)