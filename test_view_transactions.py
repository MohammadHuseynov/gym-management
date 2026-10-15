from test1 import os

path_file = f"{os.getcwd()}//this_test_transation.txt"

ls_information_user = []
if os.path.isfile(path_file):
    inp_username = user["username"]
    # inp_username = input("username: ")
    with open(path_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            this_information = line.split("|")
            if len(this_information) == 7 and (inp_username.strip() == this_information[0].strip()):
                # cheera 7 ta?    choon sakhtar code man injori hast ke 7 ta oonsor daare dar ghere insorat dorost nist  --->   (username, )
                ls_information_user.append(" | ".join(this_information))
    if ls_information_user != []:
        with open(f"{os.getcwd()}\\information_user.txt", "w", encoding="utf-8") as file:
            for this_user_information in ls_information_user:
                file.write(this_user_information)
                file.write("\n")
        print("Done!")
    else:
        print("--- not found information for user ---")
else:
    print("file not found")
