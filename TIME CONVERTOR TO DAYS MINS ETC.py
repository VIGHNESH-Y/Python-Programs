time=float(input("Enter the Value in Seconds"))
hour=time//3600
time%=3600
minutes=time//60
time%=60
seconds=time
print("Hours:Minutes:Seconds---->%dhours:%dminutes:%dseconds"%(hour,minutes,seconds,))
