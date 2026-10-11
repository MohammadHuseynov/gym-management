import os

inp_path = input("enter path file: ").strip()
is_path = os.path.exists(inp_path)
inp_name_file = input("enter file for read: ").strip()
is_file = os.path.isfile(f"{inp_path}\\{inp_name_file}")

ls_information_user = []
if (is_path == True) and (is_file == True):
    path_file = f"{inp_path}\\{inp_name_file}"
    inp_username = input("username: ")
    with open(path_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            this_information = line.split("|")
            # print(this_information)
            if len(this_information) == 7 and (inp_username.strip() == this_information[0].strip()):
                ls_information_user.append(" | ".join(this_information)) # zipfill(naaaaaaa rjust yaa hamchin chizy hast) bezan rooosh ba tabeh bezaneh
                print(this_information)
    if ls_information_user != []:
        with open(f"{os.getcwd()}\\information_user.txt", "w", encoding="utf-8") as file:
            for this_user_information in ls_information_user:
                file.write(this_user_information)
                file.write("\n")
        print("Done!")
    else:
        print("--- not found information for user ---")
else:
    print(f"error: masir dorost vard nashode! '{inp_path}\\{inp_name_file}' namotabar ast")
