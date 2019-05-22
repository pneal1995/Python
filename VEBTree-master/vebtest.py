from VEB import VEB
from pyveb import VEB2
import random
import math
import time

def test_correctness():
    n = 50000
    veb = VEB(n)
    # print "Creating VEB Tree for %d elements..." % n
    
    # print "Testing..."
    
    # print "Generating random numbers to sample..."
    # create random numbers
    numbers = set()
    for i in range(n): 
        number = random.randint(0, veb.u-1)
        numbers.add(number)
    
    # other numbers
    other_numbers = set()
    for i in range(n):
        other_numbers.add(random.randint(0, veb.u-1))
    
    # print "Adding numbers to VEB Tree..."
    # add all to set
    for num in list(numbers):
        veb.insert(num)
    
    # print("Testing for membership of numbers...")
    # test for membership
    other_numbers = other_numbers - numbers
    error = 0
    for num in list(other_numbers):
        if veb.member(num):
            error += 1
    for num in list(numbers):
        if not veb.member(num):
            error += 1
    # print "Error Number For Membership was %d" % error

    # print "Testing for successor..."
    # test for successor
    listofnums = list(numbers)
    listofnums.sort()
    error = 0
    for index in range(len(listofnums) - 1):
        if veb.successor(listofnums[index]) != listofnums[index+1]:
            error += 1
    # print "Error Number For successor was %d" % error

    # print "Testing for predecessor..."
    # test for predecessor
    error = 0
    for index in range(1, len(listofnums)):
        if veb.predecessor(listofnums[index]) != listofnums[index-1]:
            error += 1
    # print "Error Number for predecessor was %d" % error
    
def test_speed():
    
    n = 50000
    veb = VEB(n)

    # print "Creating VEB Tree for %d elements..." % n

    # create random numbers
    numbers = set()
    for i in range(n): 
        number = random.randint(0, veb.u-1)
        numbers.add(number)
    
    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.insert(number)
    total_time = (time.time() - starttime)
            
    ns = float(len(numbers))
    total_time = float(total_time)

    # print "Speed per insertion: %f seconds" % (total_time / ns)

    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.member(number)
    total_time = (time.time() - starttime)   

    # print "Speed per membership query: %f seconds" % (total_time / ns) 

    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.predecessor(number)
    total_time = (time.time() - starttime)

    # print "Speed per predecessor query: %f seconds" % (total_time / ns)

    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.successor(number)
    total_time = (time.time() - starttime)
    
    # print "Speed per successor query: %f seconds" % (total_time / ns)

test_correctness()
test_speed()