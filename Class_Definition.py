# Class in an abstraction of a entity which has a common set of properties and methods
# Object of a Class: Object is a specific instance of a Class

class Person:
    class_var = "Gokhale"           # Class variable
    
    def __init__(self, name):
        # self is the class itself - self refers to to current instance of the class
        # self gives access to instance variables and other methods defined in the class 
        # self is used to define properties of the class
        self.name = name
    # The __init__() method will be called every time we create a instance of this call
    # Even if we don't define the 
    
    # Instance Methods
    def greet(self):
        print("Hello my first name is", self.name)
        # Here using the self method we could access the variable from __init__ method - Accessing the instance variables
    
    def introduce(self):
        self.greet()  
        # Here we called another method defined in Person class using self
        
    @staticmethod  
    def static_method():
        print("This is a static method")
    
    @classmethod
    def class_method(cls):
        print("My last name is", cls.class_var)

p = Person("Atharva")        # Now we have created an instance/ object of class Person - p is instance of class Person
# If we have passed any arguement apart from self to the __init__ function, we need to pass the value for that arguement every time we create an instance of that class
# Thus, the __init__ method is called automatically when we create a instance of a class
# p.introduce()

#When you call p.introduce(), Python implicitly passes the instance p as the first argument — that's self.
#Then inside introduce, you're calling self.greet(), which again passes the same self to the greet method

# Person.static_method()
# This is a static method - This does not depend on the instance of the class 
# If I have would have called it as: p.static_method() it will throw an error. As the __init__ method expects an arguement to be passed, whereas the static_method is not having any arguement
        
p.introduce()
Person.class_method()