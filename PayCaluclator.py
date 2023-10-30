class PayCalculator:

    def __init__(self):
        # Initialize lists to store calculated wages for week, month, and year
        self.wages_week = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        self.wages_month = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        self.wages_year = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

    def pay_calculator_week(self, hours, pay):
        # Calculate wages for each employee per week
        for eachEmployee in range(len(hours)):
            self.wages_week[eachEmployee] = hours[eachEmployee] * pay[eachEmployee]

        # Print and return the weekly wages
        print(f"Wages per week: {self.wages_week}")
        return self.wages_week

    def pay_calculator_month(self, hours, pay):
        # Calculate wages for each employee per month (assuming 4 weeks per month)
        for eachEmployee in range(len(hours)):
            self.wages_month[eachEmployee] = hours[eachEmployee] * pay[eachEmployee] * 4

        # Print and return the monthly wages
        print(f"Wages per month: {self.wages_month}")
        return self.wages_month

    def pay_calculator_year(self, hours, pay):
        # Calculate wages for each employee per year (assuming 4 weeks per month and 12 months per year)
        for eachEmployee in range(len(hours)):
            self.wages_year[eachEmployee] = hours[eachEmployee] * pay[eachEmployee] * 4 * 12

        # Print and return the yearly wages
        print(f"Wages per year: {self.wages_year}")
        return self.wages_year
