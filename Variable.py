# Auther: John Blue
# Time: 2023/2
# Object: listing common types or containers in Python


import numpy as np

def func():
    print("in function: scope = ", scope)
    # or redfine func's own scope
    #scope = 2

scope = 0

if __name__ == "__main__":
    #
    ## type
    #
    print(" type … ")
    
    #
    integer = 3
    string = "3"
    
    # list
    lst = [];# ! it is empty, not None
    lst = [0, 1, 2, 3, 4]
    del lst[0] # delete
    print("lst = ", lst)
    lst = [0, 1, 2, 3, 4]
    print("lst[1:3] = ", lst[1:3]) # slice
    lst = [[1,2,3]]
    print("lst + lst = ", lst + lst)
    Ori = [[1, 2, 3]]
    Exd = [[4, 5, 6]]
    Ori.extend(Exd) # extend
    print("Ori.extend(Exd) = ", Ori)
    Ori = [[1, 2, 3]]
    Exd = [4, 5, 6]
    Ori.append(Exd) # append
    print("Ori.append(Exd) = ", Ori)
    
    # tuple
    # assignment
    employee = ('Julia', 'Roberts', 1967, 'Taichung')
    (firstName, lastName, birthYear, cityLivingIn) = employee
    print("assignment through tuple: ", firstName, " ", lastName, "", birthyear, "", cityLivingIn)
    # swap
    a = 3
    b = 5
    print("a =", a,";b=",b)
    a, b = b, a
    print("(after tuple swap) a =", a, ";b=",b)
    #https://selflearningsuccess.com/python-tuple/
    
    # set
    # ...
    #https://docs.python.org/3/library/stdtypes.html#set
    
    # dictionary
    # ...
    #https://docs.python.org/zh-tw/3.6/tutorial/datastructures.html
    
    # enum
    # …
    #https://docs.python.org/3/library/enum.html
    
    # none
    # no is None : true (memory allocated in the same place)
    # no == None : true (the value is the same)
    no = None 
    
    # numpy
    np_ar = np.array([1, 2, 3, 4])
    retn = np_ar.reshape((2, 2)).tolist()
    print("retn = ", retn)
    #np.append(…)
    #
    #print(" … ")
    #

    #
    ## scope
    #
    print("begin scope = ", scope)
    scope = 1
    func()
    print("redefine scope = ", scope)
