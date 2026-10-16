from services.courses.withdraw_member import withdraw_member


def quit_course(member, registration_repository):
    """Let a member choose and deactivate one of their active registrations."""
    if member is None or registration_repository is None:
        print("Member registration information is unavailable.")
        return False

    member_username = _member_value(member, "username")
    get_all = getattr(registration_repository, "get_all", None)
    if not member_username or not callable(get_all):
        print("Member registration information is unavailable.")
        return False

    active_registrations = [
        registration for registration in get_all()
        if registration.get("member_username", "").strip().lower() == member_username.lower()
        and registration.get("status", "active").strip().lower() == "active"
    ]
    if not active_registrations:
        print("You have no active course registrations.")
        return False

    print("-" * 8)
    print("YOUR ACTIVE COURSES")
    for number, registration in enumerate(active_registrations, start=1):
        print(f"{number}. {registration['course_title']}")
    print("0. Return")

    choice = input("Choose a course to quit: ").strip()
    if choice == "0":
        return False
    if not choice.isdigit() or not 1 <= int(choice) <= len(active_registrations):
        print("Please choose a valid course number.")
        return False

    selected = active_registrations[int(choice) - 1]
    confirmation = input(
        f"Are you sure you want to quit {selected['course_title']}? (y/n): "
    ).strip().lower()
    if confirmation not in ("y", "yes"):
        print("Withdrawal cancelled.")
        return False

    try:
        withdrawn = withdraw_member(
            member, selected["course_title"], registration_repository
        )
    except ValueError as error:
        print(f"Could not withdraw: {error}")
        return False

    print(f"You have quit {withdrawn['course_title']}.")
    print(f"Registration {withdrawn['transaction_id']} is now inactive.")
    return True


def _member_value(member, key):
    if isinstance(member, dict):
        return str(member.get(key, "")).strip()
    return str(getattr(member, key, "")).strip()
