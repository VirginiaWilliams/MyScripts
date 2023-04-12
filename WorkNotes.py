import subprocess as sp
import sys

if len(sys.argv) > 1:
    fileTitle = sys.argv[1] + " Notes"
else:
    fileTitle = "Temp File Notes"

fileName = fileTitle.replace(" ", "")

f = open(fileName, "a")
f.write(fileTitle + "\n\nScrum:\n\nToDo:\n\nNotes:\n")
f.close()

programName = "notepad.exe"
sp.Popen([programName, fileName])