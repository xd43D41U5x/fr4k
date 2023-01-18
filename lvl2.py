import lvl2Temp
import importlib
import fileinput
import time
import re

def lvl_2():
    inputfile = input("Please select a file to review: ")
    
    with open(inputfile, 'r') as textfile:
        filetext = textfile.read()
        
    matches = re.findall('function\s\_0x[a-zA-Z0-9]+.+\n\s+return\s\_0x[a-zA-Z0-9]+\(.+',filetext)
    
    #Search for and find the main string shift function before function values are stripped.  
    stringfunvalue = []
    stringshiftfun = re.findall('return\s(\_[a-zA-Z0-9]+)[\s\S]*?(?=parseInt)',filetext)
    if (stringshiftfun != []):
        stringfunvalue.append(stringshiftfun)

    new = []
    importmatch = []
    #Convert JS functions to Python, then strip from orig file.
    for m in matches:
        new.append(m.replace("function","def").replace(" {",":").replace(";",""))
        filetext = filetext.replace(m,"")

    new ="""
{}
""".format("\n".join(new[0:]))


    #Write out new file with no functions.
    outputfile2 = inputfile+".nofunctions.out"
    print("Output file with no functions saved as: %s" % outputfile2)
    with open(outputfile2, 'w') as f:
            f.write(filetext)

    inputfile = outputfile2
    
    fullmatch = []
    stringvalue = []
    whilevalue = []
    breakvalue = []
        
    #Go through the inputfile one line at a time performing regex matching/replace.
    with fileinput.FileInput(inputfile, inplace=False) as file:
        for line in file:
            #Find the full function including the hex chars to convert
            posmatches = re.findall('_0x[a-fA-F0-9]+\s\=\s_0x[a-fA-F0-9]+\s\-\s\([-0xa-zA-Z0-9\s\*\+\)]+',line)
            if (posmatches != []):
                fullmatch.append(posmatches)
            stringmatch = re.findall('\[\'.{200,}\]\;',line)
            if (stringmatch != []):
                stringvalue.append(stringmatch)
            whilematch = re.findall('_0x[a-fA-F0-9]+\s\=\s(.?parseInt.+)\;',line)
            if (whilematch != []):
                whilevalue.append(whilematch)
            stringshiftfun = re.findall('function\s(\_0x[a-fA-F0-9]+)\(.+\s+.+\s+.+\s+\S+\s\=\s\S+\s\-\s0x[a-fA-F0-9]+',line)
        
    
    with open(inputfile, 'r') as breaktest:
        fullfiletext = breaktest.read()
        
    whilebreakmatch = re.findall('shift\'\]\(\)\)\;[\s+\}]+\(\_0x[a-fA-F0-9]+\,\s([0xa-fA-F0-9\-\+\s\*]+)',fullfiletext)
    if (whilebreakmatch != []):
        breakvalue.append(whilebreakmatch)
    
    

    if (len(fullmatch) == 1):
        print("\nOne string pos match found")
        fullmatch = str(fullmatch[0])
        fullmatch = fullmatch.split("(")[1]
        fullmatch = fullmatch.replace("[","").replace("'","").replace("]","").replace(")","")
        stringpos = int(eval(fullmatch))
        print("String POS: %d"% stringpos)
        time.sleep(1)
    else:
        print("\nEither no String POS matches or multiple matches found, check the code and try again")
        time.sleep(1)

    print("\n\n")
    
    if (len(stringvalue) == 1):
        print("One String Array match found")
        stringvalue = str(stringvalue[0]).replace("[","",1).replace('"',"").replace("]","").replace(";","")
        stringvalue = stringvalue+"]"
        print(stringvalue)
        time.sleep(1)
    else:
        print("Either no String Array matches or multiple matches found, check the code and try again")
        time.sleep(1)

    print("\n\n")

    if (len(whilevalue) == 1):
        print("One While Loop ParseInt statement found.")
        whilevalue = str(whilevalue[0]).replace("[","").replace("]","").replace("'","")
        print(whilevalue)
    else:
        print("Either no While Loop matches or multiple matches found, check the code and try again")

    print("\n\n")

    if (len(stringfunvalue) == 1):
        print("One String Function Name found.")
        stringfunvalue = str(stringfunvalue[0]).replace("[","").replace("]","").replace("'","")
        print(stringfunvalue)
    else:
        print("Either no String Function Name matches or multiple matches found, check the code and try again")

    print("\n\n")
    
    if (len(breakvalue) == 1):
        print("One While break value found")
        breakvalue = str(breakvalue[0])
        breakvalue = breakvalue.replace("[","").replace("'","").replace("]","")
        breakvalue = int(eval(breakvalue))
        print("While Break Value: %d"% breakvalue)
        time.sleep(1)
    else:
        print("Either no While Break matches or multiple matches found, check the code and try again")

    print("\n\n")

    
    inputfile2 = "lvl2Temp.py"

    
    finalout2 = []
    #Go through the inputfile one line at a time performing regex matching/replace.
    with fileinput.FileInput(inputfile2, inplace=False) as file:
        for line in file:
            #Find the full function including the hex chars to convert
            line = line.replace("InsertMainStringShiftVar",stringfunvalue)
            line = line.replace("InsertStringValues",stringvalue)
            line = line.replace("InsertWhileLoopValue",whilevalue)
            line = line.replace("InsertPosShift",str(stringpos))
            line = line.replace("InsertWhileBreak",str(breakvalue))
            line = line.replace("InsertInputFile",("'"+str(inputfile)+"'"))
            line = line.replace("InsertFunctionSection",new)
            finalout2.append(line)

    #Write out new file
    outputfile2 = "lvl2Temp.py"
    print("Output file saved as: %s" % outputfile2)
    with open(outputfile2, 'w') as f:
        for final in finalout2:
            f.write(final)
    

    importlib.reload(lvl2Temp)
    lvl2Temp.lvl2Temp()

    return
