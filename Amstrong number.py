#Armstrong Number
a = int(input("Enter the  number : "))

def armstrong(a):
    n = a
    sum = 0
    while n > 0:
        d = n % 10
        sum = sum  + d ** 3
        n = n // 10

    if sum == a:
        print("It is a armstrong number")
    else:
        print("It is not  a armstrong number")

armstrong(a)