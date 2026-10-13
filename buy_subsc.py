from test1 import *

ls_subscriptions = [("1 Months", 10000), ("3 Months", 25000), ("6 Months", 45000)] # (subscription, subscription fee)

ls_test_user_balance = [45000, 37000, 43000] # balance karbar baydad save beshe yaa vaghti barname basteh shode 0 mishan balance hamey karbaran?    mooooooohhhhhmmmmm



print("="*(5*10))

for i in ls_subscriptions:
    print(*i, sep=" ---> ")
print("For a new plan enter number 1\nTo renew your subscription, enter number 2\nTo go back, enter 'BACK'")
selection_path = input("your selection: ")

print("="*(5*10))



while True:# choice_plan != "BACK":
    print(f"\nplan A for 1 monts\nplan B for 3 monts\nplan C for 6 monts\nand for back enter 'BACK'.\njust enter only A or B or C.")
    choice_plan = input("What is your choice plan? ")
    if choice_plan == "A": # pay subscribtion 1 monts
        subc, price = ls_subscriptions[0]
        print(subc, price)
        number_months = int(subc.split()[0].strip())
        buy_time_subscription = jdatetime.datetime.now()
        if new_pay(price):
            # trx = (user_name, transaction_type, amount, time_now, description if description != "" else "None", payment_id, status)
            # number of days month
            remaining_days_months = jdatetime.j_days_in_month[jdatetime.date.today().month - 1]
            if (user_name.subscriptions != None):
                if (user_name.subscriptions[-2] == "active"): # tamdid eshtrack 
                    remaining_days_for_user = user_name.subscriptions[4] + remaining_days_months if user_name.subscriptions != None else remaining_days_months# (user_subscription+=remaining_days_months if user_name.subs != None else remaining_days)
                    pre_history = jdatetime.datetime.strptime(user_name.subscriptions[2], "%Y/%m/%d %H:%M:%S")
                    ented_time_sub = get_end_time(pre_history, number_months)
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), ented_time_sub.strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_for_user]
                    user_name.subscriptions = subscriptions
                else:
                    subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_months]
                    user_name.subscriptions = subscriptions
            else:
                subscriptions = [subc, buy_time_subscription.strftime("%Y/%m/%d %H:%M:%S"), get_end_time(buy_time_subscription, number_months).strftime("%Y/%m/%d %H:%M:%S"), 'active', remaining_days_months]
                user_name.subscriptions = subscriptions
        else:
            while True:
                print("mikhay kiphpol sharzh beshe? 1 else 'BACK'")
                x = input('1 or 0: ')
                if x == '1':
                    pass # sharzh kiphpol
                elif x == 'BACK':
                    break
                else:
                    x = input('1 or 0: ')
        break # back to panel
    elif choice_plan == "B": # pay subscribtion 3 monts
        subc, price = ls_subscriptions[1]
        print(subc, price)
        if ls_test_user_balance >= price: #  ls_test_user_balance hamoon user.balance hast
            # method pay_subsc ke khodam tarif mikonam be esm "pay_subsc"      --->   upgrade hamon test.py   ------>> # zamani kharid anjam shod user.balance -= int(price) beshe
            print("pay for plan B sucseess") # agar vagean success shode dar ghere insort failedd (masalan kip pol sharzh nadasht bayad yek failed sapt beshe)
            break
        else:
            print('mojodi kafi nisht aval bayad hestab khod ra sharzh konidd.')
            print("baraye sharz kardan kifpol khode be bakhsh sharzh kifpol moraze konid.")
            break
            # back to panel
    elif choice_plan == "C": # pay subscribtion 6 monts
        subc, price = ls_subscriptions[2]
        print(subc, price)
        if ls_test_user_balance >= price: #  ls_test_user_balance hamoon user.balance hast
            # method pay_subsc ke khodam tarif mikonam be esm "pay_subsc"      --->   upgrade hamon test.py   ------>> # user.balance -= int(price)
            print("pay for plan C sucseess") # agar vagean success shode dar ghere insort failedd (masalan kip pol sharzh nadasht bayad yek failed sapt beshe)
            break
        else:
            print('mojodi kafi nisht aval bayad hestab khod ra sharzh konidd.')
            print("baraye sharz kardan kifpol khode be bakhsh sharzh kifpol moraze konid.")
            break # back to panel
    elif choice_plan == "BACK":
        break
    else:
        print('input invalid!! ')
        choice_plan = input("What is your choice? ")



