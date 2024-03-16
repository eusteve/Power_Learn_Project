#python code to illustrate classes and objects in python
class Person:
    def __init__(self,name,age,gender): #ctor
        self.name = name
        self.age = age 
        self.gender = gender

    def introduce(self):
        print(f"user details:  \n hello {self.name}, \n age : {self.age}, \n gender: {self.gender} \n")
        pass

adult = Person('james',21,'male')
adult.introduce() #method displays 

