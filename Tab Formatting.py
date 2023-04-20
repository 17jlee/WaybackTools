import sys
print("takes a text file of links and removes everything after either a tab or ?")
print("edit file to choose from which to remove")
print("usage: file path to file to read from with tab/?, file path to write to")

file = open(str(sys.argv[1]), "r")
save = open(str(sys.argv[2]), "a")
state = 0
for line in file:
    state += 1
    i = 0
    relevant = 0
    while i < len(line) :
        if relevant == 0 : 
            if line[i] == "?" :
                relevant = i
        i+= 1
    if relevant == 0 :
        save.write(line)

    else :
        save.write(line[0:relevant] + "\n")




