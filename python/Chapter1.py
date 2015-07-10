"""

Alexander Seeto
Unofficial Python Solutions
http://www.alexseeto.com

Cracking The Coding Interview
by Gayle Laakmann McDowell
Link: http://amzn.to/1biovdS

# +--------------------------------------------------------------------------+
# |                      CHAPTER 1: ARRAYS AND LISTS                         |
# +--------------------------------------------------------------------------+

"""

"""

1.1 Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

"""

# Check if unique using Set
def isUniqueWithSet(a_string):
    # If there are more than 256 chars in given String, there are duplicates
    if len(a_string > 256):
        return False
    # A Set is an unordered collection of unique elements
    uniqueChars = set()
    # Loop through each character in given String
    for c in a_string:
        # if character exists in the set, return False
        if c in uniqueChars:
            return False
        else:
            # Otherwise, add the character to the set
            uniqueChars.add(c)
    # Completing loop means all characters are unique
    return True

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print isUniqueWithSet("abc") # True
# print isUniqueWithSet("abb") # False
# print isUniqueWithSet("bab") # False

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""
    
# Check if unique without using Set
def isUnique(a_string):
    # If there are more than 256 chars in given String, there are duplicates
    if len(a_string > 256):
        return False
    # Create an array based off of # of unique ASCII chars
    chars = [False] * 256
    # Loop through each character in given String
    for c in a_string:
        # If current character is still set at default of False
        if not chars[ord(c)]:
            # Set it as True in array
            chars[ord(c)] = True
        else:
            # Otherwise, it was already found and is therefore not unique
            return False
    # Completing loop means all characters are unique
    return True

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print isUnique("abc") # True
# print isUnique("abb") # False
# print isUnique("bab") # False

"""

1.2 Implement a function reverse(str) in which reverses a string.

"""

# Reverse a given String
def reverse(a_string):
    # Treat String as list of chars. Append by stepping backwards.
    return a_string[::-1]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+
print reverse("")    # ""
print reverse("abc") # cba

"""

1.3 Given two strings, write a method to decide if one is a permutation of the
    other.

"""

# Check if s1 are permutations of one another
def isPermutation(s1, s2):
    # Convert each string to list of characters.
    # Sort each list and compare whether they are equal
    return sorted(list(s1)) == sorted(list(s2))

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+
# print isPermutation("abc", "bca") # True
# print isPermutation("abc", "bcb") # False

"""

1.4 Write a method to replace all spaces in a string with '%20'. You may assume
    that the string has sufficient space at the end of the string to hold the 
    additional characters, and that you are given the "true" length of the 
    string. (Note: if implementing in Java, please use a character array so 
    that you can perform this operation inplace.)

"""

# Replace spaces in given String with given character 'r'
def replaceSpaces(a_string, r):
    result = ''
    for c in a_string:
        if c == ' ':
            result += r
        else:
            result += c
    return result

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print replaceSpaces("a b c", "%20") == "a%20b%20c" # True
# print replaceSpaces("a b c", "") == "abc"          # True
# print replaceSpaces("a b c", "") == "a b c"        # False

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""
    
# Using built-in Python replace function
def replaceSpaces_BETTER(a_string, r):
    return a_string.replace(' ', r)

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+
# print replaceSpaces_BETTER("a b c", "%20") == "a%20b%20c" # True
# print replaceSpaces_BETTER("a b c", "") == "abc"          # True
# print replaceSpaces_BETTER("a b c", "") == "a b c"        # False

"""

1.5 Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become 
    a2b1c5a3. If the "compressed" string would not become smaller than the 
    original string, your method should return the original string.

"""

# Get frequency before a different character is reached
def getFrequency(s, a_string):
    counter = 0
    for c in a_string:
        if c==s:
            counter+=1
        else:
            break
    return counter

# Return compressed String using counts of repeated characters
def compressString(a_string):
    # Compressed string to be (maybe) returned
    compressed = ''
    # Save copy of last character in loop
    lastChar = ''
    # Loop through each character in given String
    for index, c in enumerate(a_string):
        # Check if the last char is the same as current char
        if c == lastChar:
            # Save the current char as last char for next iteration
            lastChar = c
            # Continue to next iteration since this char is same as last char
            continue
        # Save the current char as last char for next iteration
        lastChar = c
        # Add character to compressed string
        compressed += c
        # Find frequency of character in remaining string
        frequency = getFrequency(c, a_string[index:])
        # Add frequency to compressed string
        compressed += str(frequency)
    # Return given String if it is equal in length to compressed string
    if len(compressed) == len(a_string):
        return a_string
    else:
        # Otherwise return compressed string
        return compressed

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print getFrequency('a', 'aababb')                 # 2
# print getFrequency('a', 'aaabbb')                 # 3
# print compressString("aab") == "a2b1"             # True
# print compressString("aabcccccaaa") == "a2b1c5a3" # True

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""
    
# Get frequency before a different character is reached
def getFrequency_ALTERNATE(a_string, index):
    # Initialize return variable representing frequency of current character
    counter = 0
    # Save copy of current character in string
    current = a_string[index]
    # While the current character equals
    while index < len(a_string) and current == a_string[index]:
            # Add one to go to next character in string
            index += 1
            # Add one to count of current character in string
            counter += 1
    # Return the frequency of the current character
    return counter

# Return compressed String using counts of repeated characters
def compressString_ALTERNATE(a_string):
    # Compressed string array to be (maybe) returned
    compressed = []
    # Initialize variable to store current index in string
    index = 0
    # Loop through each character in given String
    while index < len(a_string):
        # Find frequency of character in remaining string
        frequency = getFrequency_ALTERNATE(a_string, index)
        # Add character and frequency to compressed string
        compressed.append(a_string[index] + str(frequency))
        # Update our index!
        index += int(frequency)
    # Flatten array into String
    compressed = ''.join(compressed)
    # Return given String if it is equal in length to compressed string
    if len(compressed) == len(a_string):
        return a_string
    else:
        # Otherwise return compressed string
        return compressed

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print getFrequency_ALTERNATE('aabab', 0)                    # 2
# print getFrequency_ALTERNATE('abbba', 1)                    # 3
# print compressString_ALTERNATE("aab") == "a2b1"             # True
# print compressString_ALTERNATE("aabcccccaaa") == "a2b1c5a3" # True

"""

1.6 Given an image represented by an NxN matrix, where each pixel in the image 
    is 4 bytes, write a method to rotate the image by 90 degrees. Can you do 
    this in place?

"""

# Print matrix all pretty-like
def displayMatrix(matrix):
    # If matrix is not empty
    if matrix:
        # Loop through and print each row on its own line
        for i in range(len(matrix)):
            print matrix[i]
    else:
        # Otherwise print error message
        print "Please make sure at least 1 element exists in Matrix."

# Rotate a given square matrix where size represents its column and row count
def rotate(matrix, size):
    # Initialize first layer (0-indexed)
    layer = 0
    # We will be rotating each of the elements in each of the "rings" or layers in our given matrix beginning with the outermost ring
    while layer < size/2:
        first = layer
        last = size - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # Left --> Top
            matrix[first][i] = matrix[last - offset][first]
            # Bottom --> Top
            matrix[last - offset][first] = matrix[last][last - offset]
            # Right --> Bottom
            matrix[last][last - offset] = matrix[i][last]
            # Top --> Right
            matrix[i][last] = top
        layer+=1
    return matrix


# TL;DR: STEPS FOR THE FOLLOWING PYTHON-Y SOLUTION
#  - Transpose each column into a row
#  - Step backwards (to append rows in reverse)
#  - Convert tuples into lists for return (optional)

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""
    
# Rotate a given square matrix 90 degrees clockwise
def rotate_CW_ALTERNATE(matrix):
    # zip takes an iterable and returns a new array of tuples.
    # Each tuple contains the i-th element from each array.
    # This means it will take an element from each "row" (see Test Cases).
    # This effectively transposes the columns into rows.
    # The [::-1] denotes the "step" value when creating the transposed arrays.
    # -1 reverses the order of the tuple so it exhibits 90 degree rotation CW.
    tuples = zip(*matrix[::-1])
    # list() converts the tuples to arrays to follow format of our examples.
    return [list(row) for row in tuples]

""" +---------------------------------------------------------------------+
    |                    SAME PROBLEM : ALTERNATE SOLUTION                |
    +---------------------------------------------------------------------+"""
    
# Rotate a given square matrix 90 degrees counter-clockwise
def rotate_CCW_ALTERNATE(matrix):
    # zip takes an iterable and returns a new array of tuples.
    # Each tuple contains the i-th element from each array.
    # This means it will take an element from each "row" (see Test Cases).
    # This effectively transposes the columns into rows.
    # The [::-1] denotes the "step" value when creating the transposed arrays.
    # -1 reverses the order of the tuple so it exhibits 90 degree rotation CCW.
    tuples = zip(*matrix)[::-1]
    # list() converts the tuples to arrays to follow format of our examples.
    return [list(row) for row in tuples]

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+
matrix_2x2      = [ [1, 2] ,
                    [3, 4] ]

matrix_2x2_CW   = [ [3, 1] ,
                    [4, 2] ]

matrix_3x3      = [ [1, 2, 3] ,
                    [4, 5, 6] ,
                    [7, 8, 9] ]

matrix_3x3_CW   = [ [7, 4, 1] ,
                    [8, 5, 2] ,
                    [9, 6, 3] ]

matrix_4x4      = [ ['01', '02', '03', '04'] ,
                    ['05', '06', '07', '08'] ,
                    ['09', '10', '11', '12'] ,
                    ['13', '14', '15', '16'] ]

matrix_4x4_CW   = [ ['13', '09', '05', '01'] ,
                    ['14', '10', '06', '02'] ,
                    ['15', '11', '07', '03'] ,
                    ['16', '12', '08', '04'] ]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# displayMatrix([])
# displayMatrix([[]])
# displayMatrix([[1]])
# displayMatrix(matrix_2x2)
# displayMatrix(matrix_3x3)
# displayMatrix(matrix_4x4)

# print rotate(matrix_2x2, 2) == matrix_2x2_CW # True
# print rotate(matrix_3x3, 3) == matrix_3x3_CW # True

# displayMatrix(rotate(matrix_2x2, 2))
# displayMatrix(rotate_CW_ALTERNATE(matrix_2x2))
# displayMatrix(rotate_CW_ALTERNATE(matrix_3x3))
# displayMatrix(rotate_CW_ALTERNATE(matrix_4x4))
# displayMatrix(rotate_CCW_ALTERNATE(matrix_2x2))
# displayMatrix(rotate_CCW_ALTERNATE(matrix_3x3))

"""

1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire
    row and column are set to 0.

"""

# Set row and column in matrix to all 0s if 0 is already present
def setZero(matrix):
    # Set m as number of rows
    m = len(matrix)
    # Set n as number of cols
    n = len(matrix[0])
    # Initiate boolean list defaulted at False for number of rows
    row = [False]*m
    # Initiate boolean list defaulted at False for number of cols
    col = [False]*n
    # Loop through each index to find row(s) and column(s) with 0s
    for i in range(n):
        for j in range(m):
            # If you find a 0 in the matrix
            if matrix[i][j] == 0:
                # Save its row index as True
                row[i] = True
                # Save its col index as True
                col[j] = True
    # Using saved row and col index values, set data with those indices to 0
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

matrix_3x3_0    = [ [1, 2, 3] ,
                    [4, 0, 6] ,
                    [7, 8, 9] ]

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# displayMatrix(setZero(matrix_3x3_0))

"""

1.8 Assume you have a method isSubstring which checks if one word is a substring 
    of another. Given two strings, s1 and s2, write code to check if s2 is a 
    rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a 
    rotation of "erbottlewat").

"""

# Return True if s2 is a rotation of s1
def isRotation(s1, s2):
    # Check s1 and s2 are of equal length, otherwise return False
    if not len(s1) == len(s2): return False
    # Append s1 to s1 as a rotation must exist within a doubled s1 string
    if s2 in s1+s1: return True

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# print isRotation("bbadfga", "a")           # False
# print isRotation("bbadaasdfafga", "asdfa") # False
# print isRotation("asdf", "sdfa")           # True



