"""

Alexander Seeto
Unofficial Ruby Solutions
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

# Check if a given string is unique
def isUnique(s)
  # Return false if greater than 256 characters
	if s.length > 256
    return false
  else
    # Otherwise create 256 false array
    s = s.split('')
    chars = Array.new(256, false)
    # Loop through each char and set true, if char is found to be true
    # Then it already existed in String so we should return false
    for c in s
      if !chars[c.ord()]
        chars[c.ord()] = true
      else
        return false
      end
    end
    return true
  end
end

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts isUnique('test')
# puts isUnique('Test')

"""

1.2 Implement a function reverse(str) in which reverses a string.

"""

# Reverse a given string
def reverseString(s)
  # Ruby has a built-in reverse function
  return s.reverse!
end

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts reverseString('test')
# puts reverseString('Test')

"""

1.3 Given two strings, write a method to decide if one is a permutation of the 
    other.

"""

# Check if s1 are permutations of one another
def isPermutation(s1, s2)
    # Convert each string to list of characters.
    s1, s2 = s1.split(''), s2.split('')
    # Sort each list and compare whether they are equal
    return s1.sort! == s2.sort!
end

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts isPermutation("abc", "bca") # True
# puts isPermutation("abc", "bcb") # False

"""

1.4 Write a method to replace all spaces in a string with '%20'. You may 
    assume that the string has sufficient space at the end of the string to 
    hold the additional characters, and that you are given the 'true' length 
    of the string. (Note: if implementing in Java, please use a character 
    array so that you can perform this operation inplace.)

"""

def replaceSpace(s)
  return s.gsub(' ', '%20')
end

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts replaceSpace('This is a test ')

"""

1.5 Implement a method to perform basic string compression using the counts 
    of repeated characters. For example, the string aabcccccaaa would become 
    a2b1c5a3. If the 'compressed' string would not become smaller than the 
    original string, your method should return the original string.

"""

# Compress a string
def compressString(s)
  # Initialize result string
  result = ''
  # Split string into an array
  string = s.split('')
  # Remove and store first character of string
  current = string.shift
  # Initialize counter for current char
  counter = 1
  # Loop as long as we still have characters in the string
  while !string.empty?
    # Remove and store the next character
    nextChar = string.shift
    # Compare characters
    if current == nextChar
      # Increase counter if the characters are the same
      counter+=1
    else
      # Append current character and its counter to result
      result += current + counter.to_s
      # Reset counter
      counter = 1
    end
    # Set current as next character
    current = nextChar
  end
  # Account for last letter since loop breaks before appending it
  result += current + counter.to_s
  # Return the compressed string if it is smaller than the original
  return s.length < result.length ? s : result
end

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts compressString('aabcccccaaa') == 'a2b1c5a3'
# puts compressString('abc') == 'abc'

"""

1.6 Given an image represented by an NxN matrix, where each pixel in the 
    image is 4 bytes, write a method to rotate the image by 90 degrees. Can 
    you do this in place?

"""

# Rotate a matrix image 90 degrees clockwise
def rotateClockwise(matrix)
  # Transpose the matrix and reverse each individual array
  return matrix.transpose.map! { |array| array.reverse! }
end

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

# puts rotateClockwise(matrix_2x2).inspect == matrix_2x2_CW.inspect
# puts rotateClockwise(matrix_3x3).inspect == matrix_3x3_CW.inspect

"""

1.7 Write an algorithm such that if an element in an MxN matrix is 0, its 
    entire row and column are set to 0.

"""

# Create a row and col array of indexes where 0's are located
def setZeroes(matrix)
  # Get matrix height and width
  rows = matrix.length
  cols = matrix[0].length
  # Initialize boolean matrix key
  row_indexes = Array.new(rows, false)
  col_indexes = Array.new(cols, false)
  # Iterate through and set locations with 0 as true
  for row in 0..rows-1
    for col in 0..cols-1
      if matrix[row][col] == 0
        row_indexes[row] = true
        col_indexes[col] = true
      end
    end
  end
  # Iterate through and set locations with true as 0
  for row in 0..rows-1
    for col in 0..cols-1
      if row_indexes[row] or col_indexes[col]
        matrix[row][col] = 0
      end
    end
  end
  return matrix
end

# +--------------------------------------------------------------------------+
# |                              EXAMPLE CASES                               |
# +--------------------------------------------------------------------------+

matrix_3x3_init = [ [1, 2, 3, 4] ,
                    [1, 0, 3, 4] ,
                    [1, 2, 3, 4] ]

matrix_3x3_zero = [ [1, 0, 3, 4] ,
                    [0, 0, 0, 0] ,
                    [1, 0, 3, 4] ]
# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts setZeroes(matrix_3x3_init).inspect == matrix_3x3_zero.inspect

"""

1.8 Assume you have a method isSubstring which checks if one word is a 
    substring of another. Given two strings, s1 and s2, write code to check 
    if s2 is a rotation of s1 using only one call to isSubstring (e.g., 
    'waterbottle' is a rotation of 'erbottlewat').

"""

def isRotation(s1, s2)
  return (s2+s2).include? s1
end

# +--------------------------------------------------------------------------+
# |                                TEST CASES                                |
# +--------------------------------------------------------------------------+

# puts isRotation("waterbottle", "erbottlewat")