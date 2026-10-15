import jdatetime

def view_subscription_status(member, subscription_repository):
    username = member.username
    member_subscriptions = []



    for subscription in subscription_repository:
        if subscription["member_username"] == username:
            member_subscriptions.append(subscription)

    if not member_subscriptions:
        print("You don't have a subscription.")

    else:
    
        subscription = member_subscriptions[-1] #this shows last item in subscription list

        print("Your Subscription Status")
        print("-" * 8)
        print(f"Type: {subscription["type"]}")
        print(f"Amount: {subscription["amount"]}")
        print(f"Start Date: {subscription["start_date"]}")
        print(f"End Date: {subscription["end_date"]}",)

        end_date = jdatetime.datetime.strptime(subscription["end_date"], "%Y/%m/%d").date()

        if end_date >= jdatetime.date.today():
            print("Status: Active")
        else:
            print("Status: Expired")

        return

    
