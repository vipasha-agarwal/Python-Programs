f = open('myFile.txt', 'a')
print(f)
text = f.write(" rajasthan")
print(text)
f.close()
# if we use write method on existing text file then it will overwrite the old content
f = open('myFile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()