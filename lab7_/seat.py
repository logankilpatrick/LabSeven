#Lab 7 Seat Class with respective sub classes
#Logan Kilpatrick 
#Implimented by lab7.py
#imported by chart class

class Seat:
    '''
    The Seat class has:
    instance variables price and taken (a boolean).(parent class)
    a constructor that initializes the taken attribute to False and ...
    has a default argument price which you should provide a default value. 
    an abstract method getExtra that requires all subclasses to implement it.#read abstract class notes!!! 
    '''
    def __init__(self, price = 0, taken = False,):
        '''constructor. takes in 2 paremeters if the user provides them, otherwise, sets them to said default values. '''
        self._price = price
        self._taken = taken 
    
    def getExtra(self):#abstract class, look up implimentation. forces the child class to have zero parameters 
        raise NotImplementedError
    def isTaken(self):
        '''isTaken: return True if the seat is taken, False if the seat is still available '''
        return (self._taken == True) 
    def setTaken(self, nowTaken):
        '''sets the origional with true or false. takes in the value to set it with as a parameter '''
        self._taken = nowTaken
        return (self._taken)
    def getPrice(self):
        '''getPrice: return the value in the instance variable price'''
        return(self._price)
    def setPrice(self, price):
        '''Sets the origional price.  Takes in a parameter and sets the prcie to that number.'''
        self._price = price
    def __repr__(self): #print statement that shows the info about the objects 
        return self._price   
   
    
class Premium(Seat):
    def __init__(self, price):
        '''takes in a price and then passes the price to the superclasses(parents) constructor '''
        super().__init__(price)
    def getExtra(self):
        '''prints the extra info about the Premium ticket'''
        
        return(" : your swag bag, drink, and ticket are at will call")
     
    
class Choice(Seat):
    def __init__(self, price):
        '''takes in a price and then passes the price to the superclasses(parents) constructor '''        
        super().__init__(price)  
    def getExtra(self):
        '''prints the extra info about the Choice ticket'''
        
        return(" : your drink ticket and ticket are at will call")    
   
    
        
class Regular(Seat):
    def __init__(self, price):
        '''takes in a price and then passes the price to the superclasses(parents) constructor '''        
        super().__init__(price)
    def getExtra(self):
        '''prints the extra info about the Regular ticket'''
        return(" : your ticket is at will call")    
    
    
    
        
    