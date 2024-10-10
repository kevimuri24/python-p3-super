class User:
    def log_in(self):
        self.logged_in = True
        
class Student(User):
    def log_in(self):
        super().log_in()
        self.in_class = True
        
print(issubclass(Student, User))  # Output: True