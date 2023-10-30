from tabulate import tabulate


class Display:

    def __init__(self):
        # Initialize an empty table to display employee data
        self.table = []

    def display_week(self, id, pay):
        # Display employee data for the week
        for each_employee in range(len(id)):
            employee_record = [id[each_employee], pay[each_employee]]
            self.table.append(employee_record)

        # Print the table using tabulate with appropriate headers
        print(tabulate(self.table, headers=['\nEmployee ID', '\nWeekly Pay']))

        # Reset the table for the next use
        self.table = []

    def display_month(self, id, pay):
        # Display employee data for the month
        for each_employee in range(len(id)):
            employee_record = [id[each_employee], pay[each_employee]]
            self.table.append(employee_record)

        # Print the table using tabulate with appropriate headers
        print(tabulate(self.table, headers=['\nEmployee ID', '\nMonthly Pay']))

        # Reset the table for the next use
        self.table = []

    def display_year(self, id, pay):
        # Display employee data for the year
        for each_employee in range(len(id)):
            employee_record = [id[each_employee], pay[each_employee]]
            self.table.append(employee_record)

        # Print the table using tabulate with appropriate headers
        print(tabulate(self.table, headers=['\nEmployee ID', '\nYearly Pay']))

        # Reset the table for the next use
        self.table = []
