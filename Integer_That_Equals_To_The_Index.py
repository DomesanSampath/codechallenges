#Integer_That_Equals_To_The_Index
a=int(input('Enter a Array Length:'))
y=[]
for i in range(0,a):
    y.append(int(input('Enter Array Element:')))
for j in range(0,len(y)):
    if y[j]==y.index(y[j]):
        print(y[j])
