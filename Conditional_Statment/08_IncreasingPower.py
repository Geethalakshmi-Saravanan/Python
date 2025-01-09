"""
Given a positive integer x, the task is to print the numbers from 1 to x
in the order as 12, 22, 32, 42, 52, ... (in increasing order).
"""
def increasingPower(n):
    i = 1
    while i <= n:
        j = i**2
        if j > n:
            break
        print(j, end=" ")
        i = i+1

num = int(input("Enter your number range : "))
increasingPower(num)