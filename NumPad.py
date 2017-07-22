def allStrings(charArr):
    # print charArr
    # base cases: charArr only has 0 or one element
    if len(charArr) == 0:
        return []
    if len(charArr) == 1:
        return list(charArr[0])

    # find the list of strings
    remaining = allStrings(charArr[1:])
    print remaining
    output = []

    for start_char in charArr[0]:
        # place start_char at the beginning of each string in
        # remaining
        output.extend([start_char + s for s in remaining])
    return output


# uses the earlier function allStrings
def pressingButtons(buttons):
    numPad = ["", "", "abc", "def", "ghi", "jkl",
              "mno", "pqrs", "tuv", "wxyz"]
    charArr = [numPad[int(digit)] for digit in buttons]

    return allStrings(charArr)


if __name__ == '__main__':
    d = pressingButtons("235")
    print d
