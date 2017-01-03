#For Findig Subscript of A Array 1 Presence in Array 2
x=int(input('Enter an Array Size 1:'))
arr1=[]
arr2=[]
count=0
for i in range(0,x):
    arr1.append(int(input('Enter Array Elements:')))
y=int(input('Enter an Array Size 2:'))
for i in range(0,y):
    arr2.append(int(input('Enter Array Elements:')))
for i in range(0,len(arr2)):
    for j in range(0,len(arr1)):
        if (arr2[i]==arr1[j]):
            count=count+1
if count>=len(arr2):
    print('Array 2 is Subscript of Array 1')
else:
    print('Array 2 is not a Subscript of Array 1')
