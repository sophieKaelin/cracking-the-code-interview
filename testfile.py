from arraysAndStrings import isUnique, isPermutation, URLify, palindrome

def test_isUnique():
    assert isUnique("abcdefg") == True, "Should be True"
    assert isUnique("abcdefa") == False, "Should be False"
    assert isUnique("") == True, "Should be True when empty string"
    assert isUnique("a") == True, "Should be True if single character"

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

def test_URLify():
    assert URLify("Hello World") == "Hello%20World", "Should be Hello%20World"
    assert URLify("Hello  World") == "Hello%20%20World", "Should be Hello%20%20World"
    assert URLify("HelloWorld") == "HelloWorld", "Should be HelloWorld"
    assert URLify("%20 %20ab") == "%20%20%20ab", "Should be %20%20%20ab"
    assert URLify("") == "", ""
    
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
    print("\t*** Everything passed ***")
