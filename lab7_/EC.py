# List of lists to dictionary extra credit

from seat import Premium, Choice, Regular

# read from file into chart
chart = []    
with open("lab7input2.txt") as infile:
    (premium, choice, regular) = infile.readline().split()# this replaces is,elif,elif
    for line in infile :   
        row = []
        for item in line.split() :   # build each row
            if item == premium :
                seat = Premium(premium)
            elif item == choice :
                seat = Choice(choice)
            else :
                seat = Regular(regular)
            row.append(seat)
        chart.append(row)     

# print chart
print()
for row in range(len(chart)):    
    for seatObj in chart[row]:
        print("%5s" % seatObj.getPrice(), end="")
    print()         
print()   

# buy 3 seats        
for i in range(3) : 
    val = input("Enter row,col: ")
    (row, col) = [int(elem) - 1 for elem in val.split(',')]

    if chart[row][col].isTaken() == False:#this needs to change 
        chart[row][col].setPrice('X')   # set seat to 'X'
    else:
        print("Sorry, that seat is not available.")

# print chart
print()
for row in range(len(chart)):
    for seatObj in chart[0]:
        print("%5s" % seatObj.getPrice(), end="")
    print()         
print() 
        

