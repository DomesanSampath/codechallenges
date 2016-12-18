#Program to Print CamelCase Letter
x=input("Enter String You Need to Convert into Camel Case \n")
x=x.lower()
y=[]
r=''
k=0
#Getting Value in List from String
for i in range(0,len(x)):
    y.append(x[i])
print(y)

#Converting to CamelCase Letter
z=len(y)
while k<z:
    y[0]=y[0].upper()
    if y[k]==' ':
        del(y[k])
        y[k]=y[k].upper()
        z=z-1  #if element gets deleted size reduced by 1
    k=k+1
               

#Printing CamelCase String from List
for j in range(0,len(y)):
    r=r+y[j]
print(r)
