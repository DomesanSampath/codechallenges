#String to Integer Conversion
x=input("Enter a String:")
y=[]
count=0
#Getting String in List
for i in range(0,len(x)):
    y.append(x[i])
#Printing ASCII or INT value for each character
for j in range(0,len(y)):
    count=count+ord(y[j])
print(count)
