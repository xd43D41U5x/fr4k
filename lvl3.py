import lvl3Temp
import importlib
import fileinput
import time
import re

def lvl_3():   
    inputfile = input("Please Enter the File to deob: ")
    print("Processing Input File: %s" % inputfile)
    time.sleep(1)
    fullmatch = []
    stringvalue = []
    whilevalue = []
    breakvalue = []
    arrayOut = {}
    lookupOut = []
    #Go through the inputfile one line at a time performing regex matching/replace.
    with fileinput.FileInput(inputfile, inplace=False) as file:
        #We have to loop through this twice.  The first time to generate the full array lookup.
        print("Finding and createing dict for needed lookups...")
        for line in file:
            #Find the array and convert to dict
            arrayMatch = re.findall('\_0x[\d\w]+\:',line)
            for a in arrayMatch:
                out = line.replace(',','')
                out = out.split(':')
                arrayOut.update({out[0].strip():out[1].strip()})

    with fileinput.FileInput(inputfile, inplace=False) as file:
        for line in file:
            #Fix up any array lookups before other matching.
            midMatch = re.findall('[\w\d]{0,2}\_0x[\w\d]+\.\_0x[\w\d]+',line)
            for m in midMatch:
                temp = m.split('.')[1]
                out = arrayOut[temp]
                line = line.replace(m,out)
            lookupOut.append(line)

    for l in lookupOut:
        #Find the full function including the hex chars to convert
        posmatches = re.findall('_0x[a-fA-F0-9]+\s\=\s_0x[a-fA-F0-9]+\s\-\s(0x[a-fA-F0-9]+)\;',l)
        if (posmatches != []):
            fullmatch.append(posmatches)
        stringmatch = re.findall('\[\'.{150,}\]\;',l)
        if (stringmatch != []):
            stringvalue.append(stringmatch)
        whilematch = re.findall('_0x[a-fA-F0-9]+\s\=\s(.?parseInt.+)\;',l)
        if (whilematch != []):
            whilevalue.append(whilematch)
      
    
    with open(inputfile,'r') as breaktest:
        fullfiletext = breaktest.read()
    


    whilebreakmatch = re.findall('shift\'\]\(\)\)\;\s+\}\s+\}\s+\}\s*\([\w\d]{0,2}\_0x[\w\d]+\,\s([\w\d]+)',fullfiletext)
    if (whilebreakmatch != []):
        breakvalue.append(whilebreakmatch)
    

    if (len(fullmatch) == 1):
        print("\nOne string pos match found")
        fullmatch = str(fullmatch[0])
        fullmatch = fullmatch.replace("[","").replace("'","").replace("]","")
        stringpos = int(fullmatch,16)
        print("String POS: %d"% stringpos)
        time.sleep(1)
    else:
        print("\nEither no String POS matches or multiple matches found, check the code and try again")
        time.sleep(1)

    print("\n\n")
    
    if (len(stringvalue) == 1):
        print("One String Array match found")
        stringvalue = str(stringvalue[0]).replace("[","",1).replace('"',"").replace("]","",1).replace(";","")
        print(stringvalue)
        time.sleep(1)
    else:
        print("Either no String Array matches or multiple matches found, check the code and try again")
        time.sleep(1)

    print("\n\n")

    if (len(whilevalue) == 1):
        print("One While Loop ParseInt statement found.")
        #whilevalue = str(whilevalue[0]).replace("[","").replace("]","").replace("'","")
        stringshiftfun = re.findall('_0x[a-fA-F0-9]+',str(whilevalue))
        stringshiftfun = list(dict.fromkeys(stringshiftfun))
        if (len(stringshiftfun) == 1):
            stringshiftfun = str(stringshiftfun[0]).replace("[","").replace("]","").replace("'","")
        else:
            print("Either no While Loop matches or multiple matches found, check the code and try again")
        print(whilevalue)
        if (type(whilevalue == list)):
            whilevalue = whilevalue[0]
            whilevalue = ''.join(whilevalue)
        time.sleep(1)
        print("\n\n")
        print("String Shift Function found")
        print(stringshiftfun)
        time.sleep(1)
    else:
        print("Either no String Shift matches or multiple matches found, check the code and try again")

    print("\n\n")
    
    if (len(breakvalue) == 1):
        print("One While break value found")
        breakvalue = str(breakvalue[0])
        breakvalue = breakvalue.replace("[","").replace("'","").replace("]","")
        breakvalue = int(breakvalue,16)
        print("While Break Value: %d"% breakvalue)
        time.sleep(1)
    else:
        print("Either no While Break matches or multiple matches found, check the code and try again")

    print("\n\n")

    print("\nWe need to input and confirm a few values: ")
    genPosShift = input(f"The general position shift was identified as {stringpos}, is this correct? (y/n) ")
    if (genPosShift.lower() == "n"): 
        stringpos = input("Please enter the correct value: ")
    
    whileStringPos = input("What is the position shift for the while lookup? ")
    variableStringPos = input("What is the position shift for the main variables? ")


    inputfile2 = "lvl3Temp.py"

    
    finalout2 = []
    #Go through the inputfile one line at a time performing regex matching/replace.
    with fileinput.FileInput(inputfile2, inplace=False) as file:
        for line in file:
            #Find the full function including the hex chars to convert
            line = line.replace("InsertMainStringShiftVar",stringshiftfun)
            line = line.replace("InsertStringValues",stringvalue)
            line = line.replace("InsertWhileLoopValue",whilevalue)
            line = line.replace("InsertGenPosShift",str(stringpos))
            line = line.replace("InsertWhileBreak",str(breakvalue))
            line = line.replace("InsertInputFile",("'"+str(inputfile)+"'"))
            line = line.replace("InsertVariableStringPos",variableStringPos)
            line = line.replace("InsertWhiletringPos",whileStringPos)
            finalout2.append(line)

    #Write out new file
    outputfile2 = "lvl3Temp.py"
    print("Output file saved as: %s" % outputfile2)
    with open(outputfile2, 'w') as f:
        for final in finalout2:
            f.write(final)

    importlib.reload(lvl3Temp)
    lvl3Temp.lvl3Temp()

    return
