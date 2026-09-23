import os
from data.activity import Activity
from datetime import datetime
from pathlib import Path
import json

ACTIVITIES = []


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def error_message(message):
    clear_terminal()
    print(message)
    input("\nPress enter to return: ")


def main():
    while True:
        clear_terminal()
        print("Welcome to Activity Planner Pro!")
        print("\nWhat would you like to do?\n")
        print("[1]  Add activity")
        print("[2]  Show activities")
        print("[3]  Search activities")
        print("[4]  Filter activities")
        print("[5]  Sort activities")
        print("[6]  Complete activity")
        print("[7]  Show statistics")
        print("[8]  Save activities")
        print("[9]  Load activities")
        print("[10] Exit")

        choice = input("\nPlease select an option (1-10): ")
        
        if choice == "1":
            add_activity()

        elif choice == "2":
            show_activities()

        elif choice == "3":
            search_activities()

        elif choice == "4":
            filter_avtivities()

        elif choice == "5":
            sort_activities()

        elif choice == "6":
            complete_activity()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            save_activities()

        elif choice == "10":
            clear_terminal()
            exit()

        else:
            error_message("Invalid input. Please enter the number behind the option.")
            continue

        input("\nPress enter to go back to menu: ")
        continue

def add_activity():
    clear_terminal()
    print("Add an activity:\n")

    while True:
        
        title = input("Title: ")
        if not title.strip():
            print("\nInvalid input: Input cannot be empty. Please try again.\n")
            continue

        category = input("Category: ")
        if not category.strip():
            print("\nInvalid input: Input cannot be empty. Please try again.\n")
            continue

        date = input("Date: ")
        if not valid_date(date):
            print("\nInvalid date: Please use the format dd.mm.yyyy.\n")
            continue

        try:
            estimated_minutes = int(input("Estimated minutes: "))
            if estimated_minutes <= 0:
                print("\nInvalid input: Must be a positive number. Please try again.\n")
                continue
        except ValueError:
            print("\nInvalid input: Must be a number. Please try again.\n")
            continue
        

        activity = Activity(
            title,
            category,
            date,
            estimated_minutes,
            "planned"
        )

        ACTIVITIES.append(activity)
        print("\nActivity added successfully.")

        break


def valid_date(date):
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def show_activities():
    clear_terminal()
    print("All activities:\n")

    if len(ACTIVITIES) == 0:
        print("No activities found.")
        return

    for activity in ACTIVITIES:
        print_activity(activity)


def print_activity(activity):
    print(f"Title:              {activity.title}")
    print(f"Category:           {activity.category}")
    print(f"Date:               {activity.date}")
    print(f"Estimated minutes:  {activity.estimated_minutes}")
    print(f"Status:             {activity.status}\n")


def search_activities():
    clear_terminal()
    search = input("Search for an activity by title or category: ").lower()

    result = []

    for activity in ACTIVITIES:
        title = activity.title.lower()
        category = activity.category.lower()

        if search in title or search in category:
            result.append(activity)

    print(f'\nFound {len(result)} activity matching "{search}"\n')

    for r in result:
        print_activity(r)


def filter_avtivities():
    clear_terminal()
    print("Filter activities by status:\n")

    print("[1] Show planned")
    print("[2] Show completed")

    choice = input("\nHow would you like to filter? ")

    if choice == "1":
        status = "planned"
    elif choice == "2":
        status = "completed"
    else:
        print("\nInvalid choice.")
        return

    print(f"\n{status.capitalize()} activities:\n")

    found = False

    for activity in ACTIVITIES:
        if status in activity.status:
            print_activity(activity)
            found = True

    if not found:
        print("No activities found with this status.")
        return


def sort_activities():
    clear_terminal()
    print("Sort activity by:\n")

    print("[1] Date")
    print("[2] Duration")

    choice = input("\nWhat would you like to sort by? ")

    if choice == "1":
        sorted_activities = sorted(ACTIVITIES, key=lambda activity: datetime.strptime(activity.date, "%d.%m.%Y"))
        sorted_by = "date"
    elif choice == "2":
        sorted_activities = sorted(ACTIVITIES, key=lambda activity: activity.estimated_minutes, reverse=True)
        sorted_by = "duration"
    else:
        print("\nInvalid choice.")
        return

    print(f"\nActivities sorted by {sorted_by}:\n")

    for a in sorted_activities:
        print_activity(a)


def complete_activity():
    clear_terminal()
    print("Complete an activity:\n")

    planned_activities = []

    for activity in ACTIVITIES:
        if activity.status == "planned":
            planned_activities.append(activity)

    if not planned_activities:
        print("There are no planned activities to complete.")
        return

    for i, activity in enumerate(planned_activities, start=1):
        print(f"[{i}] Title:              {activity.title}")
        print(f"    Category:           {activity.category}")
        print(f"    Date:               {activity.date}")
        print(f"    Estimated minutes:  {activity.estimated_minutes}")
        print(f"    Status:             {activity.status}\n")

    while True:
        try:
            choice = int(input("What activity do you want to complete? "))

            if choice < 1 or choice > len(planned_activities):
                print("\nInvalid activity number. Try again.\n")
                continue

            activity = planned_activities[choice - 1]

            activity.complete()

            print(f"\n'{activity.title}' has been marked as completed.")
            break

        except ValueError:
            print("\nPlease enter a number.\n")
    

def show_statistics():
    clear_terminal()
    print("Activities Statistics\n")
    total = len(ACTIVITIES)
    total_time = 0
    total_completed = 0

    for activity in ACTIVITIES:
        total_time += activity.estimated_minutes
        if activity.status == "completed":
            total_completed += 1

    print(f"Total activities: {total}")
    print(f"Total estimated time: {total_time}")
    print(f"Total completed: {total_completed}")


def save_activities():
    clear_terminal()
    print("Saving activities...\n")

    data = []

    for activity in ACTIVITIES:
        activity_dict = vars(activity)
        data.append(activity_dict)

    path = Path(__file__).parent / "data" / "activities.json"

    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Activities successfully saved.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Could not write to file.")

    



if __name__ == "__main__":
    main()