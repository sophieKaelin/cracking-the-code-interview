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
