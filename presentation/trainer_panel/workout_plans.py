def workout_plan():
    print("-" * 8)
    print("please select a course and a member: ")


    while True:
    
        try:
            course_choice = str(input("please enter a course: "))
    
        except:
            raise ValueError("please enter a course name")
    
        try:
            member_choice = str(input("please enter a member"))
        except:
            raise ValueError("please enter member name")
    
        #member must be in that course also course must be active \ be for the trainer not another trainer.