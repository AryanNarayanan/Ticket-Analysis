import os
import helpers
import file_handler
import analysis
import charts
from generate_tickets import make_tickets

if not os.path.exists(file_handler.FILE_PATH):
    make_tickets(file_handler.FILE_PATH)

records = file_handler.read_with_csv()
print("Total tickets loaded:", len(records))
print("First record        :", records[0])
print("Categories (set)    :", helpers.unique_values(records, "category"))
print("Status count (dict) :", helpers.count_by(records, "status"))
print("List methods demo   :", helpers.list_methods_demo())
helpers.dict_methods_demo()

df = file_handler.load_data()

while True:
    print("\n===== TICKET DATA ANALYSIS SYSTEM =====")
    print(" 1. Display all tickets")
    print(" 2. Add a new ticket")
    print(" 3. Search a ticket")
    print(" 4. Update a ticket")
    print(" 5. Delete a ticket")
    print(" 6. Summary report")
    print(" 7. NumPy demo")
    print(" 8. Pandas: select, filter, sort")
    print(" 9. Pandas: groupby and statistics")
    print("10. Insights")
    print("11. Handle missing values")
    print("12. Show graphs")
    print(" 0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        helpers.print_header("ALL TICKETS")
        helpers.show_table(df)

    elif choice == "2":
        helpers.print_header("ADD NEW TICKET")
        customer = input("Customer name: ")
        category = input("Category " + str(helpers.CATEGORIES) + ": ")
        priority = input("Priority " + str(helpers.PRIORITIES) + ": ")
        agent = input("Agent name: ")
        if category in helpers.CATEGORIES and priority in helpers.PRIORITIES:
            df, new_id = file_handler.add_ticket(df, customer, category, priority, agent)
            print("Ticket added. Ticket ID is", new_id)
        else:
            print("Invalid category or priority.")

    elif choice == "3":
        helpers.print_header("SEARCH TICKET")
        keyword = input("Enter ticket ID or customer name: ")
        result = file_handler.search_ticket(df, keyword)
        print(len(result), "ticket(s) found")
        helpers.show_table(result)

    elif choice == "4":
        helpers.print_header("UPDATE TICKET")
        tid = helpers.get_number("Enter ticket ID: ", 1, 999999)
        column = input("Column to update (status/priority/agent/resolution_hours/satisfaction): ")
        value = input("New value: ")
        if column in ["resolution_hours", "satisfaction"]:
            value = int(value)
        df, done = file_handler.update_ticket(df, tid, column, value)
        print("Ticket updated." if done else "Ticket ID not found.")

    elif choice == "5":
        helpers.print_header("DELETE TICKET")
        tid = helpers.get_number("Enter ticket ID to delete: ", 1, 999999)
        df, done = file_handler.delete_ticket(df, tid)
        print("Ticket deleted." if done else "Ticket ID not found.")

    elif choice == "6":
        analysis.summary_report(df)

    elif choice == "7":
        analysis.numpy_demo(df)

    elif choice == "8":
        analysis.pandas_basics(df)

    elif choice == "9":
        analysis.groupby_demo(df)
        analysis.statistics(df)

    elif choice == "10":
        analysis.insights(df)

    elif choice == "11":
        df = analysis.handle_missing_values(df)

    elif choice == "12":
        charts.all_charts(df)

    elif choice == "0":
        print("Thank you. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")

    input("\nPress Enter to continue...")
