#Logan Kilpatrick
#Lab 5
#10/16/2017
#MUST TEST WITH EXACT SAME #'s SHOWN IN LAB ASSIGNEMNT 
#19.5/20
from __future__ import with_statement


def saveChart(priceChart):
    '''
    takes in the list of lists
    returns nothing
    also updates file with "--" 
    saves the pricechart to the file 
    '''
    userFileName = input("Please enter file name or press 'Enter' for default file lab5input2.txt: ") # prompts user for file input 
    defaultFileName = "lab5input2.txt" #sets defualt file name 
    if(userFileName == ""): #if the user doesnt enter anthing, it goes to default 
        userFileName = defaultFileName
        print(userFileName + " updated")
    else:
        print(userFileName + " updated")
        
   
   
    #This block successfully reads in user data into a 2-D List called "priceChart"
    x = 0
    
    for line in priceChart:
        y = 0        
        for s in line:
            if( priceChart[x][y] == "X"):
                priceChart[x][y] = "--"            
            y += 1
        x += 1
        
    with open(userFileName, 'w') as f: 
        for _list in priceChart:
            for _string in _list: 
                f.write("%4s" %str(_string) + " ") 
            f.write("\n")
    
    raise SystemExit # exits out of infinite loop that duplicates data.....

#Need to loop though and get rid of "X"


def buySeat(priceChart):
    '''
    take in the priceChart list of lists
    returns nothing
    handles multiple user input excpetions
    
    
    calls printChart
    calculated total cost of seats 
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
                
            if ((int(userSeatInput[0])) > len(priceChart) or (int(userSeatInput[1])) > len(priceChart[0])):
                raise IndexError   
            
            if ((int(userSeatInput[0])) < 1 or (int(userSeatInput[1])) < 1):
                raise IndexError   
        
            if ((priceChart[int(userSeatInput[0])-1][int(userSeatInput[1])-1] == "X") or (priceChart[int(userSeatInput[0])-1][int(userSeatInput[1])-1] == "--")):
                raise UserWarning

            #print(userSeatInput)  
            
            #add up the price of the seat
            #mark the seat with an 'X' to show that it's taken
            #save the seat (row, col) location as a tuple in a list of tuples
            
            
            priceOfSeat = priceChart[int(userSeatInput[0]) - 1][int(userSeatInput[1]) - 1]
            #print(priceOfSeat)            
            priceOfSeat = int(priceOfSeat[:]) # converts user input into a usable string! 
            #THIS WAS JUST CHANGED
            #print(priceOfSeat)            
            
            totalCostOfSeats += priceOfSeat#adds up total cost of seats! 
            
            priceChart[int(userSeatInput[0])-1][int(userSeatInput[1])-1] = "X"
            
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
         
    print("\nYour total is : $" + str(totalCostOfSeats))
    print("Your " + str(len(listOfSeats)) + " seat(s) at " + str(listOfSeats)[1:-1]  + " are marked with an 'X'")
    
    printChart(priceChart)        
    #print(listOfSeats)
    #print(type(listOfSeats[0]))
    #
    #saveChart(priceChart)
    #
    #
    
def printChart(priceChart):
    '''
    takes in price chart list of list
    does not need to return anything
    simply prints the formatted price chart with the correct headings 
    called from main and other functions 
    '''
    
    temp = "Row  " + "=" * (5 * len(priceChart[0]))#prints dashes proportinal to the number of elements 
    priceTitle = (" " * int(len(temp)/2)) + "Price Chart"
   
    print(priceTitle)
    column = (" " * int(len(temp)/2)) + "Column"#prints colum at the mid-point! 
    print(column)
    z = 0
    holder = "       "
    while ( z < len(priceChart[0])):
        holder += (str(z+1) + "    ")
        z+=1
    print(holder)
    print(temp)    
    
    i = 1
    #Loops through each element of the array! 
    for r in range(len(priceChart)):  
        print(str(i) + " | ", end= " ")#does row formatting 
        i += 1
        for c in range(len(priceChart[r])):  
            if (priceChart[r][c] == "X"):
                print("%4s" %(priceChart[r][c]), end= " ")     
                
            elif (priceChart[r][c] != "--"):
                print("%4s" %("$" + priceChart[r][c]), end= " ")
                
            else:
                print("%4s" %(priceChart[r][c]), end= " ")
                
        print()  
    print()
    

def readChart():  #this happends first! 
    '''
    first part to run
    takes in no parameters
    returns the list of lists read in from the user specified file 
    '''
    
    userFileName = input("Please enter file name or press 'Enter' for default file lab5input2.txt: ") # prompts user for file input 
    priceChart = []
    defaultFileName = "lab5input2.txt" #sets defualt file name     
    
    if (userFileName == ""):
        userFileName = defaultFileName
        
    while(userFileName != ""):
        try:
                    
            with open(userFileName) as f:
                for line in f:
                    numberSplit = line.split() #Split the data at the white space.  
                    row = [n for n in numberSplit]  
                    priceChart.append(row) 
            
            
            return(priceChart)
            
        except FileNotFoundError as e: #Input file doesn't exist: print "file not found" message and re-prompt
            print("Can't open " + userFileName)
            userFileName = input("Enter filename: ")
            
            if (userFileName == ""):
                userFileName = defaultFileName            
        
    

def main():
    '''
    main function
    returns nothing
    takes in nothing
    just calls the other programs
    some might say "Driver" class 
    '''
    priceChart = readChart()#calls file read method 
    printChart(priceChart)
    buySeat(priceChart)
    saveChart(priceChart)
    
    
main()