from datetime import datetime, timedelta

def main():
    print(get_user_date())
    print(get_end_time())
    print(get_days_between_dates())


def get_user_date():
    while True:
        usr_date = input("Enter a date (dd.mm.yyyy): ")

        try:
            date_obj = datetime.strptime(usr_date, "%d.%m.%Y")
        except ValueError:
            print("Invalid format or date does not exist!\n")
            continue
        break

    return date_obj


def get_end_time():
    while True:
        start_time = input("Enter a start time (hh:mm): ")
        try:
            start_dt = datetime.strptime(start_time, "%H:%M")
        except ValueError:
            print("Invalid format or time does not exist!\n")
            continue

        try:
            min_to_add = int(input("Enter minutes to add: "))
            if min_to_add <= 0:
                print("Cannot be negative or zero!\n")
                continue
        except ValueError:
            print("Invalid input! Try again.\n")
            continue
        break

    end_dt = start_dt + timedelta(minutes=min_to_add)
    end_time = end_dt.strftime("%H:%M")

    return end_time


def get_days_between_dates():
    while True:
        input_1 = input("Enter the first date (dd.mm.yyyy): ")
        try:
            date_1 = datetime.strptime(input_1, "%d.%m.%Y")
        except ValueError:
            print("Invalid format or the dates does not exist!\n")
            continue

        input_2 = input("Enter the second date (dd.mm.yyyy): ")
        try:
            date_2 = datetime.strptime(input_2, "%d.%m.%Y")
        except ValueError:
            print("Invalid format or the dates does not exist!\n")
            continue
        break

    days_between = abs((date_1 - date_2).days)
    return days_between
            















if __name__ == "__main__":
    main()