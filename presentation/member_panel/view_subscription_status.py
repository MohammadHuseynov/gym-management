import jdatetime

def member_value(member, key):
    if isinstance(member, dict):
        return member.get(key)
    if key == "active":
        return member.is_active
    return getattr(member, key, None)

def view_subscription_status(member, subscriptions):
    while  True:
        username= member_value(member, "username")
        member_subscriptions = []
        for subscription in subscriptions:
            if subscription ["member_username"] == username:
                member_subscriptions.append(subscription)
        if not member_subscriptions:
           print("You don't have a subscription.")
        else:
            subscription = member_subscriptions[-1]
            print("Type:", subscription["type"])
            print("Amount:", subscription["amount"])
            print("Start Date:", subscription["start_date"])
            print("End Date:", subscription["end_date"])
            end_date=jdatetime.datetime.strptime(subscription["end_date"], "%Y/%m/%d").date()

            if end_date >= jdatetime.date.today():
                print("Status: Active")
            else:
                print("Status: Expired")
        
        print("\n0. Return")
        if input("Choose an option: ") == "0":
                    return
        print("Invalid choice.")   