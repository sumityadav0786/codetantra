"""
A class consists of 4 key members:
Constructor: The constructor must have a special name _init_() and a special parameter called self. In Python, the constructor is invoked automatically whenever a new object of a class is instantiated.
Class variable / Class attribute: A class variable contains information that is shared by all objects of the class.
Instance variable / Instance attribute: An attribute that is created per instance/object.
Method(s): A function that can access any of these variables.
Consider the below example in which a class Student is created with each student data as a specific instance of that class.

Understand and retype the following program.

Note: The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. This is commonly used for creating minimal classes.
Sample Test Cases
Test Case 1:
Expected Output:
Stud_1.name:·SriRam
Stud_1.age:·25
Stud_1.graduate:·MBA
Stud_2.name:·Lakshman
Stud_2.age:·23
Stud_2.graduate:·Engineer
"""

class Student:
  pass
Stud_1=Student
Stud_2=Student
Stud_1.name="Sriram"
Stud_1.age=25
Stud_1.graduate="MBA"
Stud_2.name="Lakshman"
Stud_2.age=23
Stud_2.graduate="Engineer"
print("Stud_1.name:",·Stud_1.name)
print("Stud_1.age:",·Stud_1.age)
print("Stud_1.graduate:",·Stud_1.graduate)
print("Stud_2.name:",·Stud_2.name)
print("Stud_2.age:",·Stud_2.age)
print("Stud_2.graduate:",·Stud_2.graduate)
