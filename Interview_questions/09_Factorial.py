# Below is the Program to find a factorial of a number:

num = int(input("Enter a number: "))
fact = 1
if num<0:
    print("Factorial of Zero is one")
elif num < 0:
    print("Negative number have no factorial")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(f"factorial of {num} is: ", fact)
