# Here is the Program to find if the given number is prime or not:

n = int(input("enter a number: "))
flag = False
if n>1:
    for i in range(2,n):
        if n%i == 0:
            flag = True

            break

if flag:
    print("It is not a prime number.")
else:
    print("it is a prime number")