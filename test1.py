import jdatetime
import os
from Bank import *
day_now = str(jdatetime.date.today()).split("-")


ls_test_card = [("6063997206069911", int("07"), int("1405"), "123456", "123"), ("6062997200001324", int("00"), int("1407"), "123456", "123"), ("6037997211111234", int("10"), int("1405"), "123456", "432")]
ls_tozihat = ["this for first deposit", "my balance refound", "refound"] # tozihe karbar mitone vard kone mitone vard nakone (optional) vali vard nakar "" bashe
ls_usernames = ["amin", "abas", "yosef"]
ls_random_for_user = ['10.00', '5000', '25000']
ls_bank_balance = [45000, 37000, 125000] # bank khodesh dataye valid negah midareh


def pay_validation(is_validate_card):
    if is_validate_card:
        if ls_random_for_user[i] != "":
            if ls_random_for_user[i].isdigit():
                test_inp_uesr = int(ls_random_for_user[i])
                test_bank_balance = int(ls_bank_balance[i])
                if (test_inp_uesr > 0) and (test_inp_uesr <= test_bank_balance):
                    tracking_number = user.pay(*ls_test_card[i], test_inp_uesr) # deposit chon toy bakhsh sharzh kifpol hastim
                    ls_bank_balance[i] = test_bank_balance - test_inp_uesr # ls_bank_balance[i] ---> bank an shaks
                    user.balance += test_inp_uesr
                    ls_transactons.append((ls_usernames[i],"deposit", user.balance, "/".join(day_now), ls_tozihat[i] if ls_tozihat[i] != "" else "None", tracking_number, "success")) # sucess chon inja dige sharzh anjam shode va bayad check konim ke tracking_number hatman yekta bashad 
                else:
                    print("error mojodi shoma kafi nemibashad")
            else:
                print('vorodi bayad adad sahih bashad')
        else:
            print('mablgh vard nashode')
    else:
        print("error cart shoma motabar nist")

ls_transactons = []
for i in range(len(ls_usernames)):
    user = ls_usernames[i]
    user = API() # baraye test hst vali dar asl in user az ghabre hast toy oop chon toy bkhsh afzodan karbar, karbar mishe object (farz man chon tamame datash to khodesh save mishe)
    user.balance = 0 # baraye test hst vali dar asl in mored az ghabre hast chon toy bkhsh afzodan karbar attribute balancy sapt mishode
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
