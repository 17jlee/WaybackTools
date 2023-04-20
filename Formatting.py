import os, sys
print("usage: takes raw data files with % sign and ones without and renames them ")
print("usage: raw link text file, edited text file")
print("relevant:",str(sys.argv[1]) )

file = open(str(sys.argv[2]), "r")
link = open(str(sys.argv[1]), "r")
links = []
files = []
for line in file :
    links.append(line[0:-1])

for line in link :
    files.append(line[0:-1])

i = 0
while i < len(links) - 1 :
    if links[i] != links[i + 1] :
        os.system("mv " + "\"" + files[i] + "\"" + " " +  "\"" + links[i] + "\"")
    i += 1

