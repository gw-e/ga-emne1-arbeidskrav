from pathlib import Path
from collections import Counter
import csv

def main():
    data = get_file_data()
    row_num = 1

    valid_total = 0
    categories_list = []
    minutes_list = []
    resolved_list = []
    unresolved_rows = []
    

    for row in data:
        row_num += 1
        is_valid = validate_data(row, row_num)

        if not is_valid:
            continue

        valid_total += 1
        categories_list.append(row["category"])
        minutes_list.append(row["minutes"])
        resolved_list.append(row["is_resolved"])

        if row["is_resolved"] == "no":
            unresolved_rows.append(row)

    valid_categories = dict(Counter(categories_list))

    avg_minutes = round(sum(minutes_list) / len(minutes_list), 1)

    amount_resolved = Counter(resolved_list)
    resolved = amount_resolved["yes"]
    unresolved = amount_resolved["no"]

    most_common_category = max(valid_categories, key=valid_categories.get)

    unresolved_sorted = sorted(unresolved_rows, key=lambda x: x["minutes"], reverse=True)

    report_data = {
        "total_inquiries": valid_total,
        "inquiries_per_category": valid_categories,
        "average_time": avg_minutes,
        "total_resolved": resolved,
        "total_unresolved": unresolved,
        "most_common_category": most_common_category,
        "all_unresolved_by_min": unresolved_sorted,
    }

    print()

    for key, value in report_data.items():
        print(f"{key}: {value}")


    




def get_file_data():
    file_path = Path(__file__).parent / "data" / "supporthenvendelser.csv"
    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def validate_data(row, row_num):
    if "" in row.values():
        print(f"Error! row {row_num}: Value cannot be empty.")
        return False

    try:
        row["id"] = int(row["id"])
        if row["id"] <= 0:
            print(f"Error! row {row_num}: Id must be a positive number.")
            return False
    except ValueError:
        print(f"Error! row {row_num}: Id must be a number.")
        return False

    try: 
        row["minutes"] = int(row["minutes"])
        if row["minutes"] < 0:
            print(f"Error! row {row_num}: Minutes must be a positive number.")
            return False
    except ValueError:
        print(f"Error! row {row_num}: Minutes must be a number.")
        return False

    if row["is_resolved"] not in ("yes", "no"):
        print(f'Error! row {row_num}: Resolved must be "yes" or "no".')
        return False

    return True


if __name__ == "__main__":
    main()
