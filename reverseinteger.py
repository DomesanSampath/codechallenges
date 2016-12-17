#Note Python always understands every input as integer :-)
x=input("Enter Integer \n")
y=len(x)-1
z=''
while y>=0:
    z=z+x[y]
    y=y-1
print(z) 
