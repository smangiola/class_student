class Student:
    #Class attribute - shared by all instances of a student
    #this is the same for every student
    school = "Shiz University"
    def __init__(self, name, age, grade):
        self.name = name #each student may have a different name
        self.age = age #each student may have a different age
        self.grade = grade #each student may have a different grade
    
    #Method to get information about the student
    def get_info(self):
        return f"{self.name} is {self.age} in grade {self.grade} at {self.school}"
    
#create two student instances
student1 = Student("Samantha", 19, "Sophmore")
student2 = Student("Amanda", 21, "Senior")

#print the information about the students
print(student1.get_info())
print(student2.get_info())