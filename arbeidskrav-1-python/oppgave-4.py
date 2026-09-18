from pathlib import Path
from collections import Counter
import csv


def get_file_data():
    file_path = Path(__file__).parent / "data" / "supporthenvendelser.csv"
    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    data = get_file_data()
    row_num = 1

    valid_total = 0
    categories_list = []
    minutes_list = []
    resolved_list = []
    unresolved_rows = []
    rows = []
    

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

        rows.append(row)

    valid_categories = dict(Counter(categories_list))

    total_minutes = sum(minutes_list)
    avg_minutes = round(total_minutes / len(minutes_list), 1)

    amount_resolved = Counter(resolved_list)
    resolved = amount_resolved["yes"]
    unresolved = amount_resolved["no"]

    most_common_category = max(valid_categories, key=valid_categories.get)

    unresolved_sorted = sorted(unresolved_rows, key=lambda x: x["minutes"], reverse=True)

    report_lines = [ 
        "SUPPORT-RAPPORT", 
        "================", 
        "", 
        "GYLDIGE HENDVENDELSER:",
        "----------------------", 
        f"Totalt antall gyldige henvendelser: {valid_total}", 
        "", 
        "Antall henvendelser per kategori:",
    ]

    for category, amount in valid_categories.items():
        report_lines.append(f"- {category}: {amount}")

    report_lines.extend([ 
        "",
        "TIDSBRUK:",
        "---------",
        f"Samlet tidsbruk: {total_minutes} minutter",
        f"Gjennomsnittlig tidsbruk: {avg_minutes} minutter",
        "",
        "LØSTE OG ULØSTE HENVENDELSER:",
        "------------------------------",
        f"Løste: {resolved}",
        f"Uløste: {unresolved}",
        "",
        "KATEGORIEN MED FLEST HENVENDELSER:",
        "-----------------------------------",
        f"{most_common_category}: {valid_categories[most_common_category]} henvendelser",
        "",
        "ULØSTE HENVENDELSER:",
        "--------------------",
        "Sortert etter tidsbruk, mest tidkrevende først:",
    ])

    for row in unresolved_sorted: 
        report_lines.append(f"- {row['category']}: {row['minutes']} minutter")

    write_support_report(report_lines)

    # Oppgave 4.4:
    total_resolved_minutes = sum_resolved_minutes(rows)
    print(total_resolved_minutes) 

# Oppgave 4.4:
def sum_resolved_minutes(inquiries: list[dict[str, str | int]]) -> int:
    total_minutes = 0
    for inquiry in inquiries:
        if inquiry["is_resolved"] == "yes":
            try:
                minutes = int(inquiry["minutes"])
                total_minutes += minutes
            except (ValueError, TypeError):
                continue
    return total_minutes


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


def write_support_report(report):
    file_path = Path(__file__).parent / "data" / "support-report.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        for line in report:
            file.write(f"{line}\n")




if __name__ == "__main__":
    main()
