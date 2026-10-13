
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
                # TODO: Redirect to Admin Panel (Section 2)
                print(f"\n✅ Welcome to Admin Panel, {user.name}!")
                # admin_panel(user) will be called here later
                input("\nPress Enter to return to main menu...")

        elif choice == "2":
            user = handle_login(all_users, expected_role="Trainer")
            if user:
                # TODO: Redirect to Trainer Panel (Section 3)
                print(f"\n✅ Welcome to Trainer Panel, {user.name}!")
                # trainer_panel(user) will be called here later
                input("\nPress Enter to return to main menu...")

        elif choice == "3":
            user = handle_login(all_users, expected_role="Member")
            if user:
                # TODO: Redirect to Member Panel (Section 4)
                print(f"\n✅ Welcome to Member Panel, {user.name}!")
                # member_panel(user) will be called here later
                input("\nPress Enter to return to main menu...")

        elif choice == "4":
            print("\nGoodbye! End of program!.")
            break

        else:
            print("\nInvalid option! Please enter a number between 1 and 4.")