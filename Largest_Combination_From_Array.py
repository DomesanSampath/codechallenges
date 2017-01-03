#Largest Combination of Array Elements
y=int(input('Enter an Array Length'))
z=[]
for i in range(0,y):
    x=int(input('Enter an Array Element'))
    z.append(x)
z.sort(reverse=True)
dom=''
for i in range(0,len(z)):
    dom=dom+str(z[i])
print(int(dom))
