# SALARY SETTER
class Employee:
    def __init__(self,salary):
        self._salary = salary

        @property
        def salary(self):
            return self._salary

        @salary.setter
        def salary (self,value):
            if value > 0:
                self._salary = value
            else:
                print("Invalid Salary")

                e = Employee(30000)
                print(e.salary)

                e.salary = 25000
                print(e.salary)

                e.salary = -1000