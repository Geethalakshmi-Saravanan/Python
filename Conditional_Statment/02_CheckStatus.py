"""
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
"""

def check_status(x, y, f):
    if f is False and ((x >= 0 and y < 0) or (x < 0 and y >= 0)):
        return True
    elif (x <= 0) and (y <= 0) and f == True:
        return True
    else:
        return False

a = int(input("a = "))
b = int(input("b = "))
flag = bool(input("flag (T or F) = "))

print(check_status(a, b, flag))