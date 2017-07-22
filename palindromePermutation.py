"""
Check if permutation of the given string is palindrome. If yes, Print all palindromes
"""
from collections import Counter
from itertools import permutations

def isPalindrome(s):
    # String is palindrome if there is even number of each element and/or another single element
    s = s.replace(' ', '').lower()
    return sum(freq % 2 for freq in Counter(s).values()) < 2


def getHalfString(s):
    # returns half of the total elements in a string + the odd character
    counts = Counter(s)
    half_str = ""
    odd_char = ""
    for k, v in counts.iteritems():
        if v % 2 == 0:
            half_str += k * (v / 2)
        else:
            odd_char = k
    return half_str, odd_char


def getPermutations(s):
    """

    :rtype: list of permutation strings
    """
    gh = permutations(s) # returns generator with tuples
    all_perm = ["".join(p) for p in gh]
    return list(set(all_perm))


def revString(s):
    return s[::-1]


def printAllPossiblePalindromes(s):
    # check in given string can be palindrome
    """

    :type s: String
    """
    if not isPalindrome(s): return "String is not palindrome"

    # idea is get half string and the odd character (if applicable)
    # get all permutations of the half string
    # attach the odd character at the end and attach the reverse of the half string after that
    half_str, odd = getHalfString(s)
    all_half_perms = getPermutations(half_str)
    all_full_perms = []

    for i in all_half_perms:
        string = i + odd + revString(i)
        print string
        all_full_perms.append(string)
    print len(all_full_perms)

def test():
    s = "aabbcadad"
    printAllPossiblePalindromes(s)


if __name__=='__main__':
    test()