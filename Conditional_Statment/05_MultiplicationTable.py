def multiplication_Table(n):
    print(f"Multiples of {n} is ")
    for i in range(1, 11):
        print(i*n, end=" ")

num = int(input("Enter a number : "))
multiplication_Table(num)