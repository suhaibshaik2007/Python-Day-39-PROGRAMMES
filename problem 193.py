# PROPERTY FOR MARKS
class Student:
    def __init__(self,marks):
        self._marks = marks

        @property
        def marks(self):
            return self._marks

        @marks.setter
        def marks(self,value):
            if 0 <= marks <= 100:
                self._marks = value
            else:
                print("Invalid Marks")

                s = Student(80)

                print(s.marks)

                s.marks = 95
                print(s.marks)

                s.marks = 120