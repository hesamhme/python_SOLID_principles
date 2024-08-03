'''
in SRP each class should has one reason to change, has one job and doing one job
'''
# Before SRP
# Class validateperson should has one job to validate name and age, function display is against the SRP

class ValidatePerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def validate_name(self, name):
        if len(name) > 3:
            return True
        else:
            return False

    def validate_age(self, age):
        if age > 18:
            return True
        else:
            return False

    def display(self):
        if self.validate_name(self.name) and self.validate_age(self.age):
            print(f"Name: {self.name} and Age: {self.age}")
        else:
            print("Invalid")


# After Using SRP

class ValidatePerson:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def validate_name(self, name):
        if len(name) > 3:
            return True
        else:
            return False

    def validate_age(self, age):
        if age > 18:
            return True
        else:
            return False

# using a seprate class for display

class DisplayPerson:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.validate = ValidatePerson(self.name, self.age)

    def display(self):
        if (
            self.validate.validate_name(self.name) and 
            self.validate.validate_age(self.age)
        ):
            print(f"Name: {self.name} and Age: {self.age}") 
        else:
            print("Invalid")