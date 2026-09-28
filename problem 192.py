# SETTER WITH VALIDATION

class Student:
    def __init__(self,age):
        self._age = age

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self,value):
            if value >= 0:
                self._age = value
            else:
                print("Age cannot br negative")

                s = Student(18)

                print(s.age)

                s.age = 20
                print(s.age)

                s.age = -5
                print(s.age)