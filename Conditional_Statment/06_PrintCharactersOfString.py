"""
You are given a string str, you need to print its characters at even indices(index starts at 0).
"""

def stringJumper(s):
    for i in range(0, len(s), 2):
        print(s[i], end="")

text = input("Enter your string : ")
stringJumper(text)