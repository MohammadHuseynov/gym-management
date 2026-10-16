from datetime import datetime
from uuid import uuid4


def enroll_member(member, course_title, course_repository, registration_repository,
                  subscription_repository=None):
    """Enroll a member in an active course and return the registration record.

    Repositories are intentionally passed in so this service stays consistent
    with the other course services. A registration repository should expose
    ``get_all()`` and ``add(registration)``; its records use member_username,
    course_title, transaction_id, registered_at, and status fields.
    """
    if member is None:
        raise ValueError("Member information is required.")

    member_username = _member_value(member, "username")
    if not member_username:
        raise ValueError("Member username is required.")

    course_title = str(course_title or "").strip()
    if not course_title:
        raise ValueError("Course title cannot be empty.")

    courses = course_repository.get_all()
    selected_course = next(
        (course for course in courses
         if course["title"].strip().lower() == course_title.lower()),
        None,
    )
    if selected_course is None:
        raise ValueError("Course not found.")
    if not selected_course["is_active"]:
        raise ValueError("Cannot enroll in an inactive course.")

    if subscription_repository is not None:
        _require_active_subscription(member_username, subscription_repository)

    registrations = _registrations(registration_repository)
    course_registrations = [
        registration for registration in registrations
        if registration.get("course_title", "").strip().lower()
        == selected_course["title"].strip().lower()
        and registration.get("status", "active").lower() == "active"
    ]

    capacity = int(selected_course["capacity"])
    if len(course_registrations) >= capacity:
        raise ValueError("This course has reached its capacity.")

    if any(registration.get("member_username", "").lower() == member_username.lower()
           for registration in course_registrations):
        raise ValueError("You are already enrolled in this course.")

    registration = {
        "member_username": member_username,
        "course_title": selected_course["title"],
        "transaction_id": uuid4().hex[:12].upper(),
        "registered_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "active",
    }

    add_registration = getattr(registration_repository, "add", None)
    if not callable(add_registration):
        raise ValueError("Registration repository must provide an add() method.")
    add_registration(registration)

    return registration


def _member_value(member, key):
    if isinstance(member, dict):
        return str(member.get(key, "")).strip()
    return str(getattr(member, key, "")).strip()


def _registrations(registration_repository):
    if registration_repository is None:
        return []
    get_all = getattr(registration_repository, "get_all", None)
    if not callable(get_all):
        raise ValueError("Registration repository must provide a get_all() method.")
    return get_all()


def _require_active_subscription(member_username, subscription_repository):
    get_all = getattr(subscription_repository, "get_all", None)
    subscriptions = get_all() if callable(get_all) else subscription_repository
    if subscriptions is None:
        raise ValueError("An active subscription is required to enroll.")

    for subscription in subscriptions:
        username = str(subscription.get("member_username", "")).strip()
        status = str(subscription.get("status", "")).strip().lower()
        if username.lower() == member_username.lower() and status == "active":
            return

    raise ValueError("An active subscription is required to enroll.")
