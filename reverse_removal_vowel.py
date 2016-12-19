#Program for Reversing and Removal of String
x=input("Enter String:")
y=len(x)-1
z=''
fin_str=''
f=[]
#Reversing the String
while y>=0:
    z=z+x[y]
    y=y-1
#Reversed String in a List for Easy Manipulation
for i in range(0,len(z)):
    f.append(z[i])
vowel=['a','e','i','o','u','A','E','I','O','U']
print(vowel)
#deleting vowels from string, and Printing the String
count=len(f)
g=0
while g<count:
    for j in range(0,len(vowel)):
        if vowel[j]==f[g]:
            del(f[g])
            count=count-1
    fin_str=fin_str+f[g]
    g=g+1
print(fin_str)
