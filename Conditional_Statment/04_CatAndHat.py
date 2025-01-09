"""
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.
"""

def cat_hat(s):

    if s.lower().count('cat') == s.lower().count('hat'):
        return True
    else:
        return False

my_input = input("Enter your text: ")
print(cat_hat(my_input))