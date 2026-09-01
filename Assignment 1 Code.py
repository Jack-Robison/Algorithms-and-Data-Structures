# Programing Assignment 1 Code
# Jack Robison

#postitions for txt information
ID = 0
NAME = 1
MPG = 2
CYLINDERS = 3
DISPLACEMENT = 4
HORSEPOWER = 5
WEIGHT = 6
ACCELERATION = 7
MODEL_YEAR = 8
COUNTRY = 9

# Create one record from a line in data.txt
def create_record(line):

    # txt is separated by whitespace
    data = line.split()

    record = [
        int(data[0]), data[1], float(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), float(data[7]), int(data[8]), data[9]              
    ]

    return record

#heading
def print_heading():

    print(
        f"{'ID':>3}  {'Vehicle':<28} {'MPG':>6} {'Cyl':>4} "
        f"{'Disp':>6} {'HP':>5} {'Weight':>7} {'Accel':>7} "
        f"{'Year':>5} {'Country':<10}"
    )


#formating one record
def format_record(record):

    return (
        f"{record[ID]:>3}  "
        f"{record[NAME]:<28} "
        f"{record[MPG]:>6.1f} "
        f"{record[CYLINDERS]:>4} "
        f"{record[DISPLACEMENT]:>6} "
        f"{record[HORSEPOWER]:>5} "
        f"{record[WEIGHT]:>7} "
        f"{record[ACCELERATION]:>7.1f} "
        f"{record[MODEL_YEAR]:>5} "
        f"{record[COUNTRY]:<10}"
    )

#Method 6.1
def delete_first_record(table):

    if len(table) == 0:
        print("\nThe table is empty. No record can be deleted.")
        return

    deleted_record = table.pop(0)

    print("\nThe first record was deleted successfully:")
    print_heading()
    print(format_record(deleted_record))

#Method 6.2
def sum_mpg(table):

    total = 0.0

    for record in table:
        total = total + record[MPG]

    return total

#Method 6.3
def find_largest_horsepower(table):

    if len(table) == 0:
        return -1

    largest_location = 0

    for location in range(1, len(table)):

        if table[location][HORSEPOWER] > table[largest_location][HORSEPOWER]:
            largest_location = location

    return largest_location

#Method 6.4
def sort_name_ascending(table):

    table.sort(key=lambda record: record[NAME])

    print("\nThe table has been sorted by vehicle name "
          "in ascending order.")

#Method 6.5
def sort_mpg_descending(table):

    table.sort(
        key=lambda record: record[MPG],
        reverse=True
    )

    print("\nThe table has been sorted by MPG "
          "in descending order.")

#Method 6.6
def print_report(table, outfile):

    outfile.seek(0)
    outfile.truncate()
    report_width = 94
    title = "AUTOMOBILE DATA REPORT"

    # Center the report title
    outfile.write(title.center(report_width) + "\n")

    outfile.write("=" * report_width + "\n")

    # Column headings
    outfile.write(
        f"{'ID':>3}  "
        f"{'Vehicle':<28} "
        f"{'MPG':>6} "
        f"{'Cyl':>4} "
        f"{'Disp':>6} "
        f"{'HP':>5} "
        f"{'Weight':>7} "
        f"{'Accel':>7} "
        f"{'Year':>5} "
        f"{'Origin':<10}\n"
    )

    outfile.write("-" * report_width + "\n")

    for record in table:
        outfile.write(format_record(record) + "\n")

    outfile.flush()

    print("\nThe table was written to report.txt successfully.")

#Method 6.7
def delete_Using_Key(table, key):

    location = find_Record_Using_Key(table, key)

    if location == -1:

        print(f"\nRecord with key {key} was not found.")

        return

    # Display the record before deleting it
    print("\nRecord found:")

    print_heading()

    print(format_record(table[location]))

    # Ask user to confirm deletion
    answer = input(
        "\nDelete this record permanently? (Y/N): "
    ).strip().upper()

    if answer == "Y":

        delete_Record_At_Address_Location(
            table,
            location
        )

        print(
            f"Record with key {key} "
            "was deleted successfully."
        )

    else:

        print("Delete operation canceled.")

#Method 6.7.1
def find_Record_Using_Key(table, key):

    for location in range(len(table)):

        if table[location][ID] == key:
            return location

    return -1

#Method 6.7.2
def delete_Record_At_Address_Location(table, location):

    del table[location]

#Method 6.9
def display_all_records(table):

    if len(table) == 0:

        print("\nThe table is empty.")

        return

    print()

    print_heading()

    for record in table:

        print(format_record(record))

    print(f"\nNumber of records: {len(table)}")

#Display menu
def display_menu():

    print("MENU")

    print("-" * 58)

    print("1. Delete the first record                 (Method 6.1)")
    print("2. Sum the MPG field                       (Method 6.2)")
    print("3. Find record with largest horsepower     (Method 6.3)")
    print("4. Sort vehicle names ascending            (Method 6.4)")
    print("5. Sort MPG descending                     (Method 6.5)")
    print("6. Write all records to report.txt         (Method 6.6)")
    print("7. Delete a record using its primary key   (Method 6.7)")
    print("9. Display all records                     (Method 6.9)")
    print("Q. Quit")

def main():

   infile = open("data.txt", "r")

   outfile = open("report.txt", "w")

   table = []

    for line in infile:

        if line.strip() != "":

            record = create_record(line)

            table.append(record)

    choice = ""

    while choice != "Q":

        display_menu()

        choice = input(
            "\nEnter your selection: "
        ).strip().upper()


        #Method 6.1
        if choice == "1" or choice == "6.1":

            delete_first_record(table)


        #Method 6.2
        elif choice == "2" or choice == "6.2":

            total = sum_mpg(table)

            print(
                f"\nTotal MPG of all records: "
                f"{total:,.1f}"
            )


        #Method 6.3
        elif choice == "3" or choice == "6.3":

            location = find_largest_horsepower(table)

            if location == -1:

                print("\nThe table is empty.")

            else:

                print(
                    "\nRecord with the largest horsepower:"
                )

                print_heading()

                print(
                    format_record(
                        table[location]
                    )
                )


        # Method 6.4
        elif choice == "4" or choice == "6.4":

            sort_name_ascending(table)


        # Method 6.5
        elif choice == "5" or choice == "6.5":

            sort_mpg_descending(table)


        # Method 6.6
        elif choice == "6" or choice == "6.6":

            print_report(
                table,
                outfile
            )


        # Method 6.7
        elif choice == "7" or choice == "6.7":

            try:

                key = int(
                    input(
                        "Enter the primary key "
                        "(ID) to delete: "
                    )
                )

                delete_Using_Key(
                    table,
                    key
                )

            except ValueError:

                print(
                    "\nInvalid key. "
                    "The primary key must be an integer."
                )


        # Method 6.9
        elif choice == "9" or choice == "6.9":

            display_all_records(table)


        # Quit
        elif choice == "Q":

            print("\nExiting program...")


        # Invalid menu option
        else:

            print(
                "\nInvalid menu choice. "
                "Please try again."
            )

    infile.close()

    outfile.close()

    print("Files closed. Program ended.")


main()




