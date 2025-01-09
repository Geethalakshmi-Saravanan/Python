"""
Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
"""

def decreasingNumbers(n):
    while n >= 0:
        print(n, end=" ")
        n = n - 1

num = int(input("Enter your starting number : "))
decreasingNumbers(num)