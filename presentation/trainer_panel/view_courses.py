from services.courses.get_courses import get_courses

def view_course(trainer, course_repository):
    courses = get_courses(course_repository)
    found = False
    while True:
        print("-" * 8)
        print("1.Show Courses")
        print("2.Return")
    
        user_choice = input("Enter what you want to do: ")

        if user_choice == "1":
            for course in courses:
                if course["trainer"].lower() == trainer.name.lower():
                    found = True

                    print("-" * 8)
                    print(f"Title: {course["title"]}")
                    print(f"Sport Type: {course["sport_type"]}")
                    print(f"Hall: {course["hall"]}")
                    print(f"Day: {course["day"]}")
                    print(f"Time: {course["time"]}")
                    print(f"Capacity: {course["capacity"]}")
        
                    if course["is_active"]:
                        print("Status: Active")
                    else:
                        print("Status: Inactive")
        
                    
            if not found:
                print("You don't have any assigned courses.")

        elif user_choice == "2":
            return

        else: 
            print("please enter correctly")
        

    
