#Sum_Of_Array_Pairs_Closeset_Zero
x=int(input('Enter an Array Size:'))
arr1=[]
count=0
c_sum=0
o_sum=0
y=[]
z=[]
for i in range(0,x):
    arr1.append(int(input('Enter Array Elements:')))
for j in range(0,x):
    c_sum=0;
    for k in range(j+1,x):
        c_sum=arr1[j]+arr1[k]
        if c_sum==0 or c_sum in range(0,2):
            y.append(c_sum)
            z.append((arr1[j],arr1[k]))
print(min(z))
