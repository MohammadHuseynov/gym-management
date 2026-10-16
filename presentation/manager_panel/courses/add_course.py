from services.courses.add_course import add_course

def manage_add_course(course_repository,user_repository,hall_repository):
    title = input("Enter course title (or 1 to go back): ").strip()

    
    if title == "1":
        return False

    sport_type = input("Enter sport type: ").strip()
    trainer = input("Enter trainer name: ").strip()
    hall = input("Enter hall name: ").strip()
    day = input("Enter course day: ").strip()
    time = input("Enter course time: ").strip()
    capacity = input("Enter course capacity: ").strip()
    

    
    try:
        add_course(title,sport_type,trainer,hall,day,time,capacity,course_repository,user_repository,
                hall_repository)

        print("Course added successfully!")
        return True

    except ValueError as error:
        print(error)
        return False
