import copy
import json
import os
import re

DATA_FILE = "data.json"  # MATCH WITH TEAM

INITIAL_DATA = {
    "users": [
        {"name": "مدیر باشگاه", "username": "admin", "password": "Admin@123",
         "email": "admin@gym.com", "role": "manager", "active": True},
        {"name": "هوشنگ رضایی", "username": "coach1", "password": "Coach@123",
         "email": "Hooooshi@gym.com", "role": "coach", "active": True},
        {"name": "کلثوم محمدی", "username": "coach2", "password": "Coach@456",
         "email": "kolii@gym.com", "role": "coach", "active": True},
        {"name": "رضا کریمی", "username": "coach3", "password": "Coach@789",
         "email": "reza@gym.com", "role": "coach", "active": False},
        {"name": "عباس بوعذار", "username": "member1", "password": "Member@123",
         "email": "abbas@gmail.com", "role": "member", "active": False},
        {"name": "کشور حسینی", "username": "member2", "password": "Member@456",
         "email": "iran@gmail.com", "role": "member", "active": True},
        {"name": "پویا کبیری", "username": "member3", "password": "Member@789",
         "email": "pouya@gmail.com", "role": "member", "active": True},
    ],
    "classes": [
        {"id": 1, "title": "یوگای صبحگاهی", "sport": "یوگا", "coach": "coach1",
         "hall": "سالن ۱", "day": "شنبه", "time": "08:00", "capacity": 15, "active": True},
        {"id": 2, "title": "بدنسازی مقدماتی", "sport": "بدنسازی", "coach": "coach1",
         "hall": "سالن ۲", "day": "دوشنبه", "time": "18:00", "capacity": 20, "active": True},
        {"id": 3, "title": "کراس‌فیت", "sport": "کراس‌فیت", "coach": "coach2",
         "hall": "سالن ۲", "day": "سه‌شنبه", "time": "19:00", "capacity": 12, "active": True},
    ],
    "enrollments": [
        {"member": "member1", "class_id": 1, "status": "active"},
        {"member": "member2", "class_id": 1, "status": "active"},
        {"member": "member1", "class_id": 2, "status": "active"},
        {"member": "member3", "class_id": 3, "status": "active"},
    ],
    "plans": [],
}


# ---------------------------------------------------------------- ورودی کاربر
class Ask:
    @staticmethod
    def choice(prompt, valid_choices):
        while True:
            answer = input(prompt).strip()
            if answer in valid_choices:
                return answer
            print("گزینه نامعتبر است.دوباره تلاش کنید!")

    @staticmethod
    def text(label, old=None):
        while True:
            hint = f" [{old}]" if old is not None else ""
            answer = input(f"{label}{hint}: ").strip()
            if answer == "" and old is not None:
                return old
            if answer:
                return answer
            print("این بخش نباید خالی باشد.")

    @staticmethod
    def number(label, allow_zero=False, old=None):
        pattern = r"\d+" if allow_zero else r"[1-9]\d*"
        while True:
            hint = f" [{old}]" if old is not None else ""
            answer = input(f"{label}{hint}: ").strip()
            if answer == "" and old is not None:
                return old
            if re.fullmatch(pattern, answer):
                return int(answer)
            if allow_zero:
                print("لطفاً یک عدد صحیح (صفر یا بیشتر) وارد کنید.")
            else:
                print("لطفاً یک عدد صحیح بزرگ‌تر از صفر وارد کنید.")


# ---------------------------------------------------------------- ذخیره‌سازی
class Storage:

    def __init__(self, path):
        self.path = path

    def save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        if not os.path.exists(self.path):
            return self._reset()
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("فایل دیتا خراب است. اطلاعات اولیه دوباره ساخته شدند.")
            return self._reset()

    def _reset(self):
        data = copy.deepcopy(INITIAL_DATA)
        self.save(data)
        return data


# ---------------------------------------------------------------- باشگاه
class Gym:

    def __init__(self, storage):
        self.storage = storage
        self.data = storage.load()

    def save(self):
        self.storage.save(self.data)

    def find_user(self, username):
        for user in self.data["users"]:
            if user["username"] == username:
                return user
        return None

    def coach_classes(self, username):
        return [c for c in self.data["classes"] if c["coach"] == username]

    def class_members(self, class_id):
        
        return [e["member"] for e in self.data["enrollments"]
                if e["class_id"] == class_id and e["status"] == "active"]

    def get_plan(self, class_id, member):
        
        for plan in self.data["plans"]:
            if plan["class_id"] == class_id and plan["member"] == member:
                return Plan(plan)
        new_plan = {"class_id": class_id, "member": member, "moves": []}
        self.data["plans"].append(new_plan)
        return Plan(new_plan)


# ---------------------------------------------------------------- حرکت و برنامه
class Move:
    def __init__(self, name, sets, reps, rest, description):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.rest = rest
        self.description = description

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["sets"], d["reps"], d["rest"], d["description"])

    def to_dict(self):
        return {"name": self.name, "sets": self.sets, "reps": self.reps,
                "rest": self.rest, "description": self.description}

    @classmethod
    def read_from_user(cls, old=None):
        """حرکت جدید می‌گیرد؛ اگر old داده شود، Enter یعنی نگه‌داشتن مقدار قبلی."""
        name = Ask.text("نام حرکت", old.name if old else None)
        sets = Ask.number("تعداد ست", old=old.sets if old else None)
        reps = Ask.number("تعداد تکرار", old=old.reps if old else None)
        rest = Ask.number("زمان استراحت (S)", allow_zero=True,
                          old=old.rest if old else None)

        description = input("توضیح (اختیاری): ").strip()
        if description == "" and old:
            description = old.description

        return cls(name, sets, reps, rest, description)

    def __str__(self):
        return (f"{self.name} | {self.sets} ست × {self.reps} تکرار | "
                f"استراحت: {self.rest} ثانیه | توضیح: {self.description or '-'}")


class Plan:
    """برنامه‌ی تمرینی یک عضو در یک کلاس."""

    def __init__(self, plan_dict):
        self.plan = plan_dict

    @property
    def moves(self):
        return [Move.from_dict(m) for m in self.plan["moves"]]

    def show(self):
        moves = self.moves
        if not moves:
            print("این برنامه هنوز حرکتی ندارد.")
            return
        for i, move in enumerate(moves, start=1):
            print(f"{i}. {move}")

    def add_move(self, move):
        self.plan["moves"].append(move.to_dict())

    def edit_move(self, index, move):
        self.plan["moves"][index] = move.to_dict()


# ---------------------------------------------------------------- پنل مربی
class CoachPanel:
    def __init__(self, gym, coach):
        self.gym = gym
        self.coach = coach

    def show_my_classes(self):
        classes = self.gym.coach_classes(self.coach["username"])
        if not classes:
            print("هنوز کلاسی به شما اختصاص داده نشده است.")
            return

        for c in classes:
            usernames = self.gym.class_members(c["id"])
            names = [self.gym.find_user(u)["name"] for u in usernames]
            print("-" * 40)
            print(f"عنوان: {c['title']}")
            print(f"نوع ورزش: {c['sport']}")
            print(f"روز و ساعت: {c['day']} - {c['time']}")
            print(f"سالن: {c['hall']}")
            print(f"ظرفیت: {c['capacity']}")
            print("اعضای ثبت‌نام‌شده: " + ("، ".join(names) if names else "ندارد"))
        print("-" * 40)

    def choose_class(self):
        classes = self.gym.coach_classes(self.coach["username"])
        if not classes:
            print("هنوز کلاسی به شما اختصاص داده نشده است.")
            return None

        for i, c in enumerate(classes, start=1):
            print(f"{i}. {c['title']} ({c['day']} {c['time']})")
        print("0. بازگشت")

        valid = [str(i) for i in range(len(classes) + 1)]
        choice = Ask.choice("شماره کلاس: ", valid)
        if choice == "0":
            return None
        return classes[int(choice) - 1]

    def choose_member(self, class_info):
        members = self.gym.class_members(class_info["id"])
        if not members:
            print("در این کلاس هنوز عضوی ثبت‌نام نکرده است.")
            return None

        for i, username in enumerate(members, start=1):
            print(f"{i}. {self.gym.find_user(username)['name']}")
        print("0. بازگشت")

        valid = [str(i) for i in range(len(members) + 1)]
        choice = Ask.choice("شماره عضو: ", valid)
        if choice == "0":
            return None
        return members[int(choice) - 1]

    def manage_plan(self):
        class_info = self.choose_class()
        if class_info is None:
            return

        member = self.choose_member(class_info)
        if member is None:
            return

        plan = self.gym.get_plan(class_info["id"], member)
        member_name = self.gym.find_user(member)["name"]

        while True:
            print(f"\nبرنامه تمرینی {member_name} - {class_info['title']}")
            plan.show()
            print("1. افزودن حرکت")
            print("2. ویرایش حرکت")
            print("3. بازگشت")
            choice = Ask.choice("انتخاب شما: ", ["1", "2", "3"])

            if choice == "1":
                plan.add_move(Move.read_from_user())
                self.gym.save()
                print("حرکت اضافه شد.")
            elif choice == "2":
                moves = plan.moves
                if not moves:
                    print("حرکتی برای ویرایش وجود ندارد.")
                    continue
                valid = [str(i) for i in range(1, len(moves) + 1)]
                index = int(Ask.choice("شماره حرکت: ", valid)) - 1
                plan.edit_move(index, Move.read_from_user(moves[index]))
                self.gym.save()
                print("حرکت ویرایش شد.")
            else:
                return

    def run(self):
        while True:
            print("\n=== پنل مربی ===")
            print("1. مشاهده کلاس‌های خود")
            print("2. مدیریت برنامه تمرینی اعضا")
            print("3. خروج")
            choice = Ask.choice("انتخاب شما: ", ["1", "2", "3"])

            if choice == "1":
                self.show_my_classes()
            elif choice == "2":
                self.manage_plan()
            else:
                self.gym.save()
                print("خارج شدید.")
                return


# ---------------------------------------------------------------- برنامه اصلی
class App:
    def __init__(self):
        self.gym = Gym(Storage(DATA_FILE))

    def coach_login(self):
        while True:
            username = input("نام کاربری: ").strip()
            password = input("رمز عبور: ").strip()

            user = self.gym.find_user(username)
            if user is None or user["role"] != "coach" or user["password"] != password:
                print("نام کاربری یا رمز عبور اشتباه است.")
            elif not user["active"]:
                print("حساب شما غیرفعال است. با مدیر تماس بگیرید.")
            else:
                print(f"خوش آمدید {user['name']}!")
                return user

            print("1. تلاش مجدد")
            print("2. بازگشت")
            if Ask.choice("انتخاب شما: ", ["1", "2"]) == "2":
                return None

    def run(self):
        while True:
            print("\n=== سامانه مدیریت باشگاه ===")
            print("1. ورود مربی")
            print("2. خروج")
            choice = Ask.choice("انتخاب شما: ", ["1", "2"])

            if choice == "1":
                coach = self.coach_login()
                if coach is not None:
                    CoachPanel(self.gym, coach).run()
            else:
                self.gym.save()
                print("بای بای!")
                break


if __name__ == "__main__":
    App().run()
