import shutil
import lvl1
import lvl2
import lvl3
import lvl4
import sys
import os

def cleanup(tempName):
    print("Performing template cleanup and restoring a fresh copy...")
    currentPath = os.path.dirname(__file__)
    src = "templates//" + tempName
    dst = tempName
    shutil.copy(src,dst)
    input("\n\n\nPress Enter to continue...\n\n\n")

def main_menu():

    while True:
        os.system("clear")
        fr4k = ("""
____ ____       _  _ 
|___ |__/ /__|  |_/  
|    |  \    |  | \_        
        """)
        print(f"\nWelcome to: {fr4k} \nThe obfuscator.io deob tool.\nVersion 2.0")
        print("Brought to you by: ")
        print("""
 ______        ____  ______            _     _ _______
 |     \ /__|_ ____| |     \ /__|  /|  |     | |______
 |_____/    |  ____| |_____/    |  _|_ |_____| ______|
             """)
        print("\n")
        print("1. Level 1 Deob - (Default/Low)")
        print("2. Level 2 Deob - (Chained Functions)")
        print("3. Level 3 Deob - RC4/Array lookups")
        print("4. Analyze File for possible level")
        print("5. Exit")
        userinput = input("\nSelect Option: ")

        if userinput == "1":
            print("Starting Level 1 Deob")
            lvl1.lvl_1()
            cleanup('lvl1Temp.py')
        elif userinput == "2":
            print("Starting Level 2 Deob")
            lvl2.lvl_2()
            cleanup('lvl2Temp.py')
        elif userinput == "3":
            print("Starting Analysis of File")
            lvl3.lvl_3()
            cleanup('lvl3Temp.py')
        elif userinput == "4":
            print("Starting Analysis of File")
            lvl4.lvl_4()
        elif userinput == "5":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid Selection, try again")
        
main_menu()
