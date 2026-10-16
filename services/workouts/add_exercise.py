from model.workout_plan import Exercise


def create_workout_plan(trainer,member_username,course_title,exercises,user_repository,course_repository,
                    workout_repository):
    
    selected_member = None

    for user in user_repository.get_all():
        if user["username"].lower() == member_username.lower():
            if user["role"].lower() != "member":
                raise ValueError("The selected user is not a member.")

            if not user["is_active"]:
                raise ValueError("The selected member is inactive.")

            selected_member = user
            break

    if selected_member is None:
        raise ValueError("Member not found.")

    selected_course = None

    for course in course_repository.get_all():
        if course["title"].lower() == course_title.lower():
            selected_course = course
            break

    if selected_course is None:
        raise ValueError("Course not found.")

    if selected_course["trainer"].lower() != trainer.name.lower():
        raise ValueError("This course does not belong to you.")

    if not selected_course["is_active"]:
        raise ValueError("Cannot create a plan for an inactive course.")

    if not exercises:
        raise ValueError("Add at least one exercise.")

    for exercise in exercises:
        if not exercise.name.strip():
            raise ValueError("Exercise name cannot be empty.")

        if exercise.sets <= 0 or exercise.reps <= 0:
            raise ValueError("Sets and reps must be greater than zero.")

        if not str(exercise.rest_time).strip():
            raise ValueError("Rest time cannot be empty.")

    workout_repository.add(
        selected_member["username"],
        selected_course["title"],
        exercises
    )

    return True
