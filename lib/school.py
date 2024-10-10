class user:
    def __init__(self, name):
        print("User.__init__called.")
        self.name = name
        
        
    def log_in(self):
        self.logged_in = True
        
class student(user):
    def __init__(self, name, grade):
        print("Student.__init__called.")
        super().__init__(name)
        self.grade = grade
        
    def log_in(self):
        super().log_in()
        self.in_class = True
        
oneil = student("O'neil", 10)
print(oneil.name)  # Output: O'neil
print(oneil.grade)  # Output: 10