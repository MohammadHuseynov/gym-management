import jdatetime
import os
from Bank import *
day_now = str(jdatetime.date.today()).split("-")

ls_test_card = [("6037997206064623", int("05"), int("1405"), "123456", "123"), ("6037997200004623", int("07"), int("1407"), "123456", "123"), ("6037997211114623", int("10"), int("1405"), "123456", "432")]
ls_tozihat = ["this for first deposit", "my balance refound", "refound"] # tozihe karbar mitone vard kone mitone vard nakone (optional) vali vard nakar "" bashe
ls_usernames = ["amin", "abas", "yosef"]
ls_random_for_user = [45000, 37000, 125000]
ls_bank_balance = ['10000000', '50000', '2500000']

def pay_validation(is_validate_card):
    if is_validate_card:
        if (ls_random_for_user[i] > 0) and (ls_random_for_user[i] <= int(ls_bank_balance[i])):
            tracking_numberper = user.pay(*ls_test_card[i], ls_random_for_user[i]) # deposit chon toy bakhsh sharzh kifpol hastim
            ls_bank_balance[i] = int(ls_bank_balance[i]) - ls_random_for_user[i]
            user.balance += int(ls_random_for_user[i])
            ls_transactons.append((ls_usernames[i],"deposit", user.balance, "/".join(day_now), ls_tozihat[i] if ls_tozihat[i] != "" else "None", tracking_numberper, "success")) # sucess chon inja dige sharzh anjam shode
        else:
            print("error mojodi shoma kafi nemibashad")
    else:
        print("error cart shoma motabar nist")

ls_transactons = []
for i in range(len(ls_usernames)):
    user = ls_usernames[i]
    user = API() # baraye test hst vali dar asl in user az gharl hast toy oop chon toy bkhsh afzodan karbar karbar mishe object (farz man)
    user.balance = 0 # baraye test hst vali dar asl in mored az gharl hast chon toy bkhsh afzodan karbar attribute sapt shode
    task = tuple(ls_test_card[i])
    if (task[2] < int(day_now[0])):
        print('error kart namotabar ast tarikh cart khod ra check konid')
    elif (task[2] > int(day_now[0])):
            is_validation_card = user.validate(*task)
            pay_validation(is_validation_card)
    elif (task[2] == int(day_now[0])): 
        if task[1] >= int(day_now[1]):
            is_validation_card = user.validate(*task)
            pay_validation(is_validation_card)
        else:
            print("tarikhe kart shoma tamom shodeh")
with open(f"{os.getcwd()}//this_test_transation.txt", "a", encoding="utf-8") as file:
    for i in ls_transactons:
        result = "|".join(str(x) for x in i)
        file.write(result)
        file.write("\n")


for i in ls_transactons:
    print(i)

