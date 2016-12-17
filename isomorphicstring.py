#Set identifies a unique characters,
#if strings are isomorphic then count of distinct characters will be the same
a=input("Enter a String 1 \n")
b=input("Enter a String 2 \n")
c=set(a)
d=set(b)
if len(c)==len(d):
    print("true")
else:
    print("false")
