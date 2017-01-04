x=input('Enter a Number')
y=[]
for i in range(0,len(x)):
  y.append(x[i])
y.sort()
dom=''
for i in range(0,len(y)+1):
  del(y[0])
  for j in range(0,len(y)):
    dom=dom+y[j]
    print('After Deleting %d Digit: %d'(%i,%int(dom)))
