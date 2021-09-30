import os
from sys import exit, argv

if len(argv) > 1:
    files = os.scandir("Programs")
    programs = []
    
    for i in files:
        if i.name.endswith((".py",".exe")): 
            programs.append(i.name)

    for py in programs:
        if argv[1] == py:
            os.system(f"py Programs/{argv[1]}")   
            try:
                if argv[2] == 1:
                    pass
                else:
                    exit()
            except:
                print("Exiting application...")
                exit()
    print(f"Program '{argv[1]}' not found")

while True:
    files = os.scandir("Programs")
    programs = []
    a = 1

    for i in files:
        if i.name.endswith((".py",".exe")): 
            programs.append(i.name)
    
    for i in programs:
        print(f"{a}: {i}")
        a += 1
       
    print("Which program do you want to run? (Enter number)")
    print("To exit, type 'exit'")
    print("To clear, type 'cls'")
    choose = input("- ")
    if choose == "exit":
        print("Exiting application...")
        exit()
    
    elif choose == "cls":
        os.system("cls")
    
    elif choose.isnumeric():
        try:
            print(f"Starting {programs[int(choose)-1]}...")
            os.system(f"py programs/{programs[int(choose)-1]}")
        
        except ValueError:
            print("The number is not registered, please choose a registered number")
    else:
        for i in programs:
            if i == choose:
                print(f"Starting {i}...")
                os.system(f"py programs/{i}")
                break
        print("Please enter a valid input")
