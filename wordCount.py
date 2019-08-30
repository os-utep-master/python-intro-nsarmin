import sys
import re
import os
import subprocess

#outputframe=sys.argv[1]
#with open (outputframe, "r") as outputfile:
if len(sys.argv) is not 3:
    print("usage: wordCount.py <input> <output>")
    exit()

inputName=sys.argv[1]
outputName=sys.argv[2]
words={}
if not os.path.exists(outputName):
    print("output %s file doesn't exist" % outputName)
    exit()

with open(inputName, 'r') as input:
    for line in input:
        line=re.sub('[^A-Za-z]+',' ', line).lower()
        line=line.split(' ')
        for word in line:
            if word in words:
                words[word]+=1
            else:
                words[word]=1
words.pop('')
output=open(outputName, 'a+')
for key in sorted(words):
    output.write(key+ ' ' + str(words[key]) + "\n")
output.close()

