x=input("Enter Time  I in HH:MM:SS:")
z=input("Enter Time II in HH:MM:SS:")
#function to convert entire time into seconds
def mytime(k):
      y=[]
      #Getting Value in List from Time Input
      for i in range(0,len(k)):
          y.append(k[i])
      hours=int(y[0]+y[1])
      if hours>24:
          raise ValueError("Invalid Time-Exceeding 24 Hours")
      mins=int(y[3]+y[4])
      if mins>60:
          raise ValueError("Invalid Time-Mins Exceeeding 60")
      secs=int(y[6]+y[7])
      if secs>60:
          raise ValueError("Invalid Time-Secs Exceeding 60")
      tsecs=0
      tsecs=((hours*60*60)+(mins*60)+(secs))
      return(tsecs)
x=mytime(x)
z=mytime(z)
if x>z:
    time_dif_secs=x-z
else:
    time_dif_secs=z-x
print("Time Difference in Mins:",(int(time_dif_secs/60)))
