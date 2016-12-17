#Even, Odd Position of String Swap
y=input("Enter Any String \n")
x=[]
y_length=0

def evn_odd_swap():
    r=''
    #Getting string in list
    for z in range(0,y_length):
        x.append(y[z])

    #Swapping of Even,Odd Places in List
    for i in range(0,len(x),2):
        temp=x[i]
        x[i]=x[i+1]
        x[i+1]=temp

    #Printing String from List
    for j in range(0,len(x)):
        r=r+x[j]
    return(r)

#For the case of Even Lenghthed String
if (len(y)%2==0):
    y_length=len(y)
    print(evn_odd_swap())

#For the case of Odd Lengthed String, The Last Odd Position is remains unchanged
else:
    y_length=len(y)-1
    print(evn_odd_swap()+y[len(y)-1])
