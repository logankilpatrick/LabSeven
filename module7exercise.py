# Module 7 exercise
# Test driver for people class and subclasses

# 1. Create a new file called person.py that contains
# a person class. The person object can be created 
# with a required name and an optional age, default to 0

# 2. Add to the person class so that the following main
# can run successfully

# import the correct Person class:
from person import Person, Employee, Student
#person here is a file name, but dont include the .py


# create aperson and print
aperson = Person("Fred") #creates a person object calling __init__
print(aperson)


# create bff and increment age 2 times, then print
bff = Person("Wilma")
bff.happyBday()   # print: Happy Birthday, Wilma You're 1 today
bff.happyBday()   # print: Happy Birthday, Wilma You're 2 today   
print(bff)


# who's younger?
if aperson == bff:
    print("Same age")
elif aperson < bff:
    print(aperson.getName(), "is younger")
else:
    print(bff.getName(), "is younger")
    
# invalid age?
try:
    
    testperson = Person("name", "age")
    if testPerson < bff:
        print("test person is younger")    
except ValueError as e:
    print(e)
    

    


# 3. Add a subclass of the Person class:
# Employee: 
# add a new optional field called salary,
#   defaulted to 0
# override the happyBday method so it adds 1
# to the age and print "Happy Birthday"
#              
# Student: with additional optional field called
# major, default to "undeclared"
# override the happyBday method so it does 
# what the Person class method does, and 
# then print "You're getting a free textbook"

# create an employee
e = Employee("Pebbles", 20, 15)
print(e)
e.happyBday()

# create a student
s = Student("Bam Bam", 18, "music")
print(s)
s.happyBday()
    
# polymorphism
def bdayWish(p): # function 
    p.happyBday()
    
# What is printed?
bdayWish(bff)    
bdayWish(e)
bdayWish(s)
