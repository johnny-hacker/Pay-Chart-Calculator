# Import necessary modules
from EmployeeData import EmployeeData
from PayCaluclator import PayCalculator
from Display import Display


# Function to populate employee data
def populate_data():
    # Create an instance of EmployeeData to collect employee data
    employee_data = EmployeeData()
    employee_id = employee_data.empId
    pay_rate = employee_data.payRate
    hours_worked = employee_data.hours

    # Print the collected pay rates and hours worked
    print(pay_rate, hours_worked)

    # Calculate wages and display
    calculate(employee_id, hours_worked, pay_rate)


# Function to calculate wages
def calculate(id, hours_worked, pay_rate):
    # Create an instance of PayCalculator to perform wage calculations
    calculate_pay = PayCalculator()

    # Calculate wages for week, month, and year
    per_week = calculate_pay.pay_calculator_week(hours_worked, pay_rate)
    per_month = calculate_pay.pay_calculator_month(hours_worked, pay_rate)
    per_year = calculate_pay.pay_calculator_year(hours_worked, pay_rate)

    # Display the calculated wages
    display(id, per_week, per_month, per_year)


# Function to display wages
def display(employee_id, per_week, per_month, per_year):
    # Create an instance of Display to show employee wages
    display_pay = Display()

    # Display wages for the week, month, and year
    display_pay.display_week(employee_id, per_week)
    display_pay.display_month(employee_id, per_month)
    display_pay.display_year(employee_id, per_year)


# Main function to start the program
def main():
    # Dislay purpose of program to the user
    print("This program calculates employee pay roll")

    # Give user a chance to quit the program
    answer = input("Do you wish to continue [Y/N]? ")

    while (answer.lower() == "y" or answer.lower() == "YES"):
        # call the populate data function to retrieve employee data and display it
        populate_data()
        # Give user a chance to quit the program
        answer = input("\nDo you wish to continue [Y/N]? ")
    print("Thank you and goodbye")


# Call the main function to start the program
if __name__ == "__main__":
    main()

