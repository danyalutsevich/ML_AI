
class Student :
    def __init__(self, name, surname, occupation="Base"):
        self.name = name
        self.surname = surname
        self.occupation = occupation
        self.grades = {}

    def add_grade(self,**data):
        self.grades[data["course"]] = data["grade"]

    def gpa(self):
        if(len(self.grades)==0):
            return 0
        else:
            sum = 0
            for grade in self.grades.values():
                sum += grade
            return sum / len(self.grades)

    def print(self):
        print(self.name, self.surname, self.occupation, self.grades, self.gpa())

person = Student("Joe", "Biden")

person.add_grade(course="Math", grade=90)
person.add_grade(course="English", grade=90)
person.add_grade(course="Science", grade=70)
person.add_grade(course="History", grade=90)
person.add_grade(course="Art", grade=50)
person.add_grade(course="Music", grade=40)
person.add_grade(course="PE", grade=30)
person.add_grade(course="Computer Science", grade=20)

person.print()