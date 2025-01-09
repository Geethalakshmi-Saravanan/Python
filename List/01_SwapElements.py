"""
Given a list, write a Python program to swap the first and last element of the list using Python
"""

my_list = [11, 22, 33, 44, 55]

print("List before swapping - ", my_list)

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print("List after swapping - ", my_list)