#person class
class Person: # class names start with capitals! 
    def __init__ (self, name, age = 0) : #self arguemnt makes it a method of a class
       #constructor
        self._name  = name#self makes it an instance variable  and unerscore makes it private  
        self._age = age 
        
    def __repr__ (self):
        #convert object into a string
        return "Name: " + self._name + ", Age: " + str(self._age)
        
    def happyBday():
        