#Lab 7 Chart Class 
#Logan Kilpatrick 
#imports the seat class and its sub-classes! 


from seat import Seat, Premium, Regular, Choice

class Chart:
    
    '''
    An instance variable chart which is the list of lists of Seat objects.
    A constructor that has similar functionality to the readChart function of lab5:
    prompt the user for a filename or enter key to use the default file lab7input2.txt 
    read in the first line of the input file, which has the 3 prices in order of: premium, choice, and regular.
    read in the rest of the input file, and for each price, create the appropriate Seat object (Premium, Choice, or Regular) to store in the list of lists.
    call the print method to print the seating chart with prices.
    A print method that has similar functionality to the printChart function of lab5:
    print the row and column headers
    print the seating chart with prices or with 'X', columns right justified  (see sample output)
    A buySeat method that has the same functionality as the buySeat method of lab5:
    in a loop:
    prompt the user for the row, col or 0 to end the loop
    check that the row, col values are valid, and if the seat is available, mark the seat with 'X', sum up the price, and store the row,col location in a tuple..
    when the loop ends, print the total cost, and for each seat's row,col location, print the extra perks, and then print the resulting seating chart with 'X' for the seats that are bought. See sample output.
    Be careful in the Chart class: don't directly use private instance variables of the Seat class, use the Seat methods instead.
    '''
    
    def printI(self):
        '''
        A print method that has similar functionality to the printChart function of lab5:
        print the row and column headers
        print the seating chart with prices or with 'X', columns right justified  (see sample output)
        takes in no parameters. Prints formated chart.
        '''
        
        temp = "Row  " + "=" * (5 * len(self._priceChart[0]))#prints dashes proportinal to the number of elements 
        priceTitle = (" " * int(len(temp)/2)) + "Price Chart"
       
        print(priceTitle)
        column = (" " * int(len(temp)/2)) + "Column"#prints colum at the mid-point! 
        print(column)
        z = 0
        holder = "       "
        while ( z < len(self._priceChart[0])):
            holder += (str(z+1) + "    ")
            z+=1
            
        print(holder)
        print(temp)    
        i = 1
        for r in range(len(self._priceChart)):  
            print(str(i) + " | ", end= " ")#does row formatting 
            i += 1
            for c in range(len(self._priceChart[r])):  
                if (self._priceChart[r][c].getPrice() == "X"):
                    print("%4s" %(self._priceChart[r][c].getPrice()), end= " ")     
                else:
                    print("%4s" %(self._priceChart[r][c].getPrice()), end= " ")
                    
            print()  
        print()        
        
        
        
    def __init__ (self):
        ''' constructor... takes in no paramaters... creates the chart.  
        filles it with a list if list of objects with the repsecive types '''
        
        premium = ""
        choice = ""
        regular = ""
        
        userFileName = input("Please enter file name or press 'Enter' for default file lab7input2.txt: ") # prompts user for file input 
        self._priceChart = []
              
        defaultFileName = "lab7input2.txt" #sets defualt file name     
        if (userFileName == ""):
            userFileName = defaultFileName
            
        while(userFileName != ""):
            try:
                        
                with open(userFileName) as f:
                    for line in f:
                        row = []
                        
                        numberSplit = line.split() #Split the data at the white space.  
                        if len (numberSplit) == 3:
                            premium = numberSplit[0] #sets the premium choice thing ! 
                            choice = numberSplit[1] #sets the premium choice thing ! 
                            regular = numberSplit[2] #sets the premium choice thing ! 
                        else:
                            for n in numberSplit:
                                if n == premium:
                                    #t = Premium(n)
                                    row.append(Premium(n))
                                elif n == choice:
                                    row.append(Choice(n))
                                elif n == regular:
                                    row.append(Regular(n))                                
                            #row = [Premium(n) for n in numberSplit if n == numberSplit[0]]  
                            self._priceChart.append(row)
    
                self.printI()
                break
            
                    
            
            except FileNotFoundError as e: #Input file doesn't exist: print "file not found" message and re-prompt
                print("Can't open " + userFileName)
                userFileName = input("Enter filename: ")
                
                if (userFileName == ""):
                    userFileName = defaultFileName    
            
        
    def buySeat(self):
        '''
        A buySeat method that has the same functionality as the buySeat method of lab5:
        in a loop:
        prompt the user for the row, col or 0 to end the loop
        check that the row, col values are valid, and if the seat...
        is available, mark the seat with 'X', sum up the price, and store the row,col location in a tuple..
        when the loop ends, print the total cost, and for each seat's row,col ....
        location, print the extra perks, and then print the resulting seating chart ...
        with 'X' for the seats that are bought. See sample output...
        
        '''
        
        '''
        take in the priceChart list of lists
        returns nothing
        handles multiple user input excpetions
        
        
        calls printChart
        calculated total cost of seats 
        updated for lab 7 to use the functions we crearted in the seat and chart class. 
        '''
        userSeatInput = (0,0)
        totalCostOfSeats = 0
        listOfSeats = []
        while True:#Part 5
            try:#exception handeling for simplicty sake.... Covers all negative numbers and invalid inputs! 
                my_list = input("Please enter the desired seat number or 0 to end: ")
                userSeatInput = my_list.split(",")       
                
                #userSeatInput = tuple(userSeatInput)
                if((int(userSeatInput[0]) == 0) and (len(userSeatInput) == 1)):#end of program check! 
                    break
                    
                if ((int(userSeatInput[0])) > len(self._priceChart) or (int(userSeatInput[1])) > len(self._priceChart[0])):
                    raise IndexError   
                
                if ((int(userSeatInput[0])) < 1 or (int(userSeatInput[1])) < 1):
                    raise IndexError   
            
                if (self._priceChart[int(userSeatInput[0])-1][int(userSeatInput[1])-1].isTaken() == True):
                    raise UserWarning
                
                
                priceOfSeat = (self._priceChart[int(userSeatInput[0]) - 1][int(userSeatInput[1]) - 1].getPrice())
                priceOfSeat = int(priceOfSeat[:]) # converts user input into a usable string!          
                
                totalCostOfSeats += priceOfSeat#adds up total cost of seats! 
                
                self._priceChart[int(userSeatInput[0])-1][int(userSeatInput[1])-1].setPrice("X")
                self._priceChart[int(userSeatInput[0])-1][int(userSeatInput[1])-1].setTaken(True)
                
                listOfSeats.append((int(userSeatInput[0]), int(userSeatInput[1])))
                           
                
            except UserWarning: # does index valeu out of range 
                print("Sorry, it looks like that seat has already been purchased. Please try again.")
                continue             
            except ValueError: #value error exception.... --Non-number inputs
                print("Sorry, input must be integars, please try again!")
                continue
            except TypeError as e:
                print(str(e))
                continue 
            except IndexError as e:
                print("invalid row / col, please try again.")
                continue
        self.printI()      #calls the print statement 
        print("\nYour total is : $" + str(totalCostOfSeats))
        print("Your " + str(len(listOfSeats)) + " seat(s) at : \n" + str(listOfSeats)[1:-1]  + " are marked with an 'X'")
        for a, b in listOfSeats:#loops though the tupple. 
                print(str(a) + "," + str(b) + self._priceChart[int(a)-1][int(b)-1].getExtra() )