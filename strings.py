a='''I am Vipasha
and I am pursuing MCA from VIT Bhopal
I am 20 Year old'''
print(a)
print(a[0])
print(a[6])
x='he said "he was fine"'
print(x)
x="He said \"He was fine"
print(x)
for character in x:
    print(character)
print(len(a))#len function
print(a[5:9])#slicing
print(x[:-6])
print(x[-4:-2])
# As string is immutable so there function create another as same the original string with changes 
print(x.upper())#for change in upper case
print(x.lower())#for change in lower case
z="...vip........."
y='introduction TO Python'
print(z)
print(z.rstrip("."))#stripping the tailing part only 
print(z.replace('vip','vipasha'))#change all the occurences
print(z.split('p'))
print(y.capitalize())
print(y.center(50))
print(a.count('I'))
#g=int (input("Enter a number"))
#g = ""
#print(int(g))
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
set1 ={10,3,5,7,3,99,-6}
print(set1)
set2 ={3,5,88}
print(set2)

set3 = set1.intersection(set2)
print(set3)

  