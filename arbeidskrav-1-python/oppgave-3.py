from datetime import datetime, timedelta

def main():
    show_user_date()
    show_end_time()
    show_days_between_dates()
    show_sorted_dates()


def show_user_date():
    while True:
        usr_date = input("Enter a date (dd.mm.yyyy): ")

        try:
            date_obj = get_date_obj(usr_date)
        except ValueError:
            print("Invalid format or date does not exist!\n")
            continue
        break

    print(f'Date "{usr_date}" is valid: {date_obj}\n')

def get_date_obj(date):
    return datetime.strptime(date, "%d.%m.%Y")


def show_end_time():
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

    end_time = get_end_time(start_dt, min_to_add)
    print(f"{min_to_add} minutes from {start_time} is {end_time}\n")

def get_end_time(start_dt, min_to_add):
    end_dt = start_dt + timedelta(minutes=min_to_add)
    return end_dt.strftime("%H:%M")


def show_days_between_dates():
    while True:
        input_1 = input("Enter the first date (dd.mm.yyyy): ")
        try:
            date_1 = get_date_obj(input_1)
        except ValueError:
            print("Invalid format or the dates does not exist!\n")
            continue

        input_2 = input("Enter the second date (dd.mm.yyyy): ")
        try:
            date_2 = get_date_obj(input_2)
        except ValueError:
            print("Invalid format or the dates does not exist!\n")
            continue
        break

    days_between = get_days_between_dates(date_1, date_2)
    print(f"There are {days_between} days between {input_1} and {input_2}\n")

def get_days_between_dates(date_1, date_2):
    return abs((date_1 - date_2).days)


def show_sorted_dates():
    dates = [
        datetime(2026, 9, 14),
        datetime(2023, 5, 12),
        datetime(2025, 12, 25),
    ]

    sorted_dates = get_sorted_dates(dates)

    print("These are dates sorted chronologically:")

    for date in sorted_dates:
        print(" - ", date.strftime("%d.%m.%Y"))

def get_sorted_dates(dates):
    return sorted(dates)


if __name__ == "__main__":
    main()