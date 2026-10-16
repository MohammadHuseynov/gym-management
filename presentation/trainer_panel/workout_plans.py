from model.workout_plan import Exercise
from services.courses.get_courses import get_courses
from services.workouts.add_exercise import create_workout_plan


def workout_plan(trainer, user_repository, course_repository,workout_repository):
    courses = get_courses(course_repository)
    trainer_courses = []
    exercises = []

    for course in courses:
        if course["trainer"].lower() == trainer.name.lower():
            trainer_courses.append(course)

    if not trainer_courses:
        print("You don't have any assigned courses.")
        return

    while True:
        print("My Courses")
        print("-" * 8)

        for index, course in enumerate(trainer_courses, start=1):
            status = "Active" if course["is_active"] else "Inactive"
            print(f"{index}. {course['title']} ({status})")

        print("0.Return")

        choice = input("Select a course: ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not (1 <= int(choice) <= len(trainer_courses)):
            print("Invalid choice.")
            continue

        selected_course = trainer_courses[int(choice) - 1]

        if not selected_course["is_active"]:
            print("You cannot create a workout plan for an inactive course.")
            continue

        member_username = input("Enter the member's username: ").strip()

        if not member_username:
            print("Username cannot be empty")
            continue


        while True:
            print("Enter Exercise Details")

            name = input("Exercise name: ").strip()

            if not name:
                print("Exercise name cannot be empty")
                continue

            try:
                sets = int(input("Sets: "))
                reps = int(input("Reps: "))

                if sets <= 0 or reps <= 0:
                    print("Sets and reps must be greater than zero")
                    continue

            except ValueError:
                print("Sets and reps must be integers.")
                continue

            rest_time = input("Rest time: ").strip()
            description = input("Description: ").strip()

            if not rest_time:
                print("Rest time cannot be empty")
                continue

            exercise = Exercise(name, sets, reps, rest_time, description)

            exercises.append(exercise)

            print("Exercise added")

            another = input("Add another exercise? (y/n): ").strip().lower()

            if another != "y":
                break

        try:
            create_workout_plan(trainer,member_username,selected_course["title"],exercises,user_repository,
                course_repository,workout_repository)

            print("Workout plan saved successfully")

        except ValueError as error:
            print(f"Error: {error}")


