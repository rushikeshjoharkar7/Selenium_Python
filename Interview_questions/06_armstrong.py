n = int(input("enter a number: "))

temp = n
sum = 0

while temp>0:
    digit = temp%10
    sum = sum + digit ** len(str(n))
    temp = temp//10

if n == sum:
    print("Armstrong")
else:
    print("Not a Armstrong")


