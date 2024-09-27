def isPalindrome( s):
    newString =''
    for i in s:
        if i.isalpha():
                #newString = ''.join(i.lower()) #''.join(i.lower()) is problematic. The join() method expects an iterable (like a list or string), but you’re passing a single character i
            newString += i.lower()

    return newString == newString[::-1]
    
string = input("Enter the string: ")
if isPalindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
