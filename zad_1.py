from statistics import mean

class Student:
    def __init__(self, name: str, marks: list ) -> None:
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"
    
    def is_passed(self) -> bool:
        return True if mean(self.marks) > 2.5 else False
     

student1 = Student("Mateusz", [5,2,2,2])
student2 = Student("Michał", [5,2,3,2])
student3 = Student("Martyna", [5,5,3,2])
#print(student1.is_passed())
#print(str(student1))