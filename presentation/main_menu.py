from manager_panel import *
from trainer_panel import *
from member_panel import *


print("1.Gym owner login")
print("2.Coach login")
print("3.Member login")



while True:
    try:
        userLoginChoice = int(input("Enter your login choice (1 to 3): "))
    except ValueError:
        print("Please enter a number.")
        continue

    if userLoginChoice == 1:
        print("take user to the manager panel")
        break
    elif userLoginChoice == 2:
        print("take user to trainer panel")
        break
    elif userLoginChoice == 3:
        print("take user to member panel")
        break
    else:
        print("Please enter 1, 2, or 3.")