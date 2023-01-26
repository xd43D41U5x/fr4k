from urllib.parse import unquote
import fileinput
import base64
import js2py
import time
import re

def lvl3Temp():
    #Function to mimic JS parseint.  Will check for string starting with an int.
    #If its a char, returns "nan", otherwise strips only decimal chars and converts.
    def parseInt(stringinput):
        try:
            int(stringinput[0])
        except:
            return "NaN"
        intnum = int(re.search(r'\d+', stringinput).group())
        return intnum

    #Function to mimic a push/shift in JS.  Takes string from array on the front and moves to the back.
    def shift(listinput):
        listinput.append(listinput.pop(0))

    #While function helper/mid lookup
    def MainStringShift(start,key):
        #Attempt to handle reverse order of supplied values.
        if not isinstance(start,int):
            start,key = key,start
        data = StringValues[start-genPosShift-whilePosShift]
        decodedVal = bDecode(data)
        decValue = rc4Decrypt(decodedVal,key)
        return decValue

    #While function helper/mid lookup
    def valueStringShift(start,key):
        #Attempt to handle reverse order of supplied values.
        if not isinstance(start,int):
            start,key = key,start
        data = StringValues[start+varPosShift-genPosShift]
        decodedVal = bDecode(data)
        decValue = rc4Decrypt(decodedVal,key)
        return decValue

    def bDecode(inputString):
        #Note, as much as I tried and wanted to do this in pure Python vs using js2py, I could only get it to about 95%.
        #The related function is being left in below the eval in case it can be leveraged later.
        #The issue stems from the way JS handles null and zero values in the return in fromCharCode.
        #Also, I left it returning percent separated hex values instead of possible non-printable chars
        #However, that could be changed if needed.
        #Lastly, I guess this makes more sense in that if the decode function is ever updated, its a quick swap here
        #vs taking the time to translate it.
        jsDecode = js2py.eval_js("""function (_0x45ca97) {
                var _0x5ed0c2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';
                var _0x64f838 = '',
                _0x5c3ae7 = '';
                for (var _0x3822e8 = 0x0, _0x4c3f5f, _0x16b81a, _0x3ec3d2 = 0x0; _0x16b81a = _0x45ca97['charAt'](_0x3ec3d2++); ~_0x16b81a && (_0x4c3f5f = _0x3822e8 % 0x4 ? _0x4c3f5f * 0x40 + _0x16b81a : _0x16b81a, _0x3822e8++ % 0x4) ? _0x64f838 += String['fromCharCode'](0xff & _0x4c3f5f >> (-0x2 * _0x3822e8 & 0x6)) : 0x0) {
                    _0x16b81a = _0x5ed0c2['indexOf'](_0x16b81a);
                }
                for (var _0x32f9ed = 0x0, _0x27dd7c = _0x64f838['length']; _0x32f9ed < _0x27dd7c; _0x32f9ed++) {
                    _0x5c3ae7 += '%' + ('00' + _0x64f838['charCodeAt'](_0x32f9ed)['toString'](0x10))['slice'](-0x2);
                }
                return _0x5c3ae7
            }
        """)
        

        '''
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='
        output = finalOut = temp = ''
        countPOS = loopCount = 0

        for i in inputString:
            currentChar = letters.index(i)
            temp = temp * 0x40 + currentChar if loopCount % 0x4 else currentChar
            loopCount += 1 %4
            new = 0xff & temp >> (-0x2 * loopCount & 0x6) if ~currentChar and temp else 0 
            new = chr(new)
            new = "" if new == '\x00' else new
            output += new

        hexOut = ''

        #Mimic conversion to url/hex
        for x in output:
            hexOut += '%' + ('00' + f'{ord(x):x}')[-2:];
        
        finalDecOut = unquote(hexOut, encoding='utf-8', errors='ignore')
'''
        hexOut = jsDecode(inputString)
        #Mimic decodeuricomponent
        
        finalDecOut = unquote(hexOut, encoding='utf-8', errors='ignore')
        return finalDecOut

    #Simple RC4 decrypt function
    def rc4Decrypt(data,key):  
        S = list(range(256))
        j = 0
        out = []
        #KSA Phase
        for i in range(256):
            j = (j + S[i] + ord( key[i % len(key)] )) % 256
            S[i] , S[j] = S[j] , S[i]
        #PRGA Phase
        i = j = 0
        for char in data:
            i = ( i + 1 ) % 256
            j = ( j + S[i] ) % 256
            S[i] , S[j] = S[j] , S[i]
            out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
        return ''.join(out)


    #Values Created from main script.
    inputfile = InsertInputFile
    genPosShift = InsertGenPosShift
    varPosShift = InsertVariableStringPos
    whilePosShift = InsertWhiletringPos
    Whilebreak = InsertWhileBreak
    InsertMainStringShiftVar = MainStringShift
    StringValues = InsertStringValues


    if StringValues and Whilebreak and genPosShift and inputfile:
        print("\n[*] - Key values found, proceeding...")
    else:
        print("\n[*] - Missing key values, exit...")
        exit

        
    print("\n[*] - Starting string shift while loop...")
    count = 0


    while True:
        try:
            count += 1
            ###Only update the "tryfun" variable with the math seen in your code example.
            tryfun = InsertWhileLoopValue
            if (tryfun == int(Whilebreak)):
                break
            else:
                shift(StringValues)
        except:
            shift(StringValues)


    ###End User value input section, do not change anything outside of this section.
    ########################


    print(f'\n[*] - String while loop exited after shifting {count-1} times.')
        
    finalout = []

    print(f'\n[*] - Parsing the input file {inputfile}.')
    print("\n[*] - Performing stacked string lookups...")
    print("\n[*] - Performing general file cleanup...")
    #Go through the inputfile one line at a time performing regex matching/replace.
    with fileinput.FileInput(inputfile, inplace=False) as file:
        for line in file:
            if ("parseint" not in line.lower()):
                #Find all string lookups and decrypt
                decMatch = re.findall('[\w\d]{0,2}\_0x[\w\d]+\([^\_]{4,6}\,\s?.{4,6}',line)
                for d in decMatch:
                    funValue = d.split("(",1)
                    decValues = funValue[1].split(',')
                    decInt = 0
                    decStr = ''
                    for dec in decValues:
                        dec = dec.strip().strip("'")
                        try:
                            decInt = int(dec,16)
                        except:
                            decStr = dec   
                    decodeVal = valueStringShift(decInt,decStr)
                    line = line.replace(funValue[0], '')
                    line = line.replace(funValue[1],decodeVal)
                #Find the full function including the hex chars to convert (cleanup)
                fullmatch = re.findall('_0x[a-zA-Z0-9]+\(0x[a-zA-Z0-9]+',line)
                #Find the left over null/not used functions (cleanup)
                nullfun = re.findall('var\s\_0x[a-zA-Z0-9]+\s\=\s\_0x[a-zA-Z0-9]+\;',line)
                for f in fullmatch:
                    stripfull = f.replace('[','').replace("'",'')
                    stripfull = stripfull.split("(",1)[0]
                    line = line.replace(stripfull,"")
                for n in nullfun:
                    line = line.replace(n,"")
                #Look for any left over hex values (actual nums) and convert.
                hexconvert = re.findall('[\ |\']0x[a-fA-F0-9]+',line)
                for hc in hexconvert:
                    hc = hc.replace(" ","").replace("'","")
                    if (isinstance(hc, str)):
                        hcn = str(int(hc,16))
                    else:
                        hcn = str(int(hc))
                    line = line.replace(hc,hcn)
                finalout.append(line)

    print("\n[*] - Decode finished!")

    #Write out new file
    outputfile = inputfile+".out"
    with open(outputfile, 'w') as f:
        for final in finalout:
            f.write(final)
    print(f'\n[*] - Output file saved as: {outputfile}.')  
