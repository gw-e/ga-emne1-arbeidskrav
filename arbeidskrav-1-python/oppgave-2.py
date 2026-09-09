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

def main():
    pass


if __name__ == "__main__":
    main()