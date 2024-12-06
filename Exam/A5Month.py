import operator

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

#a
user_input= input("Enter Name of a month: ")
#user_input = "March"
for key, values in year.items():
     if user_input == key:  #change equality sign to in to answer d
        print( values)
        #break


#b
sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

#c
for keys,values in year.items():
    if int(values) == 31:

      print(keys)

#d
##can sort months by changing itemgetter
# variable to 0
sorted_bymonthdays = dict(sorted(year.items(),key= operator.itemgetter(1)))
print(sorted_bymonthdays)

