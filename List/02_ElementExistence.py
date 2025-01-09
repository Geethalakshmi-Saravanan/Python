my_list = [11, 122, 33, 44, 505, 60]

num = int(input("Enter the number to be check existence : "))

if num in my_list:
    print(f"{num} is present in the list")
else:
    print(f"{num} is not present in the list")