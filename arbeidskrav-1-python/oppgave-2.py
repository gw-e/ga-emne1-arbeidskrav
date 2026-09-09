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
        pass
    elif choice == "2":
        show_all_sessions()
    elif choice == "3":
        show_completed_sessions()
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
    pass


def print_sessions(session):
    print(f"Topic: {session['topic']}")
    print(f"Duration: {session['duration_minutes']} min")
    print(f"Status: {session['status']}\n")


def show_all_sessions():
    clear_terminal()
    print("All Study Sessions:\n")

    for session in STUDY_SESSIONS:
        print_sessions(session)


def show_completed_sessions():
    clear_terminal()
    print("All Completed Study Sessions:\n")

    for sessoin in STUDY_SESSIONS:
        if sessoin['status'] == "completed":
            print_sessions(sessoin)







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