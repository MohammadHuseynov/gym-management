def withdraw_member(member, course_title, registration_repository):
    """Deactivate a member's active course registration without deleting it.

    The registration repository must expose ``get_all()`` and
    ``update_status(transaction_id, status)``.
    """
    if member is None:
        raise ValueError("Member information is required.")

    member_username = _member_value(member, "username")
    if not member_username:
        raise ValueError("Member username is required.")

    course_title = str(course_title or "").strip()
    if not course_title:
        raise ValueError("Course title cannot be empty.")

    get_all = getattr(registration_repository, "get_all", None)
    update_status = getattr(registration_repository, "update_status", None)
    if not callable(get_all) or not callable(update_status):
        raise ValueError(
            "Registration repository must provide get_all() and update_status()."
        )

    registration = next(
        (item for item in get_all()
         if item.get("member_username", "").strip().lower() == member_username.lower()
         and item.get("course_title", "").strip().lower() == course_title.lower()
         and item.get("status", "active").strip().lower() == "active"),
        None,
    )
    if registration is None:
        raise ValueError("You do not have an active registration for this course.")

    transaction_id = registration.get("transaction_id", "").strip()
    if not transaction_id:
        raise ValueError("Registration is missing its transaction ID.")
    if not update_status(transaction_id, "inactive"):
        raise ValueError("Could not update the course registration.")

    registration["status"] = "inactive"
    return registration


def _member_value(member, key):
    if isinstance(member, dict):
        return str(member.get(key, "")).strip()
    return str(getattr(member, key, "")).strip()
