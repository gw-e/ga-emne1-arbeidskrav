import os


STUDY_SESSIONS = [
    {
        "topic": "Python basics",
        "duration_minutes": 45,
        "status": "completed"
    },
    {
        "topic": "Variables and data types",
        "duration_minutes": 30,
        "status": "completed"
    },
    {
        "topic": "Lists and dictionaries",
        "duration_minutes": 60,
        "status": "planned"
    },
    {
        "topic": "Functions",
        "duration_minutes": 40,
        "status": "planned"
    },
    {
        "topic": "Object-oriented programming",
        "duration_minutes": 50,
        "status": "planned"
    }
]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def error_message(message):
    clear_terminal()
    print(message)
    input("\nPress enter to return: ")


def main():
    clear_terminal()
    print("Welcome to Task 2 :)")
    print("\nWitch of these actions would you like to do:\n")
    print("[1] Register a Study Session")
    print("[2] Show All Study Sessions")
    print("[3] Show Completed Study Sessions")
    print("[4] Search Study Sessions")
    print("[5] Sort by Duration")
    print("[6] Show Study Time Statistics ")
    print("[7] Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        register_session()
    elif choice == "2":
        show_all_sessions()
    elif choice == "3":
        show_completed_sessions()
    elif choice == "4":
        search_sessions()
    elif choice == "5":
        sort_by_duration()
    elif choice == "6":
        show_study_time_stats()
    elif choice == "7":
        clear_terminal()
        exit()
    else:
        error_message("Invalid input. Please enter the number of the action.")
        return main()

    input("\nPress enter to go back to menu: ")
    return main()


def register_session():
    clear_terminal()
    print("Register a Study Session:\n")

    while True:
        topic = input("Enter a topic: ")
        if not topic.strip():
            print("Invalid input! Try again.\n")
            continue
        break

    while True:
        try:
            duration = int(input("Session length (minutes): "))
        except ValueError:
            print("Invalid input! Try again.\n")
            continue

        if duration <= 0:
            print("Duration must be a positive number! Try again.\n")
            continue

        break

    new_session = {
        "topic": topic,
        "duration_minutes": duration,
        "status": "planned",
    }

    try:   
        STUDY_SESSIONS.append(new_session)
        print("\nStudy session successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}")


def print_sessions(session):
    print(f"Topic: {session['topic']}")
    print(f"Duration: {session['duration_minutes']} min")
    print(f"Status: {session['status']}\n")


def show_all_sessions():
    clear_terminal()

    result = []

    for session in STUDY_SESSIONS:
        result.append(session)
    
    if len(result) == 0:
        return print("Cannot find any study sessions.")
    
    print("All Study Sessions:\n")

    for r in result:
        print_sessions(r)


def show_completed_sessions():
    clear_terminal()

    result = []

    for sessoin in STUDY_SESSIONS:
        if sessoin['status'] == "completed":
            result.append(sessoin)

    if len(result) == 0:
        return print("Cannot find any completed study sessions.")

    print("All Completed Study Sessions:\n")

    for r in result:
        print_sessions(r)


def search_sessions():
    clear_terminal()
    search = input("Search for a study session: ").lower()

    result = []

    for session in STUDY_SESSIONS:
        topic = session['topic'].lower()
        if search in topic:
            result.append(session)

    print(f'\nFound {len(result)} sessions matching "{search}"\n')

    for r in result:
        print_sessions(r)


def sort_by_duration():
    clear_terminal()
    print("All Sessions Sorted By Durration (longest-shortest):\n")

    sorted_sessions = sorted(STUDY_SESSIONS, key=lambda session: session['duration_minutes'], reverse=True)

    for session in sorted_sessions:
        print_sessions(session)


def show_study_time_stats():
    clear_terminal()
    print("Study Time Statistics:\n")

    durations = []

    for session in STUDY_SESSIONS:
        durations.append(session['duration_minutes'])

    total = sum(durations)
    hours, min = divmod(total, 60)

    avg = total / len(durations)
    avg_hours, avg_min = divmod(avg, 60)

    if hours > 0:
        total_txt = f"{hours} hours and {min} minutes"
    else:
        total_txt = f"{min} minutes"

    if avg_hours > 0:
        avg_txt = f"{avg_hours:.0f} hours and {avg_min:.0f} min"
    else:
        avg_txt = f"{avg_min:.0f} min"

    print(f"Total Study Time: {total_txt}")
    print(f"Typical Session: {avg_txt}")


if __name__ == "__main__":
    main()