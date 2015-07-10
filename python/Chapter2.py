"""

Alexander Seeto
Unofficial Python Solutions
http://www.alexseeto.com

Cracking The Coding Interview
by Gayle Laakmann McDowell
Link: http://amzn.to/1biovdS

# +--------------------------------------------------------------------------+
# |                        CHAPTER 2: LINKED LISTS                           |
# +--------------------------------------------------------------------------+

"""

# Class representing Node in a Singly Linked List with basic functionality
#   - self.data is the current Node's data (defaults to None)
#   - self.next is the next Node in the list (defaults to None)
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Returns data of Node
    def getData(self):
        return self.data

    # Sets data of Node
    def setData(self, data):
        self.data = data

    # Prints data of Node
    def printNode(self):
        print self.data

    # Returns next of Node
    def getNext(self):
        return self.next

    # Sets next of Node
    def setNext(self, next):
        self.next = next

# Class representing Singly Linked List with basic functionality
#   - self.data is the current Node's data
#   - self.next is the next Node in the list or None
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Returns size of list
    def size(self):
        # Initialize counter for size
        size = 0
        # Initialize variable to store current Node
        this = self.head
        # Loop through each Node in list that is not None
        while this is not None:
            # Each Node adds 1 to count of total Nodes
            size += 1
            # Set current Node to the next Node in list
            this = this.getNext()
        # Return size
        return size

    # Returns the first Node found with given data
    def find(self, data):
        # Initialize variable to store current Node
        this = self.head
        # Loop through each Node in list that is not None
        while this is not None:
            # If Node's data matches given data
            if this.getData() == data:
                # Eureka! Return this Node!
                return this
            # Otherwise, set current Node to the next Node in list
            this = this.getNext()
        # Return size
        else:
            # If loop completes then Node is not in list
            print "Node not found in linked list"

    # Adds a Node with given data to the front of list
    def insertNode(self, data):
        # Initialize variable to store current Node
        this = self.head
        # Initialize new Node to be added
        node = Node(data)
        # Set the next value of our new Node (node) to the current head
        node.setNext(this)
        # Make this new Node our linked list's head!
        self.head = node

    # Delete the first Node found with given data
    def deleteNode(self, data):
        # Initialize variable to store current Node
        this = self.head
        # Initialize variable to store previous Node
        prev = None
        # Initialize variable to symbolize whether Node has been found
        found = False
        # Loop through each Node in list that is not None
        while this and found is False:
            # If Node's data matches given data
            if this.getData() == data:
                # Eureka! You found it.
                found = True
            else:
                # Save this Node as previous
                prev = this
                # You didn't find the data in this Node, so check the next one!
                this = this.getNext()
        # You didn't find data in any of the nodes
        if this is None:
            print "Node with given data not found in linked list."
        # If previous Node is None then you found data in the head
        # So just change head to next node, effectively removing this Node
        if prev is None:
            self.head = this.getNext()
        # You found it somewhere other than the head!
        else:
            # Set the previous Node's next to this Node's Next to skip it,
            # By skipping it, you're effectively removing this Node
            prev.setNext(this.getNext())

    # Used for testing, print all Node data
    def printList(self):
        # Initialize variable to store current Node
        this = self.head
        # Loop through each Node in list that is not None
        while this is not None:
            this.printNode()
            this = this.getNext()

"""

2.1 Write code to remove duplicates from an unsorted linked list.
    
    FOLLOW UP
    
    How would you solve this problem if a temporary buffer is not allowed?

"""

# Remove duplicates from given unsorted linked list
def removeDupes(linkedlist):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initiaize array of unique data values
    unique_data = set()
    # Initialize result list
    result_list = LinkedList()
    # Loop through each Node in list that is not None
    while this is not None:
        # Add each Node's data
        # NOTE: Sets will automatically remove duplicates
        unique_data.add(this.getData())
        # Continue onward! ...to the next Node
        this = this.getNext()
    # Convert set to a list
    unique_data = list(unique_data)
    # Create new nodes for each piece of unique data
    for data in unique_data:
        # Insert them into our linked list to return
        result_list.insertNode(data)
    # Return our new and adjusted linked list
    return result_list

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(3,n0)
n2 = Node(1,n1)
n3 = Node(6,n2)
n4 = Node(1,n3)

dupe_pos_0 = LinkedList(n4)
dupe_pos_1 = LinkedList(n0)
dupe_pos_2 = LinkedList()

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print dupe_pos_0.size()              # 5
# print removeDupes(dupe_pos_0).size() # 3
# print removeDupes(dupe_pos_1).size() # 1
# print removeDupes(dupe_pos_2).size() # 0

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""
    
# Remove duplicates from given unsorted linked list
def removeDupes_ALTERNATE(linkedlist):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initialize variable to store Node data
    data = []
    # Loop through each Node in list that is not None
    while this is not None:
        d = this.getData()
        # If data already exists in data
        if d in data:
            linkedlist.deleteNode(d)
        else:
            # Add it to the list
            data.append(d)
        # Continue onward! ...to the next Node
        this = this.getNext()
    # Return our adjusted linked list
    return linkedlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(3,n0)
n2 = Node(1,n1)
n3 = Node(6,n2)
n4 = Node(1,n3)

dupe_pos_0 = LinkedList(n4)
dupe_pos_1 = LinkedList(n0)
dupe_pos_2 = LinkedList()

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print dupe_pos_0.size()                        # 5
# print removeDupes_ALTERNATE(dupe_pos_0).size() # 1
# print removeDupes_ALTERNATE(dupe_pos_1).size() # 1
# print removeDupes_ALTERNATE(dupe_pos_2).size() # 0

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Remove duplicates from given unsorted linked list
# You're not allowed to store the data somewhere! (no buffer)
def removeDupes_NOBUFFER(linkedlist):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Loop through each Node in list that is not None
    while this is not None:
        # Initialize variable to store current Node's data
        dat = this.getData()
        # Initialize our runner! He's going to try and find dat.
        run = this
        # Loop through the remaining Nodes in list that are not None
        while not run.getNext() == None:
            # If the runner finds dat, then he adjusts the previous Node's
            # next value to skip over the Node (thereby removing it)
            if dat == run.getNext().getData():
                # Set the current Node's next to equal the NEXT NEXT node
                # instead of just the next one, because then you skip it!
                run.next = run.next.getNext()
            else:
                # The runner didn't find dat in this node!
                # Let's continue to check the others.
                run = run.getNext()
        # We removed any dupes for the first Node's data
        # Continue onward! ...Let's continue, but using the next Node's data
        this = this.getNext()
    # Return our adjusted linked list
    return linkedlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(3,n0)
n2 = Node(1,n1)
n3 = Node(6,n2)
n4 = Node(1,n3)

dupe_pos_0 = LinkedList(n4)
dupe_pos_1 = LinkedList(n0)
dupe_pos_2 = LinkedList()

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print dupe_pos_0.size()                       # 5
# print removeDupes_NOBUFFER(dupe_pos_0).size() # 1
# print removeDupes_NOBUFFER(dupe_pos_1).size() # 1
# print removeDupes_NOBUFFER(dupe_pos_2).size() # 0

"""

2.2 Implement an algorithm to find the kth to last element of a singly linked 
    list.

"""

# Find the kth to last element of a singly linked list
#   - This is equivalent to reversing the list
#   - Then traversing until k is reached
#   - Then returning the Node at k

# Reverse the given linked list
def reverseList(linkedlist):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initialize variable to store reversed linked list
    newList = LinkedList()
    # Loop through the remaining Nodes in list that are not None
    while this is not None:
        # Insert a new Node into our new list
        # With data from the current Node from our given list
        # insertNode() also sets the next value of the inserted Node
        newList.insertNode(this.getData())
        # Continue to link the next Node in our given linkedlist!
        this = this.getNext()
    # The list has been successfully reversed, return it!
    return newList

# Find the kth to last element of a singly linked list
def findKToLast(k, linkedlist):
    # Initialize variable to store list size
    size = linkedlist.size()
    # Cannot find reverse kth element if there aren't enough elements
    if not size-1 >= k:
        print "The given list does not contain enough Nodes."
    # Initialize variable to store reversed linked list
    reverse = reverseList(linkedlist)
    # Initialize variable to store current Node from reversed linked list
    this = reverse.head
    # Initialize variable to tell us when we've reached given 'k'
    index = 0
    # Loop through the remaining Nodes in list that are not None
    while this is not None and not index == k:
        index+=1
        # Move to the next Node since we haven't reached 'k' yet!
        this = this.getNext()
    # Return data for the Node that we were on when the loop condition failed
    return this.getData()

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(5,None)
n1 = Node(4,n0)
n2 = Node(3,n1)
n3 = Node(2,n2)
n4 = Node(1,n3)

linkedlist = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# linkedlist.printList()
# reverseList(linkedlist).printList()
# print findKToLast(2, linkedlist) == n2.getData() # true

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Find the kth to last element of a singly linked list
def findKToLast_ALTERNATE(k, linkedlist):
    # Initialize variable to store list size
    size = linkedlist.size()
    # Cannot find kth element if there aren't enough elements
    if not size-1 >= k:
        print "The given list does not contain enough Nodes."
    # Initialize variable to store forward traversal destination
    # Moving backwards by k in the list is the same as
    # Moving forwards by size - k - 1
    forward = size - k - 1
    # Initialize variable to store current Node from reversed linked list
    this = linkedlist.head
    # Initialize variable to tell us when we've reached given 'k'
    index = 0
    # Loop through the remaining Nodes in list that are not None
    while this is not None and index is not forward:
        index+=1
        # Move to the next Node since we haven't reached 'k' yet!
        this = this.getNext()
    # Return data for the Node that we were on when the loop condition failed
    return this.getData()

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(5,None)
n1 = Node(4,n0)
n2 = Node(3,n1)
n3 = Node(2,n2)
n4 = Node(1,n3)

linkedlist = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print findKToLast_ALTERNATE(2, linkedlist) == n2.getData() # true

"""

2.3 Implement an algorithm to delete a node in the middle of a singly linked 
    list, given only access to that node.

"""

# Delete node in the middle of a singly linked list, given only that node
def deleteMe(node):
    # Return False if Node is last Node in LinkedList or empty
    if node.getData() == None or node.getNext() == None:
        return False
    # Otherwise set data and next values
    next = node.getNext()
    # This Node's data should become the next Node's data
    node.data = next.data
    # This Node's next should become the next Node's next
    node.next = next.next
    # Return True
    return True

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n  = Node()
n0 = Node(5,None)
n1 = Node(4,n0)
n2 = Node(3,n1)
n3 = Node(2,n2)
n4 = Node(1,n3)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print deleteMe(n)
# print deleteMe(n0)
# print deleteMe(n1)
# print deleteMe(n2)
# print deleteMe(n3)
# print deleteMe(n4)

"""

2.4 Write code to partition a linked list around a value x, such that all nodes 
    less than x come before all nodes greater than or equal to x.

"""

# Partition the given linked list so values < x precede those >= to x
#   - Let's create a new list to be returned
#   - Run through the given linked list appending values >= to x
#   - Then do a second run and add values < x

# Partition the given linked list so values < x precede those >= to x
def sortAroundX(linkedlist, x):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initialize variable to store resulting linked list
    resultlist = LinkedList()
    # Loop through each Node in list that is not None
    while this is not None:
        # Compare each Node's data with x
        if this.getData() >= x:
            # Add the Nodes with data >= x to our list
            resultlist.insertNode(this.getData())
        # Continue to the next Node!
        this = this.getNext()
    # Reset this to head of list
    this = linkedlist.head
    # Loop through each Node in list that is not None
    while this is not None:
        # Compare each Node's data with x
        if this.getData() < x:
            # Add the Nodes with data < x to our list now to precede those >=
            resultlist.insertNode(this.getData())
        # Continue to the next Node!
        this = this.getNext()
    # Return the resulting list!
    return resultlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

x = 3
n0 = Node(1,None)
n1 = Node(1,n0)
n2 = Node(1,n1)
n3 = Node(5,n2)
n4 = Node(5,n3)

noneLinked = LinkedList()
singleNode = LinkedList(n0)
linkedList = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# noneLinked.printList()
# sortAroundX(noneLinked, x).printList()
# singleNode.printList()
# sortAroundX(singleNode, x).printList()
# linkedList.printList()
# sortAroundX(linkedList, x).printList()

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Partition the given linked list so values < x precede those >= to x
def sortAroundX_BETTER(linkedlist, x):
    # Check linkedlist is not empty
    if not linkedlist.size() > 1:
        return linkedlist
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initialize variable to store linked list of Nodes with values < x
    lessThanX = LinkedList()
    # Track number of elements being added to lessThanX
    lessThanX_count = 0
    # Initialize variable to store resulting linked list
    resultlist = LinkedList()
    # Track number of elements being added to lessThanX
    resultlist_count = 0
    # Loop through each Node in list that is not None
    while this is not None:
        # Compare each Node's data with x
        if this.getData() >= x:
            # Add the Nodes with data >= x to our result list
            resultlist.insertNode(this.getData())
            resultlist_count += 1
        else:
            # Add the Nodes with data < x to lessThanX
            lessThanX.insertNode(this.getData())
            lessThanX_count += 1
        # Continue to the next Node!
        this = this.getNext()
    # Check and see if any Nodes were even >= to x
    # Because if not, then we can just return our lessThanX Node list
    if resultlist_count == 0:
        return lessThanX
    # Check and see if any Nodes were even < x
    # Because if not, then we can just return our resultlist now
    if lessThanX_count == 0:
        return resultlist
    else:
        # Otherwise, set "this" to the head of lessThanX Node list
        # As always, "this" is used to help us track our current Node
        this = lessThanX.head
        # Loop through each Node in list that is not None
        while this is not None:
            # Compare each Node's data with x
            if this.getData() < x:
                # Merge the lessThanX into the front of our resultlist
                # For larger linked lists, this merging technique saves time
                resultlist.insertNode(this.getData())
            # Continue to the next Node!
            this = this.getNext()
        # Return the resulting list!
        return resultlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

x = 3
n0 = Node(1,None)
n1 = Node(1,n0)
n2 = Node(1,n1)
n3 = Node(5,n2)
n4 = Node(5,n3)

noneLinked = LinkedList()
singleNode = LinkedList(n0)
linkedList = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# noneLinked.printList()
# sortAroundX_BETTER(noneLinked, x).printList()
# singleNode.printList()
# sortAroundX_BETTER(singleNode, x).printList()
# linkedList.printList()
# sortAroundX_BETTER(linkedList, x).printList()

"""

2.5 You have two numbers represented by a linked list, where each node contains 
    a single digit. The digits are stored in reverse order, such that the 1's 
    digit is at the head of the list. Write a function that adds the two 
    numbers and returns the sum as a linked list.

    FOLLOW UP

    Suppose the digits are stored in forward order. Repeat the above problem.

"""

# Convert Linked List to Number
def getListNum(linkedlist):
    # Initialize variable to store list size
    size = linkedlist.size()
    # Initialize variable to store list num
    number = 0
    # If list has no elements, then its num is 0
    if size == 0: number = 0
    # If list has 1 element then it's 1 digit, and its num is its data value
    elif size == 1: number = linkedlist.head.getData()
    # Otherwise, we need to loop through and form the number from the digits
    else:
        # Initialize variable to store current Node
        this = linkedlist.head
        # Initialize variable to store String form of our list's number
        snum = ''
        # Loop through list for every Node that is not None
        while this is not None:
            # Append each digit in front since head is one's place digit
            snum = str(this.getData()) + snum
            # Continue to the next Node to get the next digit
            this = this.getNext()
        # Convert our String to an int and set it as the list's number
        number = int(snum)
    # Return the final number!
    return number

# Return linked list representing total of two "Digit" Linked Lists
def addDigitLists(list1, list2):
    # Initialize variable to store resulting list
    resultlist = LinkedList()
    # Store total of linked lists as String
    total = str(getListNum(list1) + getListNum(list2))
    # Create a new Node for each digit in total with head beings 1's digit
    for c in total:
        resultlist.insertNode(c)
    # Return our result list
    return resultlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(2,n0)
n2 = Node(3,n1)
n3 = Node(4,n2)
n4 = Node(5,n3)

noneLinked = LinkedList()
singleNode = LinkedList(n0)
linkedList = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print getListNum(noneLinked)                      # 0
# print getListNum(singleNode)                      # 1
# print getListNum(linkedList)                      # 12345
# addDigitLists(linkedList, noneLinked).printList() # 12,345 + 0 = 12,345
# addDigitLists(linkedList, singleNode).printList() # 12,345 + 1 = 12,346
# addDigitLists(linkedList, linkedList).printList() # 12,345 + 12,345 = 24,690

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Convert Linked List to Number
# DIGITS ARE STORED IN FORWARD ORDER
def getListNum_FORWARD(linkedlist):
    # Initialize variable to store list size
    size = linkedlist.size()
    # Initialize variable to store list num
    number = 0
    # If list has no elements, then its num is 0
    if size == 0: number = 0
    # If list has 1 element then it's 1 digit, and its num is its data value
    elif size == 1: number = linkedlist.head.getData()
    # Otherwise, we need to loop through and form the number from the digits
    else:
        # Initialize variable to store current Node
        this = linkedlist.head
        # Initialize variable to store String form of our list's number
        snum = ''
        # Loop through list for every Node that is not None
        while this is not None:
            # Append each digit after snum since last Node is 1's digit now
            snum += str(this.getData())
            # Continue to the next Node to get the next digit
            this = this.getNext()
        # Convert our String to an int and set it as the list's number
        number = int(snum)
    # Return the final number!
    return number

# Return linked list representing total of two "Digit" Linked Lists
def addDigitLists_FORWARD(list1, list2):
    # Initialize variable to store resulting list
    resultlist = LinkedList()
    # Store total of linked lists as String
    total = str(getListNum_FORWARD(list1) + getListNum_FORWARD(list2))
    # Create a new Node for each digit in total FORWARD this time
    for c in total[::-1]:
        resultlist.insertNode(c)
    # Return our result list
    return resultlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(2,n0)
n2 = Node(3,n1)
n3 = Node(4,n2)
n4 = Node(5,n3)

noneLinked = LinkedList()
singleNode = LinkedList(n0)
linkedList = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print getListNum_FORWARD(noneLinked)                      # 0
# print getListNum_FORWARD(singleNode)                      # 1
# print getListNum_FORWARD(linkedList)                      # 54321
# addDigitLists_FORWARD(linkedList, noneLinked).printList() # 54,321 + 0 = 54,321
# addDigitLists_FORWARD(linkedList, singleNode).printList() # 54,321 + 1 = 54,322
# addDigitLists_FORWARD(linkedList, linkedList).printList() # 54,321 + 54,321 = 108,642

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Return linked list representing total of two "Digit" Linked Lists
def addDigitLists_ALTERNATE(list1, list2):

    # Initialize variable to store list sizes
    size_list1 = list1.size()
    size_list2 = list2.size()

    # Initialize variable to store list sizes based on size
    # Initialize variable to store current Node dependent on sizes
    if size_list1 > size_list2:
        large = size_list1
        small = size_list2
        largeList = list1.head
        smallList = list2.head
    else:
        # Otherwise,  size_list1 <= size_list2:
        large = size_list2
        small = size_list1
        largeList = list2.head
        smallList = list1.head

    # Initialize variable to store carry value, which will be 0 or 1
    carry = 0

    # Initialize variable to store resulting sum list
    resultlist = LinkedList()

    # We want the result list to be same size as our large list
    for i in range(large):
        resultlist.insertNode(0)

    # Initialize variable to store current node in result list
    this = resultlist.head

    # Loop through each Node until smaller list is out of Nodes
    while smallList is not None:
        # Add the head Node of each list and the carry value
        digit_total = largeList.getData() + smallList.getData() + carry
        # The sum is greater than or equal to 10
        if digit_total >= 10:
            # Set a carry value for next iteration to use
            carry = 1
            # Set Node with total - 10, since each Node holds a single digit
            this.setData(digit_total-10)
            # Continue to the next Node for our lists!
            largeList = largeList.getNext()
            smallList = smallList.getNext()
            prev = this
            this = this.getNext()
        else:
            # There is no need to add a carry value for next iteration
            carry = 0
            # Set Node with the totalled digit
            this.setData(digit_total)
            # Continue to the next Node for our lists!
            largeList = largeList.getNext()
            smallList = smallList.getNext()
            prev = this
            this = this.getNext()

    # Continue looping through remaining Nodes in largeList
    while largeList is not None:
        # Add the head Node of the large list and the carry value only
        # The small list has no remaining Nodes so just add a 0
        digit_total = largeList.getData() + 0 + carry
        # The sum is greater than or equal to 10
        if digit_total >= 10:
            # Set a carry value for next iteration to use
            carry = 1
            # Set Node with total - 10, since each Node holds a single digit
            this.setData(digit_total-10)
            # Continue to the next Node for our large list only! & result list
            largeList = largeList.getNext()
            prev = this
            this = this.getNext()
        else:
            # There is no need to add a carry value for next iteration
            carry = 0
            # Set Node with the totalled digit
            this.setData(digit_total)
            # Continue to the next Node for our large list only! & result list
            largeList = largeList.getNext()
            prev = this
            this = this.getNext()
    
    # The sum went beyond the size of our large list
    if carry is 1:
        prev.setNext(Node(1))

    # Return the resulting sum of the lists
    return resultlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(2,n0)
n2 = Node(3,n1)
n3 = Node(4,n2)
n4 = Node(5,n3)

noneLinked = LinkedList()
singleNode = LinkedList(n0)
linkedList = LinkedList(n4)

n5 = Node(5, None)
n6 = Node(0, n5)
n7 = Node(0, n6)
n8 = Node(0, n7)
n9 = Node(0, n8)

largerList = LinkedList(n9)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# addDigitLists_ALTERNATE(linkedList, singleNode).printList() # 12,345 + 1 = 12,346
# addDigitLists_ALTERNATE(singleNode, linkedList).printList() # 1 + 12,345 = 12,346
# addDigitLists_ALTERNATE(linkedList, linkedList).printList() # 12,345 + 12,345 = 24,690
# addDigitLists_ALTERNATE(largerList, largerList).printList() # 50,000 + 50,000 = 100,000

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Reverse the given linked list
def reverseList(linkedlist):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initialize variable to store reversed linked list
    newList = LinkedList()
    # Loop through the remaining Nodes in list that are not None
    while this is not None:
        # Insert a new Node into our new list
        # With data from the current Node from our given list
        # insertNode() also sets the next value of the inserted Node
        newList.insertNode(this.getData())
        # Continue to link the next Node in our given linkedlist!
        this = this.getNext()
    # The list has been successfully reversed, return it!
    return newList

# Return linked list representing total of two "Digit" Linked Lists
def addDigitLists_ALTERNATE_FORWARD(list1, list2):

    # Initialize variable to store list sizes
    size_list1 = list1.size()
    size_list2 = list2.size()

    # Reverse the lists
    list1 = reverseList(list1)
    list2 = reverseList(list2)

    # Initialize variable to store list sizes based on size
    # Initialize variable to store current Node dependent on sizes
    if size_list1 > size_list2:
        large = size_list1
        small = size_list2
        largeList = list1.head
        smallList = list2.head
    else:
        # Otherwise,  size_list1 <= size_list2:
        large = size_list2
        small = size_list1
        largeList = list2.head
        smallList = list1.head

    # Initialize variable to store carry value, which will be 0 or 1
    carry = 0

    # Initialize variable to store resulting sum list
    resultlist = LinkedList()

    # We want the result list to be same size as our large list
    for i in range(large):
        resultlist.insertNode(0)

    # Initialize variable to store current node in result list
    this = resultlist.head

    # Loop through each Node until smaller list is out of Nodes
    while smallList is not None:
        # Add the head Node of each list and the carry value
        digit_total = largeList.getData() + smallList.getData() + carry
        # The sum is greater than or equal to 10
        if digit_total >= 10:
            # Set a carry value for next iteration to use
            carry = 1
            # Set Node with total - 10, since each Node holds a single digit
            this.setData(digit_total-10)
            # Continue to the next Node for our lists!
            largeList = largeList.getNext()
            smallList = smallList.getNext()
            this = this.getNext()
        else:
            # There is no need to add a carry value for next iteration
            carry = 0
            # Set Node with the totalled digit
            this.setData(digit_total)
            # Continue to the next Node for our lists!
            largeList = largeList.getNext()
            smallList = smallList.getNext()
            this = this.getNext()

    # Continue looping through remaining Nodes in largeList
    while largeList is not None:
        # Add the head Node of the large list and the carry value only
        # The small list has no remaining Nodes so just add a 0
        digit_total = largeList.getData() + 0 + carry
        # The sum is greater than or equal to 10
        if digit_total >= 10:
            # Set a carry value for next iteration to use
            carry = 1
            # Set Node with total - 10, since each Node holds a single digit
            this.setData(digit_total-10)
            # Continue to the next Node for our large list only! & result list
            largeList = largeList.getNext()
            this = this.getNext()
        else:
            # There is no need to add a carry value for next iteration
            carry = 0
            # Set Node with the totalled digit
            this.setData(digit_total)
            # Continue to the next Node for our large list only! & result list
            largeList = largeList.getNext()
            this = this.getNext()
    
    # Reverse our result list so the head is not the 1's digit
    resultlist = reverseList(resultlist)

    # The sum went beyond the size of our large list
    if carry is 1:
        # Insert a node to head of list
        resultlist.insertNode(1)

    # Return the resulting sum of the lists
    return resultlist

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(1,None)
n1 = Node(2,n0)
n2 = Node(3,n1)
n3 = Node(4,n2)
n4 = Node(5,n3)

noneLinked = LinkedList()
singleNode = LinkedList(n0)
linkedList = LinkedList(n4)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# addDigitLists_ALTERNATE_FORWARD(linkedList, noneLinked).printList() # 54,321 + 0 = 54,321
# addDigitLists_ALTERNATE_FORWARD(singleNode, linkedList).printList() # 1 + 54321 = 54,322
# addDigitLists_ALTERNATE_FORWARD(linkedList, linkedList).printList() # 54,321 + 54,321 = 108,642

"""

2.6 Given a circular linked list, implement an algorithm which returns the 
    node at the beginning of the loop.

    Modified version of: "Detect if a linked list has a loop."

"""

# Return the node at the beginning of the loop
def findLoopStart(linkedlisthead):
    # Create two variables to traverse the list
    slow = linkedlisthead
    fast = linkedlisthead
    # Loop through the Nodes
    while fast is not None and fast.next is not None:
        # Slow moves one node at a time
        slow = slow.next
        # While fast moves two nodes at a time
        fast = fast.next.next
        # If there is a loop in the linked list, 
        # then slow and fast will eventually meet
        if slow is fast:
            break
    # Slow and fast did not come to meeting point, therefore there is no loop
    if fast is None or fast.next is None:
        return None
    # Both slow and fast collided, meaning they are both at a meeting point.
    # Move slow back to the head of the list, keep fast the same place
    # Both Fast and Slow are k steps from the Start of the loop
    slow = linkedlisthead
    # When slow reaches fast, fast will have reached the start of the loop
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    # Return the Node fast has landed on (the start of the loop)
    return fast

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node(0,None)
n1 = Node(1,n0)
n2 = Node(2,n1)
n3 = Node(3,n2)
n4 = Node(4,n3)
n5 = Node(5,n4)
n6 = Node(6,n5)
n7 = Node(7,n6)
n0.setNext(n4)
linkedList = LinkedList(n7)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print findLoopStart(n7) == n4 # True

"""

2.7 Implement a function to check if a linked list is a palindrome,

"""

# Reverse the given linked list
def reverseList(linkedlist):
    # Initialize variable to store current Node
    this = linkedlist.head
    # Initialize variable to store reversed linked list
    newList = LinkedList()
    # Loop through the remaining Nodes in list that are not None
    while this is not None:
        # Insert a new Node into our new list
        # With data from the current Node from our given list
        # insertNode() also sets the next value of the inserted Node
        newList.insertNode(this.getData())
        # Continue to link the next Node in our given linkedlist!
        this = this.getNext()
    # The list has been successfully reversed, return it!
    return newList

# Return True if values for given lists are the same
def isEqual(list1, list2):
    # Initialize variable to store current Node
    list1_node = list1.head
    list2_node = list2.head
    # Initialize variable representing boolean return value
    equal = True
    # Loop through the remaining Nodes in list that are not None
    while list1_node is not None:
        # Check if data does not match for lists
        if list1_node.getData() is not list2_node.getData():
            # If they're not, change our return value to False, and break
            equal = False
            break
        # Continue to check the next Nodes in our lists!
        list1_node = list1_node.getNext()
        list2_node = list2_node.getNext()
    # Return our boolean
    return equal

# Returns True if the given linked list is a palindrome
def isPalindrome(linkedlist):
    # Initialize variable to store current Node in list
    this = linkedlist.head
    # Initialize variable to store size of linked list
    size = linkedlist.size()
    # Initialize variable to store the reversed linked list
    reversedlist = reverseList(linkedlist)
    # Linked list is palindrome if its values remain the same when reversed
    return isEqual(linkedlist, reversedlist)

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

n0 = Node('A',None)
n1 = Node('B',n0)
n2 = Node('C',n1)
n3 = Node('B',n2)
n4 = Node('A',n3)

n5 = Node('O',None)
n6 = Node('L',n5)
n7 = Node('L',n6)
n8 = Node('E',n7)
n9 = Node('H',n8)

none_Linked = LinkedList()
single_Node = LinkedList(n0)
linkedList1 = LinkedList(n4)
linkedList2 = LinkedList(n9)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print reverseList(none_Linked).printList()  # ''
# print reverseList(single_Node).printList()  # A
# print reverseList(linkedList1).printList()  # ABCBA
# print reverseList(linkedList2).printList()  # OLLEH
# print isPalindrome(none_Linked) # True
# print isPalindrome(single_Node) # True
# print isPalindrome(linkedList1) # True
# print isPalindrome(linkedList2) # False


