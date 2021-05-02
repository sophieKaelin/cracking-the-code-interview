# Arrays and Strings Interview Questions

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters
def isUnique(string):
    for letter in string:
        if string.index(letter) != string.rindex(letter):
            return False
    return True

def test_isUnique():
    assert isUnique("abcdefg") == True, "Should be True"
    assert isUnique("abcdefa") == False, "Should be False"
    assert isUnique("") == True, "Should be True when empty string"
    assert isUnique("a") == True, "Should be True if single character"

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

def test_isPermutation():
    assert isPermutation("god", "dog") == True, "Bad and Dog ARE permutations"
    assert isPermutation("cat", "dog") == False, "cat and Dog ARE NOT permutations"
    assert isPermutation("racecar", "acecarr") == True, "Should be True"
    assert isPermutation("racecar", "acecar") == False, "Should be False"
    assert isPermutation("", "") == True, "Should be True"
    assert isPermutation("", "acecarr") == False, "Should be False"
    assert isPermutation("racecar", "") == False, "Should be False"
    assert isPermutation("race car", "acecarr ") == True, "Should be true"
    assert isPermutation("dog", "dog") == True, "Should be true"

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

def test_URLify():
    assert URLify("Hello World") == "Hello%20World", "Should be Hello%20World"
    assert URLify("Hello  World") == "Hello%20%20World", "Should be Hello%20%20World"
    assert URLify("HelloWorld") == "HelloWorld", "Should be HelloWorld"
    assert URLify("%20 %20ab") == "%20%20%20ab", "Should be %20%20%20ab"
    assert URLify("") == "", ""

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

def test_palindrome():
    assert palindrome("racecar") == True
    assert palindrome("racecra") == True
    assert palindrome("raceca") == False
    assert palindrome("") == True
    assert palindrome("a") == True
    assert palindrome("abc") == False

if __name__ == "__main__":
    # Write tests here
    test_isUnique()
    test_isPermutation()
    test_URLify()
    test_palindrome()
    print("Everything passed")