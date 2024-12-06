import time

def usingWhile():
    i = 0 
    while i<5000:
        i = i + 1
        print(i)

def usingFor():
    for i in range(5000):
        print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
t2 = time.time() - init
print(t1)
print(t2)

#Sleep method
print("Vipasha")
time.sleep(3)
print("This will run after 3 sec")

#local time method
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)