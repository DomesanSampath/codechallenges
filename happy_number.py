#Program Will Return Number:Is Happy Number, if not so, It will return Nothing
#It neglects 1 not as a Happy Number,by raising ValueError
x=int(input("Enter an Integer:"))
if x==1:
    raise ValueError("1 Is Not a Happy Number")
y=x
z=0
i=0
#If digit is a Single_Digit Number
def single_digit(k):
    new_digit=pow(k,2)
    return(new_digit)
#If digit is a Double_Digit Number
def  two_digit(j):
              p=j%10
              q=int((j-p)/10)
              new_digit=pow(p,2)+pow(q,2)
              return(new_digit)
#If digit is a Three_Digit Number
def three_digit(k):
              p=k%10
              k=k-p
              q=(k%100)/10
              k=k-(k%100)
              r=(k%1000)/100
              new_digit=int(pow(p,2))+int(pow(q,2))+int(pow(r,2))
              return(new_digit)
#Loop to find out Happy_Number            
while True:
    if x==1:
        print(y,": Is Happy Number")
        break
    elif 1<x<10:
        x=single_digit(x)
    elif 9<x<100:
        x=two_digit(x)
    elif 99<x<1000:
        x=three_digit(x)
