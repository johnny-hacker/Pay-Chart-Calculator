class EmployeeData:

    def __init__(self):
        self.empId = [56588, 45201, 78951, 87775, 84512, 13028, 75804]
        self.hours = [0, 1, 2, 3, 4, 5, 6]
        self.payRate = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        self.wages = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        self.get_data()

    def get_data(self):
        # Iterate through employee data for input
        for empNum in range(len(self.empId)):
            # Display the employee number
            print(f"\nEmployee ID#{self.empId[empNum]}")

            # Retrieve hours worked
            self.hours[empNum] = int(input("Enter the number of hours worked by the employee: "))
            # Input validation for non-negative value
            while self.hours[empNum] < 0:
                print("Invalid value. Please enter a number equal to or greater than 0.")
                self.hours[empNum] = int(input("Enter the number of hours worked by the employee: "))

            # Retrieve hourly pay rate
            self.payRate[empNum] = int(input("Enter the employee's pay rate: "))
            # Input validation for non-negative value
            while self.payRate[empNum] < 0:
                print("Invalid value. Please enter a number equal to or greater than 0.")
                self.payRate[empNum] = int(input("Enter the employee's pay rate: "))

            # Calculate wages based on hours worked and pay rate
            self.wages[empNum] = self.hours[empNum] * self.payRate[empNum]
