# Below is the Program to check if the given number is palindrome or not:

n = int(input("Enter a number: "))
temp = n
reverse = 0

while temp>0:
    remainder = temp%10
    reverse = (reverse*10) + remainder
    temp = temp//10

if n == reverse:
    print("it is palindrome number.")
else:
    print("it is not palindrome number.")

