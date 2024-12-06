with open('myFile3.txt','r') as f:
    print(type(f))
    #Move to the 10th Byte in the File
    f.seek(10)
    # Read the next 8 bytes
    print(f.tell())#to find the current position in file
    data = f.read(8)
    print(data)


with open('myFile4.txt', 'w') as f:
    f.write('Hello, World!')  # overwrite the file
    f.truncate(5)

with open('myFile4.txt', 'r') as f:
    print(f.read(5))  # read the first 5 characters