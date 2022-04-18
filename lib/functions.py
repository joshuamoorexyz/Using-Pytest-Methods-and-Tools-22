import math
import sys     






## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        string_int=str(filename)
        infile = open(string_int, "r")
        print("File opened.")
    except error:
        print("Please enter a string")




## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        intfromstring=int(num1)
        intfromstring1=int(num2)
        if(intfromstring1==0):
            print("Please enter a non zero number for num2")
            sys.exit("Error message")
        else:
            return intfromstring / intfromstring1
    except error:
        print("Please enter an integer")






## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        intfromstringx1=int(x1) #changing style only bc its easier to keep track of here :)
        intfromstringy1=int(y1)
        intfromstringx2=int(x2)
        intfromstringy2=int(y2)
        dist = (intfromstringx2 - intfromstringx1) ** 2 + (intfromstringy2 - intfromstringy1) ** 2
        dist = math.sqrt(dist)
        dist = math.ceil(dist)
        return dist
    except error:
        print("please enter integer values instead")

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        stringfromint=str(temp)
        test = stringfromint[::-1]
        if(test == stringfromint):
            return True
    except error:
        print("please enter integer values instead")


## has input to receive two numbers
## divides the two, then outputs the result


    #requires input testing
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if(num2==0):
        print("Please enter a non zero number for num2")
        sys.exit("Error message")
    div = num1/num2
    print("Your numbers divided is:", div)
    return div 
    
    #by returning div here we save the trouble of having to test the output from up above. 
    #to test the output an example is shown in the notes, but after monkeypatching input,the output would 
    #have to be captured. 





## returns the squareroot of a particular number
def sq(num):
    number=int(num)
    return math.sqrt(number)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")





## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    if(index < 0 or index > len(numbers)): #check to see if index size is greater than zero but not out of bounds
        sys.exit("Error message")
    else:
        print("Your item at", index, "index is", numbers[index])
