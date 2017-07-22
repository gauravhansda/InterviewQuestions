import unittest
from math import *
from collections import OrderedDict


class Solution(object):
    def isPrime(self, number):
        # It only needs to go up to the square root of n because if n is divisible by a number
        # greater than its square root then it's divisible by something smaller than it.
        if number < 0:
            raise ValueError("Enter positive number")
        if number == 1:
            return True
        for i in range(2, int(ceil(sqrt(number)))):
            if number % i == 0:
                print "number {} is not prime".format(number)
                return False
        return True

    def Factorial(self, n):
        if n < 0: return -1
        if n == 0: return 1
        return n * self.Factorial(n - 1)

    def fibonacci_nth(self, index):
        if index <= 0: return 0
        if index == 1: return 1
        return self.fibonacci_nth(index - 1) + self.fibonacci_nth(index - 2)

    def permutations(self, word):
        if len(word) <= 1:
            return [word]

        # get all permutations of length N-1
        perms = self.permutations(word[1:])
        char = word[0]
        result = []
        # iterate over all permutations of length N-1
        for perm in perms:
            # insert the character into every possible location
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])
        return result

    # Compress string with duplicate characters with numbers
    def compressString(self, s):
        d1 = OrderedDict()
        new_str = ""
        for i in s:
            if i in d1.keys():
                d1[i] += 1
            else:
                d1[i] = 1
        for k, v in d1.iteritems():
            new_str += k + str(v)
        return new_str

    # Code to Get a Duplicated Number in an Array
    # An array contains n numbers ranging from 0 to n-1. There are some numbers duplicated in the array.
    # It is not clear how many numbers are duplicated or how many times a number gets duplicated.
    # How do you find a duplicated number in the array?
    # For example, if an array of length 7 contains the numbers {2, 3, 1, 0, 2, 5, 3},
    # the implemented function (or method) should return either 2 or 3.
    def findDuplicate(self, numbers):
        length = len(numbers)

        for i in range(length):

            if numbers[i] < 0 or numbers[i] > length - 1:
                raise ValueError("Number out of range")

            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    return numbers[i]
                # swap(numbers[i], numbers[numbers[i]])
                # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp

        return "No Duplicates found"

    # Output a 2d array in spiral order such as [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
    def matrixSpiral(self, mat):
        print("\n".join("\t".join(map(str, row)) for row in mat))

        sp_arr = []

        top = 0
        bottom = len(mat) - 1
        left = 0
        right = len(mat[0]) - 1
        direction = 0

        # range1 = lambda start, end, step: range(start, end + 1, step)
        # print right,left
        # for i in range1(right, left, -1):
        #     print i,
        # print "\nPrinting loop"

        while top <= bottom and left <= right:

            if direction == 0:
                for i in range(left, right + 1, 1):
                    sp_arr.append(mat[top][i])
                top += 1

            elif direction == 1:
                for i in range(top, bottom + 1, 1):
                    sp_arr.append(mat[i][right])
                right -= 1

            elif direction == 2:
                for i in range(right, left - 1, -1):
                    sp_arr.append(mat[bottom][i])
                bottom -= 1

            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    sp_arr.append(mat[i][left])
                left += 1

            direction = (direction + 1) % 4
            # print direction

        for i in sp_arr:
            print i,
        return sp_arr

    # Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    # For example, Given [100, 4, 200, 1, 3, 2],
    # The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = 0
        for i in range(len(nums)):

            if nums[i] - 1 not in s:
                j = nums[i]
                while j in s:
                    j += 1
                ans = max(ans, j - nums[i])
        return ans

    def intToStr(self, number, base):
        base_string = "0123456789ABCDEF"

        if number < base:
            return base_string[number]
        else:
            return self.intToStr(number // base, base) + base_string[number % base]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def testPrimeNumber(self):
        self.assertTrue(self.s.isPrime(17))
        # self.assertRaises(ValueError, self.s.isPrime(-1))
        self.assertFalse(self.s.isPrime(20))

    def testFacorial(self):
        print self.s.Factorial(7)

    def testfibonacci_nth(self):
        print self.s.fibonacci_nth(6)

    def testPermutations(self):
        print self.s.permutations("abc")

    def testcompressString(self):
        print self.s.compressString("aaabbcccccccd")

    def testfindDuplicate(self):
        print self.s.findDuplicate([2, 3, 1, 0, 2, 5, 3])
        print self.s.findDuplicate([0, 0])
        print self.s.findDuplicate([0, 1, 2, 3])

    def testmatrixSpiral(self):
        self.assertEqual(self.s.matrixSpiral(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def testlongestConsecutive(self):
        self.assertEqual(self.s.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    # unittest.TextTestRunner(verbosity=2).run(suite)
