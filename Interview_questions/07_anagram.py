# Here is the Program to check if the given strings are anagram or not:

def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("anagram string")
    else:
        print("Not a anagram string")

string1 = str(input("Enter a string: "))
string2 = str(input("Enter second string: "))

anagram(string1,string2)