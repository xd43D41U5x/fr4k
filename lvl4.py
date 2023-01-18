import re

def lvl_4():

    fileres = input("Please select a file to review: ")
    
    with open(fileres, 'r') as textfile:
        filetext = textfile.read()
        
    matchChain = re.findall('function\s\_0x[a-zA-Z0-9]+.+\n\s+return\s\_0x[a-zA-Z0-9]+\(.+',filetext)
    matchRC4 = re.findall('\<\s0x100\;',filetext)
    
    if (matchChain != []):
        print("Possible chained functions found, please review this sample and choose lvl2 if confirmed.")
        print(matchChain[0])
        input("\n\n\nPress Enter to continue...\n\n\n")
        return
    elif (matchRC4 != []):
        print("Possible RC4 functions found, please review this sample and choose lvl3 if confirmed.")
        print(matchRC4[0])
        input("\n\n\nPress Enter to continue...\n\n\n")
        return
    else:
        print("No chained functions or RC4 found, suggest lvl 1 deob")
        input("\n\n\nPress Enter to continue...\n\n\n")
        return