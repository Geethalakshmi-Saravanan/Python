"""
There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry.
You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false
"""

def friends_in_trouble(j_angry, s_angry):
    if j_angry is True and s_angry is True:
        return True
    elif j_angry is False and s_angry is False:
        return True
    else:
        return False


john = bool(input())
smith = bool(input())
print(friends_in_trouble(john, smith))