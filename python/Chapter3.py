"""

Alexander Seeto
Unofficial Python Solutions
http://www.alexseeto.com

Cracking The Coding Interview
by Gayle Laakmann McDowell
Link: http://amzn.to/1biovdS

# +--------------------------------------------------------------------------+
# |                       CHAPTER 3: STACKS AND QUEUES                       |
# +--------------------------------------------------------------------------+

"""

"""

3.1 Describe how you could use a single array to implement three stacks

"""

# Single array implementing three stacks
class SingleArrayStacks(object):
    def __init__(self, stacksize=100, number=3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    # Adds given value to given Stack Number
    def push(self, stackNum, value):
        # Return error message if Stack size is exceeded
        if self.pointer[stackNum] + 1 >= self.stacksize:
            print "Out of space"
        else:
            # Increment Stack pointer for given Stack number by 1
            self.pointer[stackNum] += 1
            # Set top of Stack as given value
            self.array[self.absTopOfStack(stackNum)] = value

    # Removes top Node from Stack and returns its data
    def pop(self, stackNum):
        # Return error message if Stack size is empty
        if self.isEmpty(stackNum):
            print "Trying to pop an empty stack."
        else:
            # Otherwise, initialize variable to store top of Stack value
            value = self.array[self.absTopOfStack(stackNum)]
            # Set top of Stack value as None
            self.array[self.absTopOfStack(stackNum)] = None
            # Decrement Stack pointer for given Stack number by 1
            self.pointer[stackNum] -= 1
            # Return stored Stack value
            return value

    # Returns data of top Node in Stack
    def peek(self, stackNum):
        return self.array[self.absTopOfStack(stackNum)]

    # Checks if Stack is empty
    def isEmpty(self, stackNum):
        return self.pointer[stackNum] < 0

    # Returns index of top of given stack
    def absTopOfStack(self, stackNum):
        return stackNum * self.stacksize + self.pointer[stackNum]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# array = SingleArrayStacks()
# array.push(1, 1)
# array.push(1, 2)
# print array.pop(0)  # Trying to pop an empty stack.
# print array.peek(1) # 2
# array.push(0, 1)
# array.push(0, 2)
# print array.pop(0)  # 2
# print array.peek(0) # 1

"""

3.2 How would you design a stack which, in addition to push and pop, also has 
    a function min which returns the minimum element? Push, pop and min should 
    all operate in 0(1) time.

"""

class StackWithMin:
    
    def __init__(self):
        self.stack = []
        # Initialize a min variable as part of class to store min values
        self.min = []
        # Initialize a variable to track size of list of min values
        self.minSize = 0
        
    def push(self, value):
        # Append the value to our Stack
        self.stack.append(value)
        # If there are no mins or the given value is less than last min
        if self.minSize == 0 or value <= self.min[-1]:
            # Append the new min
            self.min.append(value)
            # Increase our variable for min size
            self.minSize += 1

    def pop(self):
        # If there are no mins, return None
        if self.minSize == 0:
            return None
        # Otherwise, initialize variable to store data from top of Stack
        data = self.stack.pop()
        # If the data is the last min
        if data == self.min[-1]:
            # Remove the last added element from the min Stack
            self.min.pop()
            # Reduce the min Stack size by 1
            self.minSize -= 1
        # Return the data from top of Stack
        return data

    def getMin(self):
        # If there are no mins, return None
        if self.minSize == 0:
            return None
        # Otherwise, get the last added element from the min Stack
        return self.min[-1]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# from random import randrange
# Stack = StackWithMin()
# for i in range(15):
#     data = randrange(1,100)
#     Stack.push(data)
#     print data,
# print ""
# for i in range(15):
#     print "Popped", Stack.pop(), " New min", Stack.getMin()

"""

3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might 
    topple. Therefore, in real life, we would likely start a new stack when 
    the previous stack exceeds some threshold. Implement a data structure 
    SetOfStacks that mimics this. SetOfStacks should be composed of several 
    stacks and should create a new stack once the previous one exceeds capacity. 
    SetOfStacks.push() and SetOfStacks.pop() should behave identically to a 
    single stack (that is, pop() should return the same values as it would if 
    there were just a single stack).
    
    FOLLOW UP

    Implement a function popAt(int index) which performs a pop operation on a 
    specific sub-stack.

"""

class SetOfStacks:
    
    def __init__(self):
        # An array of arrays to represent our stacks
        self.stacks = []
        # Capacity for one stack of plates
        self.capacity = 3
        
    def push(self, value):
        # If there are no Stacks or the last Stack is at capacity
        if len(self.stacks) is 0 or len(self.stacks[-1]) is self.capacity:
            # Append a new stack
            self.stacks.append([])
            # Append a new value to our new Stack
            self.stacks[-1].append(value)
        else:
            # Otherwise append new value to last Stack
            self.stacks[-1].append(value)

    def pop(self):
        # If there are no Stacks
        if len(self.stacks) is 0:
        # Return None
            print "... Can't pop, no Stacks!"
            return
        # Pop the last value from the last stack
        data = self.stacks[-1].pop()
        # If the last Stack is now 0
        if len(self.stacks[-1]) is 0:
            # Remove the last stack
            self.stacks.pop()
        # Return the data from top of last Stack
        return data

    def popAt(self, stackNum):
        # If there are no Stacks
        if len(self.stacks) is 0 or len(self.stacks) < stackNum:
        # Return None
            print "... Can't pop, there isn't a Stack there!"
            return
        # Pop the top value from the given stackNum-1 to account for 0 index
        data = self.stacks[stackNum-1].pop()
        # If the given stack is now 0
        if len(self.stacks[stackNum-1]) is 0:
            # Remove it
            self.stacks.pop(stackNum-1)
        # If there is no stack above this stack
        elif stackNum > len(self.stacks)-1:
            # Return our data and that's it!
            return data
        else:
            # Otherwise, we need to shift our plates accordingly
            self.shiftPlates(stackNum)
        # Return the data from top of requested stack
        return data

    def shiftPlates(self, stackNum):
        # Number of Stacks above this stack are the size - current stack
        stacksAbove = len(self.stacks) - stackNum
        # # While there is a stack above our stack and the next stack's not empty
        # while stacksAbove > 0:
        if len(self.stacks[stackNum]) is not 0:
            # Make the bottom of the next Stack, the top of the previous stack
            bottom = self.stacks[stackNum][0]
            self.stacks[stackNum-1].append(bottom)
            self.stacks[stackNum].pop(0)
            # If the stack above is empty now
            if len(self.stacks[stackNum]) is 0:
                # Remove it
                self.stacks.pop(stackNum)

    def displayStacks(self):
        for stack in self.stacks:
            print ""
            for i in stack:
                print i,

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# from random import randrange
# Stacks = SetOfStacks()

# ------------------------ Testing push() and pop() ------------------------

# for i in range(15):
#     data = randrange(1,100)
#     Stacks.push(data)
#     print data,
# print ""
# Stacks.displayStacks()
# print ""
# for i in range(16):
#     print "Popped", Stacks.pop()

# -------------------- Testing popAt() and shiftPlates() --------------------

# print ""
# for i in range(15):
#     data = randrange(1,100)
#     Stacks.push(data)
#     print data,
# print ""
# Stacks.displayStacks()
# print ""
# for i in range(16):
#     print "Popped", Stacks.popAt(1)

"""

3.4 In the classic problem of the Towers of Hanoi, you have 3 towers and 
    N disks of different sizes which can slide onto any tower. The puzzle 
    starts with disks sorted in ascending order of size from top to bottom 
    (i.e., each disk sits on top of an even larger one). You have the 
    following constraints:

    (T) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto the next rod.
    (3) A disk can only be placed on top of a larger disk.

    Write a program to move the disks from the first tower to the last 
    using Stacks.

"""
# +-------------------------------------------------------------------------+
# |                             Towers of Hanoi                             |
# +-------------------------------------------------------------------------+
# |            _                       _                    _               |
# |           | |                     | |                  | |              |
# |           | |                     | |                  | |              |
# |          _|_|_                    | |                  | |              |
# |        _|_____|_                  | |                  | |              |
# |      _|_________|_                | |                  | |              |
# |_____|_____________|_______________|_|__________________|_|______________|
# +-------------------------------------------------------------------------+

class Tower:
    def __init__(self, index):
        # Number of Tower
        self.index = index
        # An array of ints represents disk sizes
        self.stack = []

    # Returns Tower Number
    def getIndex(self):
        return self.index

    # Appends disk to top of Stack
    def push(self, size):
        # Make sure disk's size is not greater than top of stack
        if self.isEmpty() or size <= self.peek():
            # If it isn't, append that disk!
            self.stack.append(size)

    # Removes top disk from Stack and returns its data
    def pop(self):
        # Make sure that stack isn't empty
        if not self.isEmpty():
            # If it's not, then grab that disk!
            disk = self.stack.pop()
            # Return it!
            return data
        # Otherwise print error message
        print "There aren't any disks in this stack! "
        return

    # Returns data of top Node in Stack
    def peek(self):
        # Make sure that stack isn't empty
        if not self.isEmpty():
            # If it's not, then return the size of the disk on top!
            return self.stack[len(self.stack)-1]
        print "There aren't any disks in this stack! "
        return

    # Returns True if Stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Move top of this stack to the given stack
    def moveTopTo(self, tower):
        # Pop top of this stack    
        disk = self.stack.pop()
        # Move it to the given stack
        tower.push(disk)
        # Print what's happening
        print "Moved disk with size " + str(disk) + " from Tower " +\
              str(self.getIndex()) + " to Tower " + str(tower.getIndex())

    # Move disks
    def moveDisks(self, n, destination, pitstop):
        if n>0:
            # Move top n-1 disks from origin to buffer
            # We make the destination our buffer in this case
            self.moveDisks(n-1, pitstop, destination)
            # Move top disk from origin to destination
            self.moveTopTo(destination)
            # Move top n-1 disks from buffer to destination
            # The origin in this case is the buffer
            pitstop.moveDisks(n-1, destination, self)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# DISKS  = 3
# TOWERS = 3
# Towers = []

# # Initalize Towers
# for i in range(TOWERS):
#     Towers.append(Tower(i+1))
#     print i+1

# # Initialize Disks on Tower 1
# for i in range(1,DISKS+1)[::-1]:
#     Towers[0].push(i)

# # Display Towers and Disks bottom to top (left to right)
# def displayTowers(arrayOfTowers):
#     for index, tower in enumerate(arrayOfTowers):
#         print "Tower "+str(index+1)+": ",
#         print tower.stack,
#         print ""

# # Before
# displayTowers(Towers);
# # Move
# Towers[0].moveDisks(DISKS, Towers[2], Towers[1])
# # After
# displayTowers(Towers);

"""

3.5 Implement a MyQueue class which implements a queue using two stacks.

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

class Stack(object):
    def __init__(self, top=None):
        self.top = top

    # Creates a new Node and adds it top of Stack
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # Removes top Node from Stack and returns its data
    def pop(self):
        if self.top is not None:
            data = self.top.getData()
            self.top = self.top.getNext()
            return data
        return None

    # Returns data of top Node in Stack
    def peek(self):
        if self.top is not None:
            return self.top.data
        return "Empty stack! Sorry :("

    # Returns True if Stack is empty
    def isEmpty(self):
        return self.top is None

# A Queue represented by two Stacks
class MyQueue(object):
    def __init__(self):
        self.new = Stack()
        self.old = Stack()

    # Add the newest piece of data
    def add(self, val):
        # Pushes the data to the top of the new stack
        self.new.push(val)

    # Ensure new has the newest data on top and old has the oldest data on top
    def shiftStacks(self):
        # The stack must be empty because we don't want older data still here
        # Before we start adding the new data
        if self.old.isEmpty():
            # We are adding the new data, but by pushing each data onto the
            # top of the stack, we add the new stack in reverse. This makes
            # our old stack have the oldest data at the top
            while not self.new.isEmpty():
                self.old.push(self.new.pop())

    # Take a peek at the oldest data in the queue
    def peek(self):
        # Ensure all data has been shifted accordingly
        self.shiftStacks()
        return self.old.peek()

    # Remove the oldest piece of data
    def remove(self):
        # Ensure all data has been shifted accordingly
        self.shiftStacks()
        return self.old.pop()

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# STACK = Stack()
# print STACK.peek()
# STACK.push(1)
# print STACK.peek()
# print STACK.pop()

# NODES = 3
# QUEUE = MyQueue()

# # Initialize Nodes in Queue
# for i in range(1,NODES+1):
#     QUEUE.add(i)

# print QUEUE.peek()
# print QUEUE.remove()
# print QUEUE.remove()
# QUEUE.add(10)
# print QUEUE.remove()
# print QUEUE.remove()

"""

3.6 Write a program to sort a stack in ascending order (with biggest items on 
    top). You may use at most one additional stack to hold items, but you may 
not copy the elements into any other data structure (such as an array). The 
stack supports the following operations: push, pop, peek, and isEmpty.

"""

# A Plate
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

# A Stack O' Plates
class Stack(object):
    def __init__(self, top=None):
        self.top = top

    # Creates a new Node and adds it top of Stack
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # Removes top Node from Stack and returns its data
    def pop(self):
        if self.top is not None:
            data = self.top.getData()
            self.top = self.top.getNext()
            return data
        return None

    # Returns data of top Node in Stack
    def peek(self):
        if self.top is not None:
            return self.top.data
        return None

    # Returns True if Stack is empty
    def isEmpty(self):
        return self.top is None

# Sort a Stack o' Plates in ascending order
def sortStack(stack):
    # platesholder ... get it? PLACEHOLDER ha..
    platesholder = Stack()
    # While the given stack still has its unsorted plates
    while stack.top is not None:
        # Hold its top plate so we can figure out where to put it
        plate = stack.pop()
        print "Picked up plate #"+ str(plate) + ".\n"
        # Look through plates in our platesholder until you see where it fits
        while platesholder.peek() > plate:
            top = platesholder.peek()
            # If it doesn't fit on top, move plates over to platesholder
            stack.push(platesholder.pop())
            print "Moved plate #"+ str(top) + " to top of Stack.\n"
        else:
            # Once you find the plate it's bigger than, add the plate!
            platesholder.push(plate)
            print "Placed plate #"+ str(plate) + " at top of platesholder.\n"
    # By now, the given stack is all gone, and it's sorted in platesholder!
    return platesholder

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# NODES = 3
# STACK = Stack()

# # Initialize Nodes in Stack
# for i in range(1,NODES+1):
#     STACK.push(i)

# # Returns the STACK, but sorted in ascending order
# sortStack(STACK)


"""

3.7 An animal shelter holds only dogs and cats, and operates on a strictly 
    "first in, first out" basis. People must adopt either the "oldest" (based 
    on arrival time) of all animals at the shelter, or they can select whether 
    they would prefer a dog or a cat (and will receive the oldest animal of 
    that type). They cannot select which specific animal they would like. 
    Create the data structures to maintain this system and implement operations 
    such as enqueue, dequeueAny, dequeueDog and dequeueCat.You may use the 
    built-in LinkedList data structure.

"""

# An Animal
class Animal(object):
    def __init__(self, name, data, next=None):
        self.name = name
        # Data will represent the type of Animal
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getName(self):
        return self.name

    def getNext(self):
        return self.next

# Stack represents animals waiting in line at the shelter to be adopted 
# (in a surprisingly orderly manner)
class Stack(object):
    def __init__(self, top=None):
        self.top = top

    # Creates a new Node and adds it top of Stack
    def push(self, name, data):
        node = Animal(name, data)
        node.next = self.top
        self.top = node

    # Removes top Node from Stack and returns it
    def pop(self):
        if self.top is not None:
            node = self.top
            self.top = self.top.getNext()
            return node
        return None

    # Returns data of top Node in Stack
    def peek(self):
        if self.top is not None:
            return self.top.data
        return None

    # Returns True if Stack is empty
    def isEmpty(self):
        return self.top is None

    # Return the stack reversed
    def reverseStack(self):
        # Initialize our empty reversed stack
        reverse = Stack()
        # Store current animal
        this = self.top
        # Reverse the stack by adding each animal to the top of reverse
        while this is not None:
            reverse.push(this.getName(), this.getData())
            this = this.getNext()
        # Return our reversed stack
        return reverse

# The line of animals at the shelter
class AnimalQueue(object):
    def __init__(self):
        self.animals = Stack()

    # A new animal joins the line at the shelter :'(
    def enqueue(self, name, data):
        self.animals.push(name, data)

    # Someone adopted the shelter's oldest animal!
    def dequeueAny(self):
        # Reverse the queue
        queueReversed = self.animals.reverseStack()
        # Find our oldest animal
        animal = queueReversed.pop()
        # Update our real list
        self.animals = queueReversed.reverseStack()
        # Give our oldest animal to the adopter
        return animal

    # Someone adopted the shelter's oldest dog!
    def dequeueDog(self):
        # Reverse the queue
        queueReversed = self.animals.reverseStack()
        # Find oldest animal that's a dog
        dog = self.getElder('dog', queueReversed)
        # Give our oldest dog to the adopter
        return dog

    # Someone adopted the shelter's oldest cat!
    def dequeueCat(self):
        # Reverse the queue
        queueReversed = self.animals.reverseStack()
        # Find oldest animal that's a cat
        cat = self.getElder('cat', queueReversed)
        # Give our oldest cat to the adopter
        return cat

    # Returns the oldest animal in our line with the given type if specified
    def getElder(self, data, queueReversed):
        # Initialize variable to store animal we're looking at
        animal = queueReversed.top
        # Store the previous animal
        prev = None
        # Search through our line of animals
        while animal is not None:
            # Check current animal against requested type
            if animal.getData() is data:
                # Remove the animal from the top of list if prev is None
                if not prev:
                    animal = queueReversed.pop()
                else:
                    # Otherwise, remove animal from stack by skipping over it
                    prev.next = animal.next
                # Update our animals line
                self.animals = queueReversed.reverseStack()
                # If so, then return it!
                return animal
            # Update prev
            prev = animal
            # Otherwise, continue searching through our line
            animal = animal.getNext()
        # If there are no animals left to search through, return None
        return None

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# Shelter = AnimalQueue()
# print Shelter.dequeueAny()             # None
# print Shelter.dequeueDog()             # None
# print Shelter.dequeueCat()             # None
# Shelter.enqueue('Gaara','dog')
# Shelter.enqueue('Naruto','other')      # Not removed ever
# Shelter.enqueue('Sasuske','dog')
# Shelter.enqueue('Kakashi','dog')
# Shelter.enqueue('Shikamaru','dog')
# Shelter.enqueue('Kiba','dog')
# Shelter.enqueue('Lee','dog')
# Shelter.enqueue('Neji','dog')
# Shelter.enqueue('Sakura','cat')
# print Shelter.dequeueAny().getName()   # Gaara
# print Shelter.dequeueDog().getName()   # Sasuske
# print Shelter.dequeueDog().getName()   # Kakashi
# print Shelter.dequeueDog().getName()   # Shikamaru
# print Shelter.dequeueDog().getName()   # Kiba
# print Shelter.dequeueDog().getName()   # Lee
# print Shelter.dequeueCat().getName()   # Sakura
# print Shelter.dequeueDog().getName()   # Neji