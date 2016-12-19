#Program to Find Out Maximum Repeated Character in a Word of a String
x=input("Enter String \n")
igeni=x
y=[]
count=0
z=[]
c=[]
d=[]
length=[]
h=0
fin_str=''
#Getting Value in List from String
for i in range(0,len(x)):
    y.append(x[i])
#Getting Individual Words
for x in range(0,len(y)):
    if y[x]==' ':
        length.append(len(z))
        count=count+1
        for j in range(0,len(z)):
            c.append(z.count(z[j]))
        d.append(max(c))
        z=[]
        continue
    else:
        z.append(y[x])
count=count+1
length.append(len(z))
for j in range(0,len(z)):
    c.append(z.count(z[j]))
    d.append(max(c))
    f=d.index(max(d))
print("The Word Which Contains Highest No of Reepeated Characters",d.index(max(d)))
for z in range(0,length[f]):
    fin_str=fin_str+igeni[z]
print(fin_str)
