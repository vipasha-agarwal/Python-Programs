#Enumeration is used to get the value with index number
marks = [12, 45, 67, 49, 47, 60]
# index = 0
# for mark in marks: 
#     print(mark)
#     if(index == 2):
#         print("Awesome")
#     index+=1

for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index == 2):
        print("Awesome")