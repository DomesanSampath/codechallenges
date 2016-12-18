#Program for Counting of Prime Numbers
x=int(input("Enter Starting No:"))
y=int(input("Enter Ending No:"))
prime=[]
for i in range(x,y+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        prime.append(i)
print("The Prime Numbers Are:",prime)
print("The No. of Prime Numbers:",len(prime))
