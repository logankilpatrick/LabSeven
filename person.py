#person class
class Person: # class names start with capitals! 
    #if declared/initalized here, it is static by deafult and shared by all objects of the class 
    
    '''
    def __init__(self): #takes in no arguemnts -- object = person()
    Always a good idea to initalize all instance variables in the constructor 
    
    
    '''
    def __init__ (self, name, age = 0) : #self arguemnt makes it a method of a class
        #only allowed constructor 
       #constructor
        #try: 
        #    self._age = int(age)
        #except ValueError:
        #    print("age has to be an integar")
        if isinstance(age, int): #tests wheter age is an int 
            self._age = age
        else:
            raise ValueError("age needs to be an int")
            #raises accept and exits constructor. never makes object! 
        
        self._location = "cupertino" #default(need a get and set to change) #it is possble to init 
                                     # instance varibales without the user
        self._name  = name#self makes it an instance variable  and unerscore makes it private  
        
        
    def __repr__(self): #print statement that shows the info about the objects 
        return "Name: " + self._name + ", Age: " + str(self._age) # this is called by default when you print an object 
    
    def happyBday(self):
        '''increments the age and retruns the string'''
        self._age += 1
        print("Happy Birthday", self._name, "You're", self._age, "today")
        
    '''getters are methods that allow use to fetch a paricular instance variable value'''    
    def getName(self):
        '''returns the name'''
        return self._name
    
    '''setters are methods that allow use to chnage a vlaue of a paricular instance variable value'''        
    def setName(self, newName):
        '''sets the new variable name'''
        self._name = newName

    '''overloading methods... overload certian operators '''
    #overloads the == operator 
    def __eq__ (self, rhs): #rhs = right hand side object 
        return(self._age == rhs._age)
    #overloads the < operator 
    def __lt__ (self, rhs): #rhs = right hand side object 
        return(self._age < rhs._age)    
    
class Employee(Person):
    def __init__ (self, name, age = 0, salary = 0) : #self arguemnt makes it a method of a class
        super().__init__(name, age) #child class can rewrite requirments. parent ownes these values 
        self._salary = salary 
    
    def happyBday(self):
        '''increments the age and retruns the string'''
        self._age += 1
        print("Happy Birthday", self._name)    
    
    
class Student(Person):
    def __init__ (self, name, age = 0, major = "undeclared") :
        super().__init__(name, age)
        self._major = major


    def happyBday(self):
        '''increments the age and retruns the string'''
        super().happyBday()#this is fo demostartion, not fater than rewriting myself here 
        print("your getting a free text book")    
        #self arguemnt makes it a method of a class
        