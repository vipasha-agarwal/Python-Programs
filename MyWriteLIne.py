f = open('myFile2.txt','w')
lines = ['line1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()