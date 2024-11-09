# Define the Student class and demonstrate inheritance

# Step 1: Define the Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    # Method for studying
    def study(self):
        print(f"{self.name} is studying")
    
    # Method for attending class
    def attend_class(self):
        print(f"{self.name} is attending class")

# Step 2: Define subclasses UndergraduateStudent, GraduateStudent, and PhDStudent inheriting from Student
class UndergraduateStudent(Student):
    def prepare_for_exam(self):
        print(f"{self.name} is preparing for undergraduate exams")

class GraduateStudent(Student):
    def write_thesis(self):
        print(f"{self.name} is writing a thesis")

class PhDStudent(Student):
    def conduct_research(self):
        print(f"{self.name} is conducting research")

# Step 3: Create instances of UndergraduateStudent, GraduateStudent, and PhDStudent
undergraduate = UndergraduateStudent("Alice", 101)
graduate = GraduateStudent("Bob", 102)
phd_student = PhDStudent("Charlie", 103)

# Step 4: Call methods from the Student class and their own methods
undergraduate.study()        # Output: Alice is studying
undergraduate.attend_class() # Output: Alice is attending class
undergraduate.prepare_for_exam() # Output: Alice is preparing for undergraduate exams

graduate.study()             # Output: Bob is studying
graduate.attend_class()      # Output: Bob is attending class
graduate.write_thesis()      # Output: Bob is writing a thesis

phd_student.study()          # Output: Charlie is studying
phd_student.attend_class()   # Output: Charlie is attending class
phd_student.conduct_research() # Output: Charlie is conducting research
