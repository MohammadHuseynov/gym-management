from datetime import date


def member_value(member, key):
    if isinstance(member, dict):
        return member.get(key)
    if key == 'active':
        return member.is_active
    return getattr(member, key, None)


def member_menu(member, classes, subscriptions, workout_plans, registrations=None, wallet_menu=None):
    if registrations is None:
        registrations = []

    while True:
        print('\n----- Member Panel -----')
        print('1. Profile & Subscription')
        print('2. Wallet')
        print('3. Classes')
        print('4. Workout Plans')
        print('0. Logout')
        choice = input('Choose an option: ')

        if choice == '1':
            profile_subscription_menu(member, subscriptions)
        elif choice == '2':
            if wallet_menu is None:
                print('Wallet section is not connected yet.')
            else:
                wallet_menu(member)
        elif choice == '3':
            classes_menu(member, classes, registrations)
        elif choice == '4':
            workout_plan_menu(member, workout_plans)
        elif choice == '0':
            print('Logged out.')
            return
        else:
            print('Invalid choice.')
#منو ورودی کاربر

def profile_subscription_menu(member, subscriptions):
    while True:
        print('\n--- Profile & Subscription ---')
        print('1. My Profile')
        print('2. My Subscription')
        print('0. Back')
        choice = input('Choose an option: ')

        if choice == '1':
            profile_menu(member)
        elif choice == '2':
            subscription_menu(member, subscriptions)
        elif choice == '0':
            return
        else:
            print('Invalid choice.')


def profile_menu(member):
    while True:
        print('\n--- My Profile ---')
        print('Name:', member_value(member, 'name'))
        print('Username:', member_value(member, 'username'))
        print('Email:', member_value(member, 'email'))
        if member_value(member, 'active'):
            print('Account Status: Active')
        else:
            print('Account Status: Inactive')

        print('\n0. Back')
        if input('Choose an option: ') == '0':
            return
        print('Invalid choice.')
#نمایش پروفایل عضو بعد از ورود

def subscription_menu(member, subscriptions):
    while True:
        print('\n--- My Subscription ---')
        username = member_value(member, 'username')
        member_subscriptions = []
        for subscription in subscriptions:
            if subscription['member_username'] == username:
                member_subscriptions.append(subscription)

        if not member_subscriptions:
            print("You don't have a subscription.")
        else:
            subscription = member_subscriptions[-1]
            print('Type:', subscription['type'])
            print('Amount:', subscription['amount'])
            print('Start Date:', subscription['start_date'])
            print('End Date:', subscription['end_date'])
            if subscription['end_date'] >= date.today().isoformat():
                print('Status: Active')
            else:
                print('Status: Expired')

        print('\n0. Back')
        if input('Choose an option: ') == '0':
            return
        print('Invalid choice.')
#نمایش وضعیت اشتراک

def classes_menu(member, classes, registrations):
    while True:
        print('\n--- Classes Menu ---')
        print('1. My Active Classes')
        print('2. Available Classes')
        print('0. Back')
        choice = input('Choose an option: ')

        if choice == '1':
            my_classes_menu(member, classes, registrations)
        elif choice == '2':
            available_classes_menu(classes, registrations)
        elif choice == '0':
            return
        else:
            print('Invalid choice.')
#قسمت منو کلاس ها

def enrolled_count(gym_class, registrations):
    count = 0
    for registration in registrations:
        if registration['class_title'] == gym_class['title'] and registration['status'] == 'active':
            count += 1
    return count


def show_available_classes(classes, registrations):
    print('\n--- Available Classes ---')
    found = False
    for gym_class in classes:
        remaining = gym_class['capacity'] - enrolled_count(gym_class, registrations)
        if gym_class['active'] and remaining > 0:
            found = True
            print('Title:', gym_class['title'])
            print('Sport:', gym_class['sport_type'])
            print('Trainer:', gym_class['trainer_id'])
            print('Hall:', gym_class['hall_name'])
            print('Day:', gym_class['day'])
            print('Time:', gym_class['time'])
            print('Remaining Capacity:', remaining)
            print('--------------------')
    if not found:
        print('No available classes.')
#ثبت نام عضو- نیاز به بروز کردن کد طبق نوشتن بچه ها داره-کد پیگیری صادر نمیکنه

def available_classes_menu(classes, registrations):
    while True:
        show_available_classes(classes, registrations)
        print('0. Back')
        if input('Choose an option: ') == '0':
            return
        print('Invalid choice.')


def show_my_classes(member, classes, registrations):
    print('\n--- My Active Classes ---')
    found = False
    username = member_value(member, 'username')
    for registration in registrations:
        if registration['member_username'] == username and registration['status'] == 'active':
            for gym_class in classes:
                if gym_class['title'] == registration['class_title']:
                    found = True
                    print('Title:', gym_class['title'])
                    print('Trainer:', gym_class['trainer_id'])
                    print('Hall:', gym_class['hall_name'])
                    print('Day:', gym_class['day'])
                    print('Time:', gym_class['time'])
                    print('--------------------')
                    break
    if not found:
        print('You are not enrolled in any classes.')
#کلاس های فعال

def my_classes_menu(member, classes, registrations):
    while True:
        show_my_classes(member, classes, registrations)
        print('0. Back')
        if input('Choose an option: ') == '0':
            return
        print('Invalid choice.')


def workout_plan_menu(member, workout_plans):
    while True:
        found = False
        print('\n--- My Workout Plans ---')
        username = member_value(member, 'username')
        for plan in workout_plans:
            if member_value(plan.member, 'username') == username:
                found = True
                print('\nClass:', plan.group_class.title)
                for exercise in plan.exercises:
                    print('--------------------')
                    print('Exercise:', exercise.name)
                    print('Sets:', exercise.sets)
                    print('Reps:', exercise.reps)
                    print('Rest Time:', exercise.rest_time)
                    print('Description:', exercise.description)
        if not found:
            print("You don't have a workout plan.")

        print('\n0. Back')
        if input('Choose an option: ') == '0':
            return
        print('Invalid choice.')
#برنامه‌های ورزشی کاربر