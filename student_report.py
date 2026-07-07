class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >=60:
            return "B"
        elif self.marks >=40:
            return "C"
        else:
            return "Fail"
s1= student("ali",85)
s2 = student("ahmed", 62)
s3 = student("ahmed", 45)
                      
students = [s1, s2, s3]
for s in students:                        
    print(f"Name: {s.name} Marks: {s.marks} Grade: {s.grade()}")
passed = 0
failed = 0
for s in students:
    if s in students:
        if s.grade() == "Fail":
            failed += 1
        else:
            passed += 1
print(f"\nTotal Passed: {passed}")
print(f"Total Failed: {failed}")