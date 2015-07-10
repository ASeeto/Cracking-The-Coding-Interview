"""

Alexander Seeto
Unofficial Ruby Solutions
http://www.alexseeto.com

Cracking The Coding Interview
by Gayle Laakmann McDowell
Link: http://amzn.to/1biovdS

# +--------------------------------------------------------------------------+
# |                        CHAPTER 2: LINKED LISTS                           |
# +--------------------------------------------------------------------------+

"""


"""

2.1 Write code to remove duplicates from an unsorted linked list.
    
    FOLLOW UP
    
    How would you solve this problem if a temporary buffer is not allowed?

"""

# Remove duplicates using buffer
def removeDupeBuff(linkedlist)
  # Initialize buffer array
  result = Array.new
  for i in 0..linkedlist.length-1
    # Pop value from linkedlist 
    value = linkedlist[i]
    # Check if value already exists in buffer linkedlist
    if !result.include?(value)
      # If not, add to beginning of linkedlist
      result.push(value)
    end
  end
  # Return result
  return result
end

# Use Ruby's built-in function to destroy duplicates
def removeDupe(linkedlist)
  return linkedlist.uniq!
end

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

list1 = [1, 1, 2, 2, 3]
list2 = ["a", "a", "b"]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts removeDupeBuff(list1) == [1,2,3]
# puts removeDupeBuff(list2) == ["a","b"]
# puts removeDupe(list1) == [1,2,3]
# puts removeDupe(list2) == ["a","b"]

"""

2.2 Implement an algorithm to find the kth to last element of a singly linked 
    list.

"""

# Find the kth to last element of a singly linked list
def find(linkedlist, k)
  return k > 1 ? linkedlist.at(linkedlist.length-k) : linkedlist.last
end

# Find the kth to last element of a singly linked list using built in method
# Negative index in slice returns element starting from end of array
def findSlice(linkedlist, k)
  return linkedlist.slice(-k)
end

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

list1 = [1, "b", 2, "a", 3]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts find(list1, 1) == 3
# puts find(list1, 2) == "a"
# puts find(list1, 4) == "b"
# puts findSlice(list1, 1) == 3
# puts findSlice(list1, 2) == "a"
# puts findSlice(list1, 4) == "b"

"""

2.3 Implement an algorithm to delete a node in the middle of a singly linked 
    list, given only access to that node.

"""

# I am solving linked list problems using arrays. Normally this problem would
# be solved by setting the given node equal to the next node's data and next
# values.

# Could be solved if given array and index by simply using delete_at(index)

"""

2.4 Write code to partition a linked list around a value x, such that all nodes 
    less than x come before all nodes greater than or equal to x.

"""

# Partition a linked list around a given value x
def partition(linkedlist, x)
  # Use select block function to create arrays with correct values
  lessThanX = linkedlist.select { |val| val < x }
  moreThanX = linkedlist.select { |val| val >= x }
  # Return values greater than or equal to x appended to values lesser than x
  return lessThanX + moreThanX
end

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

list1 = [3, 7, 4, 9, 2]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts partition(list1, 4) == [3,2,7,4,9]

"""

2.5 You have two numbers represented by a linked list, where each node 
    contains a single digit. The digits are stored in reverse order, such that 
    the 1's digit is at the head of the list. Write a function that adds the 
    two numbers and returns the sum as a linked list.

    FOLLOW UP

    Suppose the digits are stored in forward order. Repeat the above problem.

"""

# Linked lists represent numbers such that the 1's digit is at the head
def reverseLinkedListsSum(linkedlist1, linkedlist2)
  # Convert each list to its represented integer
  linkedlist1 = linkedlist1.reverse!.join.to_i
  linkedlist2 = linkedlist2.reverse!.join.to_i
  # Return the sum as a list
  sum = linkedlist1 + linkedlist2
  return sum.to_s.split('').map { |string| string.to_i }
end

# Linked lists represent numbers such that the 1's digit is the last node
def forwardLinkedListsSum(linkedlist1, linkedlist2)
  # Convert each list to its represented integer
  linkedlist1 = linkedlist1.join.to_i
  linkedlist2 = linkedlist2.join.to_i
  # Return the sum as a list
  sum = linkedlist1 + linkedlist2
  return sum.to_s.split('').map { |string| string.to_i }
end

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

list1 = [1, 1, 1, 1, 1]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts reverseLinkedListsSum(list1, list1) == [2,2,2,2,2]
# puts forwardLinkedListsSum(list1, list1) == [2,2,2,2,2]

"""

2.6 Given a circular linked list, implement an algorithm which returns the 
    node at the beginning of the loop.

    Modified version of: 'Detect if a linked list has a loop.'

"""

# I am solving linked list problems using arrays. Normally this problem would
# be solved by using a slow and fast iterator, finding a collision and then
# returning the beginning node by counting k steps from the collision

"""

2.7 Implement a function to check if a linked list is a palindrome,

"""

# Return true if given linked list is a palindrome
def isPalindrome(linkedlist)
  return true if linkedlist.length <= 1
  return linkedlist.reverse == linkedlist
end

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

list1 = ["A"]
list2 = ["L", "E", "V", "E", "L"]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts isPalindrome(list1)
# puts isPalindrome(list2)


