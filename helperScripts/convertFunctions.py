#Helper function to find and convert (from js to python) all chained funtions that would be needed if you had to manually create parts of the script.  
#This does not run as part of fr4k but ad-hoc only

import re

inputfile = 'input.txt'
    
with open(inputfile, 'r') as textfile:
    filetext = textfile.read()
        
matches = re.findall('function\s\_0x[a-zA-Z0-9]+.+\n\s+return\s\_0x[a-zA-Z0-9]+\(.+',filetext)
out = []
for m in matches:
    out.append(m.replace("function","def").replace(" {",":").replace(";",""))


for o in out:
    print(o)
