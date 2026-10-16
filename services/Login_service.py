
def login_menu_presentation(all_users):

    while True:
        print("\n" + "=" * 45)
        print("  GYM MANAGEMENT SYSTEM  ")
        print("=" * 45)
        print("  1. Admin Login")
        print("  2. Trainer Login")
        print("  3. Member Login")
        print("  4. Exit")
        print("=" * 45)

        choice = input("Please select an option (1-4): ").strip()

        if choice == "1":
            user = handle_login(all_users, expected_role="Admin")
            if user:
                print(f"\nWelcome to Admin Panel, {user.name}!")
                input("\nPress Enter to return to main menu...")

        elif choice == "2":
            user = handle_login(all_users, expected_role="Trainer")
            if user:
                print(f"\nWelcome to Trainer Panel, {user.name}!")
                input("\nPress Enter to return to main menu...")

        elif choice == "3":
            user = handle_login(all_users, expected_role="Member")
            if user:
                print(f"\nWelcome to Member Panel, {user.name}!")
                input("\nPress Enter to return to main menu...")

        elif choice == "4":
            print("\nGoodbye! End of program!.")
            break

        else:
            print("\nInvalid option! Please enter a number between 1 and 4.")