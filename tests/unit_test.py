from lib.functions import *
import os
import getpass
import os.path
import unittest.mock as mock
from unittest.mock import patch
import pytest




##From https://youtu.be/UMgxJvozR5A as reference

#input function for passing input to function that need it
def geninputs():
    inputs = ["3","1"]

    for item in inputs:
        yield item

def geninputs1():
    inputs = ["3","0"]

    for item in inputs:
        yield item

def geninputs2():
    inputs = ['3','1']

    for item in inputs:
        yield item


#sets up our inputs
GEN = geninputs()
GEN1=geninputs1()
GEN2=geninputs2()

#get windows/linux username for path
#user=getpass.getuser()     not working in vscode? need to debug or remove




#path for testing
FILE="/home/joshuamoore/Documents/Using-Pytest-Methods-and-Tools-22/tests/testing.txt"
FILE1="/home/joshuamoore/Documents/Using-Pytest-Methods-and-Tools-22/tests/testing1.txt"
FILE2="/home/joshuamoore/Documents/Using-Pytest-Methods-and-Tools-22/tests/testing2.txt"




#item list for getitems()
items = ["chair","sofa","stool"]



#testing openFile()

#should pass if testing.txt exists
def test_openFile():
    assert os.path.exists(FILE) == 1 #essentially stat file
    openFile(FILE)
    
def test_openFile1():
    assert os.path.exists(FILE1) == 1 #essentially stat file
    openFile(FILE)
#should fail if testing1.txt does not exist
#will pass if set equal to 0, due to it not existing. Could also just touch testing1.txt and will pass

#updated to create file then test if exists.
def test_openFile_nofile():
    if(os.path.exists(FILE1) == 0):
        f = open(FILE1, "x") #create the file, x returns an error if the file exists already
        assert os.path.exists(FILE1) ==1
        openFile(FILE1)





#should fail due to invalid type input
#will pass if a path to file, which is supplied in string format.


#updated to try converting to string

def test_openFile_invalidtype():
    if(os.path.exists(FILE2) == 0):
        f = open(FILE2, "x") #create the file, x returns an error if the file exists already
        assert os.path.exists(FILE2) ==1
        openFile(FILE2)








#testing numbers()
#should pass with supplied ints
def test_numbers():
    assert numbers(3,1)==3


def test_numbers1():
    assert numbers(30,10)==3

def test_numbers2():
    assert numbers(30,10)==3.0
#should fail due to division by zero
#will pass if second input is !0
def test_numbers_dividebyzero():
    assert numbers(3,0)==0
#should fail due to invalid type being input
#will pass if converted to ints first
def test_numbers_invalidtype():
    assert numbers("3","1")




#testing dist()



#manually testing function
#print(dist(2,2,1,1))

#should pass with supplied ints
def test_dist():
    assert dist(2,2,1,1)==2
#should not pass but does in this configuration. How many decimal places are considered?

#changed dist function to round up. The decimal places make it harder to compare (#this fails on purpose)
def test_dist_noteq():
    assert dist(2,2,1,1)==1
#explores equality with first decimal point. It fails

def test_dist_noteq1():
    assert dist(2,2,1,1)==1.5
#fails due to string input
#would pass if converted to ints before
def test_dist_invalidtype():
    assert dist("2","2","1","1")==2





#testing isPalindrome()
#should pass
def test_isPalindrome():
    assert isPalindrome("racecar")==True
#should pass
def test_isPalindrome():
    assert isPalindrome("mom")==True
#would fail if set to True
def test_isPalindrome_False():
    assert isPalindrome("test")==False
#will fail due to invalid type input to function
#will pass if converted to string that is also a palindrome
def test_isPalindrome_invalidtype():
    assert isPalindrome(1)==True





#input testing

#testing divide()
#practice in input testing using monkeypatch

#should pass
def test_divide(monkeypatch):
        monkeypatch.setattr('builtins.input',lambda _: next(GEN))
        assert divide() == 3.0

#will fail due to division by zero
#will pass if passing in GEN instead
def test_dividebyzero(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda _: next(GEN1))
    assert divide() == 1

#fails due to int being passed in through monkeypatch which expects a string
#will pass if correct type in list
def test_divide_invalidtype(monkeypatch):
        monkeypatch.setattr('builtins.input',lambda _: next(GEN2))
        assert divide() == 3.0





#testing sq
#should pass
def test_sq():
    assert sq(49)==7

def test_sq1():
    assert sq(49)==7.0
#should fail
#will work if set == 7
def test_sq_False():
    assert sq(49)==8
#should fail
#will work if 49 converted first
def test_sq_invalidtype():
    assert sq("49")==7



#testing greetUser
#should work
def test_greetUser(capsys):
    greetUser("joshua","jordan","moore")
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program joshua jordan moore\nGlad to have you!"
 
#typo should not work
#add u at back of sentence
def test_greetUser_typo(capsys):
    greetUser("joshua","jordan","moore")
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program joshua jordan moore\nGlad to have yo!"
#invalid type
def test_greetUser_invalidtype(capsys):
    greetUser(1,2,3)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program 1 2 3\nGlad to have you!"


def test_greetUser_invalidtype1(capsys):
    greetUser(1.0,2,3)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program 1.0 2 3\nGlad to have you!"

# #testing displayItem()
# ## takes in a Python list
# ## attempts to display the item at the index provided



#should work
def test_displayItem(capsys):
    displayItem(items, 2)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 2 index is stool"


#should not work. This is because the item at index number 2 is stool

def test_displayItem_fail(capsys):
    displayItem(items, 2)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 2 index is chair"


#should not work. This is to simulate out of bounds 

def test_displayItem_bounds(capsys):
    displayItem(items, 3)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 2 index is stool"