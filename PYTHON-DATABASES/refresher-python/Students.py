"""
	Python Object Oriented
    ----------------------
    class - is a template for an Object
          - programmable part of the OOP
          
    Object properties
    ----------------
    1. instance properties - are properties(attribute/method-function)\
        that requires an instance of the class
    2. class/static properties - are properties that does not require an instance of a class 
    Object - is an instance of the class
"""
from os import system

#create a class in python
class Person(object):
    lastname = "bravo" # _ emulate the private declaration
    def __init__(self,lastname:str,firstname:str):
        self.lastname = lastname
        self.firstname = firstname
        
    #to string module- display the content of the object in a string format
    def __str__(self)->str:
        return self.lastname+" "+self.firstname
        
    def displayLastname()->str: #class/static module
        return self.lastname 
##############################################
class Student(Person):
    def __init__(self,idno:str,lastname:str,firstname:str,course:str,level:str):
        super().__init__(lastname,firstname)
        self.idno = idno
        self.course = course
        self.level = level
        
    def __eq__(self,otherobject)->bool:
        if self is otherobject: return True
        if type(self) != type(otherobject): return False
        if self.idno == otherobject.idno:
            return True
        else:
            return False
    
    def __str__(self)->str:
        return f"{self.idno} {super().__str__()} {self.course} {self.level}"


def main()->None: 
    system("cls")
    s1 = Student("0001","alpha","bravo","bscpe","4")
    s2 = Student("0002","sample","user","bsit","3")
    s3 = Student("0003","hello","world","bscs","2")
    s4 = Student("0004","oscar","quebec","bsit","2")
    
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    
    print(s1.__eq__(s2))

    
    

if __name__=="__main__":
    main()