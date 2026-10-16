class SubscriptionRepository:
    def __init__(self, file_path="data/subscriptions_data.txt"):
        self.file_path = file_path

    #region ADD
    def add(self, subscription):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{subscription.member}|{subscription.subscription_type}|{subscription.price}|{subscription.start_date}|{subscription.end_date}|{subscription.status}\n"
            )
    #endregion

    #region GET_ALL
    def get_all(self):
        subscriptions = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                fields = line.rstrip("\n").split("|")
                if len(fields) < 6:
                    continue

                subscriptions.append({
                    "member": fields[0],
                    "subscription_type": fields[1],
                    "price": fields[2],
                    "start_date": fields[3],
                    "end_date": fields[4],
                    "status": fields[5],
                })

        return subscriptions
    #endregion
