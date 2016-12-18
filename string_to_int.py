#String to Integer Conversion
x=input("Enter a String:")
y=[]
count=0
for i in range(0,len(x)):
    y.append(x[i])
for j in range(0,len(y)):
    count=+ord(y[j])
print(count)
