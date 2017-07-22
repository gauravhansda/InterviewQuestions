"""
Return most occurred character in alphabetical order
"""
def returnString(s):
    char_dictionary = {}
    max_num = 0
    if s == "":
        raise ValueError("Please input valid string")
    s = s.replace(" ", "")  # Replacing spaces in the string

    for i in range(len(s)):
        if s[i] in char_dictionary:
            char_dictionary[s[i]] += 1
            if char_dictionary[s[i]] > max_num:
                max_num = char_dictionary[s[i]]
                max_char = s[i]
        else:
            char_dictionary[s[i]] = 1
    return max_char

print returnString("abcdcdefg")
