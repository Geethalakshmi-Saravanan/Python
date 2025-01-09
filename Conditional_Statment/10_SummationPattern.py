"""
Given a natural number n, the task is to write a Python program to first
find the sum of first n natural numbers and then print each step as a pattern.

1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15
"""

num = int(input("Enter your input number - "))

i = 1
while i <= num:
    j = 1
    a = []
    while j <= i:
        print(j, end=" ")
        if j<i:
            print("+", end=" ")
        a.append(j)
        j=j+1
    print("= ", sum(a), end=" ")
    print()
    i=i+1