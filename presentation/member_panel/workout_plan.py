def view_workout_plan(member, workout_repository):

    workout_plans = workout_repository.get_all()
    found = False
    while True:

        print("-" * 8)
        print("1.Workout Plan")
        print("2.Return")
    
        user_choice = input("please enter your choice")
        if user_choice == "1":
            for plan in workout_plans:
                if plan["member_username"].lower() == member.username.lower():
                    found = True
        
                    print(f"Course: {plan["course_title"]}")
        
                    for exercise in plan["exercises"]:
                        print("-" * 8)
                        print(f"Exercise: {exercise["name"]}")
                        print(f"Sets: {exercise["sets"]}")
                        print(f"Reps: {exercise["reps"]}")
                        print(f"Rest Time: {exercise["rest_time"]}")
                        print(f"Description: {exercise["description"]}")
        
            if not found:
                print("You don't have a workout plan.")

        elif user_choice == "2":
            return

        else:
            return

    
