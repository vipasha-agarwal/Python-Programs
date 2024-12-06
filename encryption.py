# Write a Python Program to translate a message into secret code language. Use the rule below to translate normal English into secret code language
# Rule: If the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the end and the starting
# else: simply reverse the string
# decoding: if the word contains less than 3 characters, reverse it
# else: remove 3 random characters from starting and end. Now remove the last letter and append it to the beginning
# your program should ask whether you want to code or decode
import random
import string
st=input("enter a message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ") #for encoding coding="true" else "false"
coding = True if (coding=="1") else False
if(coding):#for encoding
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = ''.join((random.choice(string.ascii_lowercase) for x in range(3)))
            r2 = ''.join((random.choice(string.ascii_lowercase) for x in range(3)))
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else: #for decoding
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))