import re

def validate_password(password):
    all_constraints = re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9\s]).{8,}$", password)

    return bool(all_constraints)


def validate_email(email):
    pattern = r"^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.fullmatch(pattern, email))



def get_user_status():
    while True:
        print("\nSelect account status:")
        print("1.Active")
        print("2.Inactive")

        choice = input("Choose (1-2): ").strip()

        if choice == "1":
            return True

        elif choice == "2":
            return False

        else:
            print("Invalid choice. Please enter 1 or 2.")
