#From the Twice Repeated Element Array Finding the Unique Element
#0.For Iteration for Length of Given Array
#1. Each Time Get the No. Of counts of Array Element
#2. Each Time Check for Count==1
#3. If count==1, Get the Number It will be unique
x=input('Enter an Array Elements: Eg. 1,2,3,4::')
x=list(x)
count=0
for j in range(0,len(x)):
    try:
        del(x[x.index(',')])
    except ValueError:
        break;
for j in range(0,len(x)):
    cv=x.count(x[j])
    if cv==1:
        print(x[j])
