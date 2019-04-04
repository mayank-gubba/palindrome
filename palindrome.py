ori=input("enter a word:")
ori=ori.casefold()
rev=reversed(ori)
if list(ori)==list(rev):
    print("palindrome")
else:
    print("try again")
