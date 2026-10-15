def member_value(member, key):
    if isinstance(member, dict):
        return member.get(key)
    if key == 'active':
        return member.is_active
    return getattr(member, key, None)

def view_workout_plan(member, workout_plans):
    while True:
        found= False
        print("My Workout Plans")
        username = member_value(member ,"username")
        for plan in workout_plans:
            if member_value(plan.member,"username")== username:
                found= True
                print("\nClass:", plan.group_class.title)
                for exercise in plan.exercise:
                    print("--------------------")
                    print("Exercise:", exercise.name)
                    print("Sets:", exercise.sets)
                    print("Reps:", exercise.reps)
                    print("Rest Time:", exercise.rest_time)
                    print("Description:", exercise.description)
        if not found:
            print("You don't have a workout plan.")
        print("\n0. Return")
        if input("Choose an option: ") == "0":
            return
        print("Invalid choice.") 