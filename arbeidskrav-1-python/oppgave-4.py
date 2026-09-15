from pathlib import Path
import csv

def main():
    data = get_file_data()
    valid_data = []

    for row in data:
        if "" in row.values():
            print("Error! Value cannot be empty:", row)
            continue

        try:
            row["id"] = int(row["id"])
            if row["id"] <= 0:
                print("Error! Id must be a positive number:", row)
                continue
        except ValueError:
            print("Error! Id must be a number:", row)
            continue

        try: 
            row["minutes"] = int(row["minutes"])
            if row["minutes"] < 0:
                print("Error! Minutes must be a positive number:", row)
                continue
        except ValueError:
            print("Error! Minutes must be a number:", row)
            continue

        # is_resolved is yes or no

        valid_data.append(row)


def get_file_data():
    file_path = Path(__file__).parent / "data" / "supporthenvendelser.csv"
    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

    

if __name__ == "__main__":
    main()