#From the Twice Repeated Element Array Finding the Unique Element
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
