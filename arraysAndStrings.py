# Arrays and Strings Interview Questions

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters
def isUnique(string):
    for letter in string:
        if string.index(letter) != string.rindex(letter):
            return False
    return True

# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
def isPermutation(string1, string2):
    if len(string1) == len(string2) == 0:
        return True
    elif len(string1) == 0 or len(string2) == 0:
        return False
    elif string1[0] in string2:
        return isPermutation(string1[1:], string2.replace(string1[0],'',1))
    else:
        return False

# 1.3 URLify: Write a method to replace all spaces in a string with %20
def URLify(string):
    # SIMPLE: return string.replace(' ', '%20')
    newstring = ""
    for ch in string:
        if ch is ' ':
            newstring += '%20'
        else:
            newstring += ch 
    return newstring

# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. Permutation is rearangment of letters
def palindrome(string):
    chs = {}
    for ch in string: # count number of characters
        if ch not in chs:
            chs[ch] = 1
        else:
            chs[ch] +=1
    countOdds = 0 # Allowed one odd number of character, otherwise not a palindrome
    for key in chs:
        if not chs[key] %2 == 0:
            countOdds +=1
        if countOdds > 1:
            return False
    return True
<<<<<<< HEAD

def test_palindrome():
    assert palindrome("racecar") == True
    assert palindrome("racecra") == True
    assert palindrome("raceca") == False
    assert palindrome("") == True
    assert palindrome("a") == True
    assert palindrome("abc") == False

# 1.5 One Away: There are three types of edits that can be performed on strings: insert a char, remove a char, replace a char
# Given 2 strings, write a function to check if they are one edit (or zero edits) away.


# 1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated chars
# e.g. aabcccccaaa would become a2b1c5a3
# If your compressed string would not become smaller than the original string, your method should return the original.
# Limited to lower and upper case letters

# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image 90 degrees

# 1.8 Zero Matrix: Write an algorithm such that if an element in a MxM matrix is 0, its entire row and column are set to 0

# 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given 2 stringscheck if s2 is a rotation of s1 using one call to isSubstring
# e.g. waterbottle is a rotation of erbottlewat

if __name__ == "__main__":
    # Write tests here
    test_isUnique()
    test_isPermutation()
    test_URLify()
    test_palindrome()
    print("Everything passed")
=======
>>>>>>> 9902d38d4b714dd79ddcf371c026d4ecd38814d5
