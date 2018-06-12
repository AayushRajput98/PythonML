def is_palindrome(s):
    if s == s[::-1]:
        print("The string '{0}' is a palindrome string".format(s))
    else:
        print("The string '{0}' is not a palindrome string".format(s))

s=input("Enter the string to be checked for palindorme: ")
is_palindrome(s)