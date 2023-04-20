import os, sys
print("downloads all wayback links in a file")
print("usage: path to text file of wayback links")
file = open(str(sys.argv[1]), "r")
for line in file :
    command = "wayback_machine_downloader -e \"" + (line[0:-1] + "\"")
    os.system(command)
