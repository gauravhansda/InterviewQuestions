'''
Fibonacci sequence generator
0 1 1 2 3 5 8
Print fibonacci list till n
'''
import sys


# def fib(n):
# seq = []
# n0, n1 = 0, 1
# count = 2
# assert n > 0
# if n == 1:
#     return [n0]
# if n == 2:
#     return [n0, n1]
#
# seq = [n0, n1]
# print "Fibonacci Sequence: "
# while count < n:
#     nth = n0 + n1
#     seq.append(nth)
#     n0 = n1
#     n1 = nth
#     count += 1
# return seq
## Example 2: Using recursion
def fibR(n):
    if n == 1 or n == 2:
        return 1
    return fibR(n - 1) + fibR(n - 2)


print fibR(5)


def fib(n):
    a, b = 1, 1
    seq = [a]
    if n == 1:
        return a, seq
    for i in range(n - 1):
        a, b = b, a + b
        seq.append(a)

    return a, seq


def fibMem(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]


def main():
    try:
        terms = int(raw_input("enter the number of terms: "))
        nth_term, fib_seq = fibMem(fib, terms)
        print "fib_seq:{}".format(fib_seq)
        print "{}th term:{}".format(terms, nth_term)
    except ValueError:
        sys.exit('Only positive real numbers are accepted')


if __name__ == '__main__':
    main()
