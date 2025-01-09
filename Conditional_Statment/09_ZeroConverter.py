"""
You are given a number n. The number n can be negative or positive.
If n is negative, print numbers from n to 0 by adding 1 to n in the neg function.
If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
"""
def positive(n):
    while n >= 0:
        print(n, end=" ")
        n = n - 1

def negative(n):
    while n <= 0:
        print(n, end=" ")
        n = n + 1

num = int(input("Enter your input (Positive or Negative) : "))

if num > 0:
    positive(num)
elif num < 0:
    negative(num)
else:
    print("Already Zero")