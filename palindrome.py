def palindrome(s):
    return s == s[::-1]
s=input("ENTER SENTENCE")
sentence=palindrome(s)
if sentence:
    print("is a palindrone")
else:
    print("no is not a palindrone")
        