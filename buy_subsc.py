

# رفیق به نظرم که ایرادی نداره برای فعلا و ظاهرا اماده است برای کامیت :)

from test1 import *

ls_subscriptions = [("1 Months", 10000), ("3 Months", 25000), ("6 Months", 45000)] # (subscription, subscription fee)
# sub, price  nabayad float bashand  agar int nabashad error mishe masalan 1 mah 2 mah naaa bashe 1.1 3.3  ....

# ls_test_user_balance = [45000, 37000, 43000] # balance karbar baydad save beshe yaa vaghti barname basteh shode 0 mishan balance hamey karbaran?    mooooooohhhhhmmmmm



print("="*(5*10))

for i in ls_subscriptions:
    print(*i, sep=" ---> ")
print("\nplan A for 1 monts\nplan B for 3 monts\nplan C for 6 monts\nand for back enter 'BACK'.\njust enter only A or B or C.")

print("="*(5*10))


choice_plan = input("What is your choice plan? ")
while choice_plan != "BACK":# choice_plan != "BACK":
    if choice_plan == "A": # pay subscribtion 1 monts
        subc, price = ls_subscriptions[0]
        print(subc, price)
        number_months = int(subc.split()[0].strip())
        buy_time_subscription = jdatetime.datetime.now()
        if new_pay(price):
            tozih = input(f"if you don't want to write anything, just press enter\ntransaction explanation text: ")
            # number of days month
            remaining_days_months = jdatetime.j_days_in_month[jdatetime.date.today().month - 1]
            if (user_name.subscriptions != None):
                if (user_name.subscriptions[-2] == "active"): # tamdid eshtrack 
                    remaining_days_for_user = user_name.subscriptions[4] + remaining_days_months# (user_subscription+=remaining_days_months if user_name.subs != None else remaining_days)
                    pre_history = jdatetime.datetime.strptime(user_name.subscriptions[2], "%Y/%m/%d %H:%M:%S")
                    ented_time_sub = get_end_time(pre_history, number_months)
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), ented_time_sub.strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_for_user]
                    user_name.subscriptions = subscriptions
                    trx_resubscribe = (user_name, "Resubscribe", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                    translation_saved(trx_resubscribe)
                    break # back to panel
                else:
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_months]
                    user_name.subscriptions = subscriptions
                    trx_buy = (user_name, f"buy subscriptions {subc}", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                    translation_saved(trx_buy)
                    break # back to panel
            else:
                subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_months]
                user_name.subscriptions = subscriptions
                trx_buy = (user_name, f"buy subscriptions {subc}", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                translation_saved(trx_buy)
                break # back to panel
        else:
            print("aval kiphpol khode ra sharzh konid")
            fail_trx = (user_name, "buy subscription", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), "insufficient funds", user_name.generate_payment_id(price, user_name.information_card_user[0]), "failed")
            translation_saved(fail_trx)
            break # back to panel
    elif choice_plan == "B": # pay subscribtion 3 monts
        subc, price = ls_subscriptions[1]
        print(subc, price)
        number_months = int(subc.split()[0].strip())
        buy_time_subscription = jdatetime.datetime.now()
        if new_pay(price):
            tozih = input(f"if you don't want to write anything, just press enter\ntransaction explanation text: ")
            x = jdatetime.datetime.now().month - 1
            c = x_counter_days = 0
            while c != number_months:
                if x == 12:
                    x = 0
                x_counter_days += jdatetime.j_days_in_month[x]
                x+=1
                c+=1
            # number of days month
            # remaining_days_months = jdatetime.j_days_in_month[jdatetime.date.today().month - 1]
            if (user_name.subscriptions != None):
                if (user_name.subscriptions[-2] == "active"): # tamdid eshtrack 
                    remaining_days_for_user = user_name.subscriptions[4] + x_counter_days# (user_subscription+=remaining_days_months if user_name.subs != None else remaining_days)
                    pre_history = jdatetime.datetime.strptime(user_name.subscriptions[2], "%Y/%m/%d %H:%M:%S")
                    ented_time_sub = get_end_time(pre_history, number_months)
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), ented_time_sub.strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_for_user]
                    user_name.subscriptions = subscriptions
                    trx_resubscribe = (user_name, "Resubscribe", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                    translation_saved(trx_resubscribe)
                    break # back to panel
                else:
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', x_counter_days]
                    user_name.subscriptions = subscriptions
                    trx_buy = (user_name, f"buy subscriptions {subc}", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                    translation_saved(trx_buy)
                    break # back to panel
            else:
                subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', x_counter_days]
                user_name.subscriptions = subscriptions
                trx_buy = (user_name, f"buy subscriptions {subc}", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                translation_saved(trx_buy)
                break # back to panel
        else:
            print("aval kiphpol khode ra sharzh konid")
            fail_trx = (user_name, "buy subscription", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), "insufficient funds", user_name.generate_payment_id(price, user_name.information_card_user[0]), "failed")
            translation_saved(fail_trx)
            break # back to panel
    elif choice_plan == "C": # pay subscribtion 6 monts
        subc, price = ls_subscriptions[2]
        print(subc, price)
        number_months = int(subc.split()[0].strip())
        buy_time_subscription = jdatetime.datetime.now()
        if new_pay(price):
            tozih = input(f"if you don't want to write anything, just press enter\ntransaction explanation text: ")
            x = jdatetime.datetime.now().month - 1
            c = x_counter_days = 0
            while c != number_months:
                if x == 12:
                    x = 0
                x_counter_days += jdatetime.j_days_in_month[x]
                x+=1
                c+=1
            # number of days month
            # remaining_days_months = jdatetime.j_days_in_month[jdatetime.date.today().month - 1]
            if (user_name.subscriptions != None):
                if (user_name.subscriptions[-2] == "active"): # tamdid eshtrack 
                    remaining_days_for_user = user_name.subscriptions[4] + x_counter_days# (user_subscription+=remaining_days_months if user_name.subs != None else remaining_days)
                    pre_history = jdatetime.datetime.strptime(user_name.subscriptions[2], "%Y/%m/%d %H:%M:%S")
                    ented_time_sub = get_end_time(pre_history, number_months)
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), ented_time_sub.strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_for_user]
                    user_name.subscriptions = subscriptions
                    trx_resubscribe = (user_name, "Resubscribe", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                    translation_saved(trx_resubscribe)
                    break # back to panel
                else:
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', x_counter_days]
                    user_name.subscriptions = subscriptions
                    trx_buy = (user_name, f"buy subscriptions {subc}", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                    translation_saved(trx_buy)
                    break # back to panel
            else:
                subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', x_counter_days]
                user_name.subscriptions = subscriptions
                trx_buy = (user_name, f"buy subscriptions {subc}", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), tozih if tozih != "" else "None", user_name.generate_payment_id(price, user_name.information_card_user[0]), "success") # user_name.name   masaaaalan
                translation_saved(trx_buy)
                break # back to panel
        else:
            print("aval kiphpol khode ra sharzh konid")
            fail_trx = (user_name, "buy subscription", price, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), "insufficient funds", user_name.generate_payment_id(price, user_name.information_card_user[0]), "failed")
            translation_saved(fail_trx)
            break # back to panel
    else:
        print('input invalid!! ')
        choice_plan = input("What is your choice? ")



