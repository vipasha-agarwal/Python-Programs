import sys
length_cm = eval(input("Enter Lenth in Centimeters: "))
if length_cm < 0:
    print("You Have Entered an Invalid Number")
    sys.exit()
else:
    length_inches = length_cm / 2.54
    print(length_inches," inches")    

