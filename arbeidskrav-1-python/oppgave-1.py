import os


# Oppgave 1.4 - Lag en meny

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def error_message(message):
    clear_terminal()
    print(message)
    input("\nPress enter to return: ")
    return main()


def main():
    clear_terminal()
    print("Welcome to Task 1 :)")
    print("\nWitch of these actions would you like to do:\n")
    print("[1] Calculate the time required")
    print("[2] Analyze text")
    print("[3] Analyze number intervals")
    print("[4] Exit")

    try:
        choice = int(input("\nPlease select an action by wrinting its number (1-4): "))
    except ValueError:
        error_message('Invalid input. Please enter the number of the action. (e.g. type "2" for "Analyze text" etc...)')

    if choice == 1:
        clear_terminal()
        show_total_study_time()
    elif choice == 2:
        clear_terminal()
        show_analyzed_text()
    elif choice == 3:
        clear_terminal()
        show_analyzed_number_range()
    elif choice == 4:
        clear_terminal()
        exit()
    else:
        error_message('Invalid input. Please enter the number of the action. (e.g. type "2" for "Analyze text" etc...)')

    input("\nPress enter to go back to menu: ")
    return main()



# Oppgave 1.1 - Beregn tidsbruk

def show_total_study_time():
    print("This is task 1.1 - Calculate the time required:\n")
    try:
        sessions = int(input("Number of study sessions: "))
        min_per_session = int(input("Minutes per session: "))
    except ValueError:
        print("Invalid input. Please enter positive whole numbers.")
        return show_total_study_time()

    if sessions < 0 or min_per_session < 0:
        print("Please enter positive whole numbers.")
        return show_total_study_time()

    hours, minutes = calc_time_spent(sessions, min_per_session)
    print(f"\nTotal time spent: {hours} hours and {minutes} minutes")


def calc_time_spent(sessions, min_per_session):
    total_min = min_per_session * sessions
    hours = total_min // 60
    rest = total_min % 60

    return hours, rest



# Oppgave 1.2 - Analyser tekst

def show_analyzed_text():
    print("This is task 1.2 - Analyze text:\n")
    text = input("Enter a text: ")

    if not text.strip():
        print("Invalid input. Please enter a text.")
        return show_analyzed_text() 

    count_characters(text)
    to_lowercase(text)
    reverse_text(text)
    contains_python(text)


def count_characters(text):
    with_spaces = len(text)
    without_spaces = len(text.replace(" ", ""))

    print(f"\nCharacters with spaces: {with_spaces}.")
    print(f"Characters without spaces: {without_spaces}.")


def to_lowercase(text):
    lc = text.lower()
    print(f"Text in lowercase: {lc}")


def reverse_text(text):
    reversed_text = text[::-1]
    print(f"Text in reverse: {reversed_text}")


def contains_python(text):
    if "python" in text.lower():
        print('Text contains the word "python".')
    else:
        print('Text do not contain the word "python".')



# Oppgave 1.3 - Analyser et tallintervall

def show_analyzed_number_range():
    print("This is task 1.3 - Analyze number intervals:\n")
    try:
        start_value = int(input("Enter a start value: "))
        end_value = int(input("Enter a end value: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers.")
        return show_analyzed_number_range()

    even_numbers(start_value, end_value)
    divisible_by_3(start_value, end_value)
    sum_range(start_value, end_value)


def even_numbers(start_value, end_value):
    print(f"\nAll even numbers from {start_value} to {end_value}:", end=" ")
    for i in range(start_value, end_value+1):
        if i % 2 == 0:
            print(i, end=" ")


def divisible_by_3(start_value, end_value):
    print(f"\nAll number from {start_value} to {end_value} that are divisible by 3:", end=" ")
    for i in range(start_value, end_value+1):
        if i % 3 == 0:
            print(i, end=" ")


def sum_range(start_value, end_value):
    total_sum = 0
    for i in range(start_value, end_value+1):
        total_sum += i

    print(f"\nSum of all numbers from {start_value} to {end_value}: {total_sum}")



if __name__ == "__main__":
    main()



    
    
