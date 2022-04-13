import functions

#testing openFile()
def test_openFile():
    assert functions.openFile("testing.txt")

def test_openFile_nofile():
    assert functions.openFile("test.txt")==1

def test_openFile_invalidtype():
    assert functions.openFile(1)==1




#testing numbers()
def test_numbers():
    assert functions.numbers(3,1)==3

def test_numbers_dividebyzero():
    assert functions.numbers(3,0)==0

def test_numbers_invalidtype():
    assert functions.numbers("num1","num2")

#testing dist()
def test_dist():
    assert functions.dist(3.0,1.0)==2.0

def test_numbers_negative():
    assert functions.dist(-3.0,-1.0)==2.0

def test_numbers_invalidtype():
    assert functions.dist("num1","num2")


#testing isPalindrome()
def test_isPalindrome():
    assert functions.isPalindrome("racecar")==True

def test_isPalindrome_False():
    assert functions.isPalindrome("test")==False

def test_isPalindrome_invalidtype():
    assert functions.isPalindrome(1)==True