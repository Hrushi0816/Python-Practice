a = int(input("Enter the age of first person "))
b = int(input("Enter the age of second person "))
c = int(input("Enter the age of third person "))

if (a > b) and (a > c):
    print(" A is the oldest person")
elif (b > a) and (b > c):
    print(" B is the oldest person")
else:
    print(" c is the oldest person")


if (a < b) and (a < c):
    print(" A is the youngest person")
elif (b <a) and (b < c):
    print(" B is the youngest person")
else:
    print(" C is the youngest person")
