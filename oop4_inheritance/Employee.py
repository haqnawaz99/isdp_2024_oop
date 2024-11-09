# Define a base Employee class to demonstrate inheritance with calculating salary and displaying information

# Step 1: Define the Employee class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    # Method to display the name of the employee
    def display_info(self):
        print(f"Employee Name: {self.name}")

    # Placeholder method for calculating salary
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

# Step 2: Define the FullTimeEmployee class inheriting from Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    # Method to calculate the total salary for full-time employees
    def calculate_salary(self):
        return self.base_salary + self.bonus

# Step 3: Define the PartTimeEmployee class inheriting from Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Method to calculate the total salary for part-time employees
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Step 4: Define the Intern class inheriting from Employee
class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, stipend)
        self.stipend = stipend

    # Method to calculate the total salary for interns
    def calculate_salary(self):
        return self.stipend

# Step 5: Create instances of FullTimeEmployee, PartTimeEmployee, and Intern
full_time_employee = FullTimeEmployee("Alice", 50000, 10000)
part_time_employee = PartTimeEmployee("Bob", 20, 80)
intern = Intern("Charlie", 1000)

# Step 6: Call methods for each instance
# FullTimeEmployee methods
full_time_employee.display_info()  # Output: Employee Name: Alice
print(f"Total Salary: ${full_time_employee.calculate_salary()}")  # Output: Total Salary: $60000

# PartTimeEmployee methods
part_time_employee.display_info()  # Output: Employee Name: Bob
print(f"Total Salary: ${part_time_employee.calculate_salary()}")   # Output: Total Salary: $1600

# Intern methods
intern.display_info()              # Output: Employee Name: Charlie
print(f"Total Salary: ${intern.calculate_salary()}")               # Output: Total Salary: $1000
