class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def increase_salary(self, percent):
        self._salary += self._salary * percent / 100

    def __str__(self):
        return f"Employee: {self._name}, Salary: {self._salary}"

    def show_details(self):
        print(f"Employee details:\nName: {self._name}\nSalary: {self._salary}")
        
if __name__ == "__main__":
    emp = Employee("John Doe", 5000)
    emp.show_details()
    emp.increase_salary(10)
    emp.show_details()

