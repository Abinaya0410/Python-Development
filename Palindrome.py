def palindrome(text):
    res = text.lower()
    return res == res[::-1]  

input = input()
if palindrome(input):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
