firstword = input("enter the first word:")
secondword = input("enter the second word:")
if set(firstword) == set(secondword):
    print (" both " + firstword +" and " + secondword + " are anagrams ")
else:
    print(" The two strings " + firstword + " and " + secondword + " are not anagrams ")
