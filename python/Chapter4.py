"""

Alexander Seeto
Unofficial Python Solutions
http://www.alexseeto.com

Cracking The Coding Interview
by Gayle Laakmann McDowell
Link: http://amzn.to/1biovdS

# +--------------------------------------------------------------------------+
# |                        CHAPTER 4: TREES AND GRAPHS                       |
# +--------------------------------------------------------------------------+

"""

# Class representing a Binary Tree
class BinaryTree(object):
    def __init__(self, value=None):
        # Left node containing BT or None
        self.left = None
        # Right node containing BT or None
        self.right = None
        # ID of BT
        self.value = value

    # Returns the left BT
    def getLeft(self):
        return self.left

    # Returns the right BT
    def getRight(self):
        return self.right

    # Insert a BT into this binary tree's left side
    def insertLeft(self, value):
        # Create a new BT node for the given value
        btree = BinaryTree(value)
        # If there's no left for this BT
        if self.left == None:
            # Insert the new BT node as its left
            self.left = btree
        else:
            # Otherwise, save the current left to a variable
            left = self.left
            # Set the left of this BT as the new BT node
            btree.left = left
            # Then set the left of this new BT node as the old left
            self.left = btree

    # Insert a BT into this binary tree's right side
    def insertRight(self, value):
        # Create a new BT node for the given value
        btree = BinaryTree(value)
        # If there's no right for this BT
        if self.right == None:
            # Insert the new BT node as its right
            self.right = btree
        else:
            # Otherwise, save the current right to a variable
            right = self.right
            # Set the right of this BT as the new BT node
            btree.right = right
            # Then set the right of this new BT node as the old right
            self.right = btree

# Helper function to visualize binary tree
def printBTree(btree):
    if btree is not None:
        print btree.value
        printBTree(btree.getLeft())
        printBTree(btree.getRight())

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

"""

4.1 Implement a function to check if a binary tree is balanced. For the 
    purposes of this question, a balanced tree is defined to be a tree such 
    that the heights of the two subtrees of any node never differ by more 
    than one.

"""

# Returns height of given Binary Tree
def getHeight(btree):
    # If the Binary Tree is None
    if btree is None:
        # Then its height is 0
        return 0
    else:
        # Otherwise its height is 1 + the greater of its left or right side
        return 1 + max(getHeight(btree.left), getHeight(btree.right))

# Returns True if binary tree is balanced
def isBalanced(btree):
    # If the Binary Tree is None
    if btree is None:
        # Then the tree is balanced!
        return True
    else:
        # Otherwise, get the difference between the left and right heights 
        diff = getHeight(btree.left) - getHeight(btree.right)
        # If left is less than right, then we'll get a negative, so fix that!
        # We take the absolute value and make sure the difference isn't > 1
        if abs(diff) > 1:
            # If the difference is more than one, then our BT is unbalanced
            return False
        else:
            # Otherwise, recurse and check the left and right side of our BT
            return isBalanced(btree.left) and isBalanced(btree.right)

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

# BTREE = BinaryTree("Root")
# BTREE.insertLeft("(Left, 1)")
# BTREE.insertRight("(Right, 1)")
# BTREE.left.insertLeft("(Left, 2)")
# BTREE.left.insertRight("(Right, 2)")
# BTREE.right.insertLeft("(Left, 3)")
# BTREE.right.insertRight("(Right, 3)")

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# printBTree(BTREE)
# print isBalanced(BTREE)

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""

# Returns -1 if binary tree is not balanced
def checkHeight(btree):
    # The height of this BT is 0
    if btree is None:
        return 0
    # The height of this BT's left branch had a difference > 1
    leftHeight = checkHeight(btree.left)
    if leftHeight == -1:
        return -1
    # The height of this BT's right branch had a difference > 1
    rightHeight = checkHeight(btree.right)
    if rightHeight == -1:
        return -1
    # Get the difference between the left and right heights 
    heightDiff = leftHeight - rightHeight
    # If left is less than right, then we'll get a negative, so fix that!
    # We take the absolute value and make sure the difference isn't > 1
    if abs(heightDiff) > 1:
        # If the difference is more than one, then our BT is unbalanced
        return -1
    else:
        # If not, we return the height of this BT
        return max(leftHeight, rightHeight) + 1

# Returns True if our binary tree is balanced
def isBalanced_BETTER(btree):
    if checkHeight(btree) == -1:
        return False
    else:
        return True

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# BTREE = BinaryTree("Root")
# BTREE.insertLeft("1")
# BTREE.insertRight("1")
# BTREE.left.insertLeft("2")
# BTREE.left.insertRight("2")
# BTREE.right.insertLeft("3")
# BTREE.right.insertRight("3")
# printBTree(BTREE)
# print isBalanced_BETTER(BTREE)

"""

4.2 Given a directed graph, design an algorithm to find out whether there 
    is a route between two nodes.

"""

# Returns True if a route between given nodes in a directed graph exists
# This function utilizes Breadth First Search meaning adjacent nodes are
# visited before visiting any 'grandchildren' nodes
def search_BFS(graph, here, there):
    # You're always somewhere and you can't end up nowhere.
    # So if you don't get get a place on the graph for here or there.. FALSE!
    if here is None or there is None: return False
    # Initialize a hash map to mark places as True if they're visited
    # Each "place" is a "key" with True as its value
    visited = {}
    # Initialize a queue to store our current location
    # We start 'here', so add our starting point to the queue
    queue = [here]
    # Loop through nodes in our graph while queue is not empty
    while queue != []:
        # Where are we? Pop the value stored in our queue to find out
        # Make sure to pop from first index, as to follow breadth first
        place = queue.pop(0)
        # If this place is the same as our desired endpoint... we made it!
        if place == there:
            # Therefore, return True
            return True
        # Otherwise, mark this place visited. We set the place as a key in 
        # our hashmap holding a value of True
        visited[place] = True
        # Get the next place in our graph that we haven't visited yet
        for n in graph.get(place, []):
            # Verify this place hasn't been visited already
            if n not in visited:
                # Then add it to our queue
                queue.append(n)
    # If the while loop completes, we couldn't get to 'there' from 'here'
    return False

# Returns True if a route between given nodes in a directed graph exists
# This function utilizes Depth First Search meaning an adjacent node will
# be searched and its children will be searched before looking at another
# adjacent node from the root
def search_DFS(graph, here, there, visited = None):
    # Initialize hashmap
    if visited == None:
        visited = {}
    # If this place is the same as our desired endpoint... we made it!
    if here == there:
        # Therefore, return True
        return True
    # Otherwise, mark this place visited. We set the place as a key in 
    # our hashmap holding a value of True
    visited[here] = True
    # Get the next place in our graph that we haven't visited yet
    for place in graph.get(here, []):
        # Verify this place hasn't been visited already
        if place not in visited:
            # Recurse with this next place in our graph
            if search_DFS(graph, place, there, visited):
                # If the result is True, return True
                return True
    # Otherwise return False as we couldn't get to 'there' from 'here'
    return False    

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

"""

Reference to Clarify Understanding: 
https://www.python.org/doc/essays/graphs/

        ROUTES         -->        DICT (Graph Representation)

        A -> B                    graph = {'A': ['B', 'C'],
        A -> C                             'B': ['C', 'D'],
        B -> C                             'C': ['D'],
        B -> D                             'D': ['C'],
        C -> D                             'E': ['F'],
        D -> C                             'F': ['C']}
        E -> F          
        F -> C

"""

graph = dict()
graph['A']=['B','C']
graph['B']=['C','D']
graph['C']=['D']
graph['D']=['C']
graph['E']=['F']
graph['F']=['C']

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print search_BFS(graph, 'B', 'A') # False
# print search_BFS(graph, 'A', 'B') # True
# print search_BFS(graph, 'C', 'D') # True
# print search_BFS(graph, 'E', 'F') # True
# print search_BFS(graph, 'F', 'D') # True

# print search_DFS(graph, 'B', 'A') # False
# print search_DFS(graph, 'A', 'B') # True
# print search_DFS(graph, 'C', 'D') # True
# print search_DFS(graph, 'E', 'F') # True
# print search_DFS(graph, 'F', 'D') # True

"""

4.3 Given a sorted (increasing order) array with unique integer elements, 
    write an algorithm to create a binary search tree with minimal height.

"""

# Return a binary search tree with minimal height using the given sorted array
def createBST_Helper(array, beg, end):
    # Stop recursion when the starting point exceeds the array's greatest index
    if end < beg: return None
    # Take the middle index (beginning index + end index divided by 2)
    mid = (beg + end) / 2
    # The middle index is the root
    bst = BinaryTree(array[mid])
    # The left side becomes the root's left
    bst.left = createBST_Helper(array, beg, mid-1)
    # The right side becomes the root's right
    bst.right = createBST_Helper(array, mid+1, end)
    # Return the final BST
    return bst

# Return a binary search tree with minimal height using the given sorted array
def createBST(array):
    # Get the length of the array - 1 into our recursive function
    return createBST_Helper(array, 0, len(array)-1)

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

# array1 = [1,4,5]
# array2 = [1,4,5,10]
# array3 = [0,1,2,3,4,5]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# printBTree(createBST(array1))
# printBTree(createBST(array2))
# printBTree(createBST(array3))

"""

4.4 Given a binary tree, design an algorithm which creates a linked list of 
    all the nodes at each depth (e.g., if you have a tree with depth D, you'll 
    have D linked lists).

"""

"""

4.5 Implement a function to check if a binary tree is a binary search tree.

"""

"""

4.6 Write an algorithm to find the 'next' node (i.e., in-order successor) of a 
    given node in a binary search tree. You may assume that each node has a 
    link to its parent.

"""

"""

4.7 Design an algorithm and write code to find the first common ancestor of 
    two nodes in a binary tree. Avoid storing additional nodes in a data 
    structure. NOTE: This is not necessarily a binary search tree.

"""

"""

4.8 You have two very large binary trees: T1, with millions of nodes, and T2, 
    with hundreds of nodes. Create an algorithm to decide if T2 is a subtree 
    of T1.

    A tree T2 is a subtree of Tl if there exists a node n in Tl such that the 
    subtree of n is identical to T2. That is, if you cut off the tree at node 
    n, the two trees would be identical.

"""

"""

4.9 You are given a binary tree in which each node contains a value. Design an 
    algorithm to print all paths which sum to a given value. The path does not 
    need to start or end at the root or a leaf.

"""

