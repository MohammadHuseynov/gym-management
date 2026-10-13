import jdatetime # get jalali Date time
import os
from random import randint
from Bank import *
day_now_now = str(jdatetime.date.today()).split("-")



ls_enter_transactons = []

int_vorodi_pol_user = input("meghdar sharzh: ")
user_name = API() #?? user for test -> montazer code bachehaaa

inp_card = input("enter id card: ")
inp_exp_month = input("enter exp month: ")
inp_exp_year = input("enter inp exp year: ")
inp_cvv2 = input("enter code cvv2 card: ")
inp_password = input("enter password: ")
user_name.information_card_user = (inp_card, inp_exp_month, inp_exp_year, inp_password, inp_cvv2)# barayee eteebar sanjiiii

def validation_card(tup_information, day_now): # while toy bakhsh eshterak
    if (day_now[0].isdigit() == True) and (day_now[1].isdigit() == True) and (tup_information[1].isdigit() == True) and (tup_information[2].isdigit() == True):
        year_now = int(day_now[0]) # hameyeh int haa error handling beshan
        month_now = int(day_now[1])
        month_card_user = int(tup_information[1])
        year_card_user = int(tup_information[2])
        if (year_card_user < year_now): # int bodan ya nabodan check shavad barayeh error handling
            print('error kart namotabar ast tarikh cart khod ra check konid')
            return False
        elif (year_card_user > year_now):
            is_validation_card = user_name.validate(tup_information[0], month_card_user, year_card_user,tup_information[3], tup_information[4])
            return is_validation_card
        else:
            if month_card_user >= month_now:
                is_validation_card = user_name.validate(tup_information[0], month_card_user, year_card_user,tup_information[3], tup_information[4])
                return is_validation_card
            else:
                print("mahhe kart shoma motabar nist")
                return False
    else:
        print("vorodi bayad adade sahih bashad") 
        return False

# is_veealidate_card
def deposit(is_veealidate_card, int_vorodi_pol):
    if int_vorodi_pol == "":
        return("mablagh khali ghbel ghbool nist")
    elif int_vorodi_pol.isdigit() == False:
        return('meghdar barayeh sharzzh bayad adad sahiih bashad')
    elif is_veealidate_card == False:
        return("error kart namotabar ast tarikh cart khod ra check konid")
    elif (int_vorodi_pol.isdigit() == True) and (is_veealidate_card==True):
        test_inp_uesr = int(int_vorodi_pol)
        if (test_inp_uesr > 0):
            month_card_user = int(user_name.information_card_user[1])
            year_card_user = int(user_name.information_card_user[2])
            t = (user_name.information_card_user[0], month_card_user, year_card_user, user_name.information_card_user[3], user_name.information_card_user[4])
            tracking_number = user_name.pay(*t, test_inp_uesr)
            user_name.balance += test_inp_uesr
            tozih = input(f"if you don't want to write anything, just press enter\ntransaction explanation text: ")
            time_now = jdatetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            trx_deposit = (user_name, "deposit", test_inp_uesr, time_now, tozih if tozih != "" else "None", tracking_number, "success") # user_name.name   masaaaalan
            ls_enter_transactons.append(trx_deposit)
            return True
        else:
            print("adad bayad yek adad sahiih va mosbat bashad")
            return False

def new_pay(price_subscription):
    if user_name.balance >= price_subscription:
        user_name.balance -= price_subscription
        tozih = input(f"if you don't want to write anything, just press enter\ntransaction explanation text: ")
        time_now = jdatetime.datetime.now()
        new_pay_trx = (user_name, "buy subscription", price_subscription, time_now.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price_subscription, user_name.information_card_user[0]), "success")
        ls_enter_transactons.append(new_pay_trx)
        return True # chooon bayad eshterak karabr active beshe
    else:
        print("mojodi shoma nakaafi")
        time_now = jdatetime.datetime.now()
        new_pay_trx = (user_name, "buy subscription", price_subscription, time_now.strftime("%Y/%m/%d %H:%M:%S"), "Insufficient funds", user_name.generate_payment_id(price_subscription, user_name.information_card_user[0]), "failed")
        ls_enter_transactons.append(new_pay_trx)
        return False



def get_end_time(start_time, months):
    end_month = start_time.month + months
    end_year = start_time.year
    if end_month > 12:
        end_month -= 12
        end_year += 1
    end_day = min(start_time.day, jdatetime.j_days_in_month[end_month - 1])
    # -1 barayeh in hast ke python az 0 mishmareh   jdatetime.j_days_in_month -> [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]   in onser 0 mishe mah aval khodemoon   mah akhar mishe 12 valii toy in list mishe 11
    end_time = start_time.replace(year=end_year, month=end_month, day=end_day)
    return end_time


with open(f"{os.getcwd()}//this_test_transation.txt", "a", encoding="utf-8") as file:
    for i in ls_enter_transactons:
        result = "|".join(str(x) for x in i)
        file.write(result)
        file.write("\n")
