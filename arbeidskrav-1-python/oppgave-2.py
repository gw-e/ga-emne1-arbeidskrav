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
    print("[1] View study sessions")
    print("[2] Register study session")
    print("[3] View total and average duration for completed sessions. ")
    print("[4] Exit the program")

    choice = input("\nPlease select an action by wrinting its number (1-7): ")

    if choice == "1":
        pass
    elif choice == "7":
        clear_terminal()
        exit()
    else:
        error_message("Invalid input. Please enter the number of the action.")
        return main()

    input("\nPress enter to go back to menu: ")
    return main()



if __name__ == "__main__":
    main()