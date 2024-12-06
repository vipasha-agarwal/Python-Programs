import time
tim=time.strftime('%H:%M:%S')
print(tim)
tim=time.strftime('%H')
print(tim)

tim=int(time.strftime("%H"))
if tim in range(0,12):  #if(tim>=0 and tim<12):
    print('Good Morning')
elif tim in range(12,17):  #elif(tim>=12 and tim<17):
    print('Good Afternoon')
elif tim in range(17,19):  #if(tim>=17 and tim<0):
    print('Good Evening')    #print('good night')
else:
    print('Good Night')