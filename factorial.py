#Factorial of A Number
def fact(n):
    temp=1
    for x in range(1,n+1):
        temp=temp*x
    return(temp)
x=int(input("Enter an Integer \n"))
print(fact(x))
