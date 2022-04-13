import functions
import os
import getpass
import os.path
import random

#get windows/linux username for path
user=getpass.getuser()




#path for testing
FILE="/home/{user}/Documents/Using-Pytest-Methods-and-Tools-22/testing.txt"
FILE1="/home/{user}/Documents/Using-Pytest-Methods-and-Tools-22/testing1.txt"


#testing openFile()

#should pass if testing.txt exists
# def test_openFile():
#     functions.openFile(FILE)
#     assert os.path.exists(FILE) == 1 #essentially stat file
    

# #should fail if testing1.txt does not exist
# #will pass if set equal to 0, due to it not existing. Could also just touch testing1.txt and will pass
# def test_openFile_nofile():
#     functions.openFile(FILE1)
#     assert os.path.exists(FILE1) == 1



# #should fail due to invalid type input
# #will pass if a path to file, which is supplied in string format.
# def test_openFile_invalidtype():
#     assert functions.openFile(1)




# #testing numbers()
# #should pass with supplied ints
# def test_numbers():
#     assert functions.numbers(3,1)==3
# #should fail due to division by zero
# #will pass if second input is !0
# def test_numbers_dividebyzero():
#     assert functions.numbers(3,0)==0
# #should fail due to invalid type being input
# #will pass if converted to ints first
# def test_numbers_invalidtype():
#     assert functions.numbers("3","1")




# #testing dist()



#manually testing function
#print(functions.dist(2,2,1,1))

# #should pass with supplied ints
# def test_dist():
#     assert functions.dist(2,2,1,1)==1.4142135623730951
# #should not pass but does in this configuration. How many decimal places are considered?

# def test_numbers_noteq():
#     assert functions.dist(2,2,1,1)==1.4142135623730952
# #explores equality with first decimal point. It fails

# def test_numbers_noteq1():
#     assert functions.dist(2,2,1,1)==1.5142135623730952
# #fails due to string input
# #would pass if converted to ints before
# def test_numbers_invalidtype():
#     assert functions.dist("2,2,1,1")==1.4142135623730952





# #testing isPalindrome()
#should pass
# def test_isPalindrome():
#     assert functions.isPalindrome("racecar")==True
# #should pass
# #would fail if set to True
# def test_isPalindrome_False():
#     assert functions.isPalindrome("test")==False
# #will fail due to invalid type input to function
# #will pass if converted to string that is also a palindrome
# def test_isPalindrome_invalidtype():
#     assert functions.isPalindrome(1)==True



# #testing divide()
def test_divide():
    monkeypatch.setattr('builtins.input', lambda _: 3) #while monkeypatching (:]) has a broader scope than just mocking, i am using it here for mocking
    monkeypatch.setattr('builtins.input', lambda _: 1)
    assert functions.divide(3,1)==3 

def test_dividebyzero():
    monkeypatch.setattr('builtins.input', lambda _: 3)
    monkeypatch.setattr('builtins.input', lambda _: 0)
    assert div==0

def test_divide_invalidtype():
    monkeypatch.setattr('builtins.input', lambda _: "three")
    monkeypatch.setattr('builtins.input', lambda _: "one")
    assert div==3





# #testing sq
# def test_sq():
#     assert functions.sq(49)==7

# def test_sq_False():
#     assert functions.sq(49)==8

# def test_sq_invalidtype():
#     assert functions.sq("49")==7



# #testing greetUser
# def test_greetUser():
#     assert functions.greetUser(josh, jordan, moore)==1

# # def test_sq_False():
# #     assert functions.greetUser(1, middle, last)

# # def test_sq_invalidtype():
# #     assert functions.sq("49")==7



# #testing displayItem()




# ## takes in a Python list
# ## attempts to display the item at the index provided
# def displayItem(numbers, index):
#     print("Your item at", index, "index is", numbers[index])
