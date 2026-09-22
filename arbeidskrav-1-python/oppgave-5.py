import os
from data.activity import Activity


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

        date = input("Date: ")
        # validate_date()

        try:
            estimated_minutes = int(input("Estimated minutes: "))
            # if estimated_minutes >= 0:
        except ValueError:
            print("\nInvalid input: Must be a positive number. Please try again.\n")
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



if __name__ == "__main__":
    main()