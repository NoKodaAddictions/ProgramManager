import os
from sys import exit, argv

#delete this if you don't want to run program manager on startup
os.system('copy "{{ PATH TO PROGRAM MANAGER SHORTCUT FILE }}" "C:\\Users\\{{ USER }}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"')

if len(argv) > 1:
    execute = False
    files = os.scandir("{{ PATH TO PROGRAMS FOLDER }}")
    programs = []
    
    for i in files:
        if i.name.endswith((".py",".exe", ".vbs", ".bat")): 
            programs.append(i.name)
    
    if argv[1] == "list":
        for py in range(len(programs)):
            print(f"{py+1}: {programs[py]}")
        exit()

    for py in range(len(programs)):
        if argv[1] == programs[py]:
            os.system(f"py {{PATH TO PROGRAMS FOLDER}}//{argv[1]}")
            execute = True
            break
            
        elif argv[1] == str(py+1):
            os.system(f"py {{PATH TO PROGRAMS FOLDER}}//{programs[py]}")
            execute = True
            break
            
    if execute:
        try:
            if argv[2] == "1":
                pass
            else:
                exit()
        except:
            print("Exiting application...")
            exit()
    else:
        print(f"Program '{argv[1]}' not found")

print("Do you want to run startup?")
y = input("- ")
if y in ("Y","y"):
    print("Running Startup Programs")
    with open("startup_programmanager.txt", 'r') as r:
        startups = r.read().split("\n")
        for startup in startups:
            os.system(f"start {{PATH TO PROGRAMS FOLDER}}//{startup}")

else:
    pass

while True:
    files = os.scandir("{{PATH TO PROGRAMS FOLDER}}")
    programs = []
    a = 1

    for i in files:
        if i.name.endswith((".py",".exe",".bat",".vbs")): 
            programs.append(i.name)
    
    for i in programs:
        print(f"{a}: {i}")
        a += 1
       
    print("Which program do you want to run? (Enter number or file name)")
    print("To exit, type 'exit'")
    print("To clear, type 'cls'")
    print("To restart, type 'restart'")
    print("To create a file, type 'newfile'")
    choose = input("- ")
    if choose == "exit":
        print("Exiting application...")
        exit()
    
    elif choose == "cls":
        os.system("cls")
        
    elif choose == "restart":
        os.system("cls")
        print("Restarting Program Manager...")
        os.system("py {{PATH TO programmanager.py}}")
        exit()
    
    elif choose == "newfile":
        print("Enter file name (specify .py, .bat, or .vbs)")
        name = input("- ")
        if name.endswith((".py",".bat",".vbs")):
            try:
                with open(f"{{PATH TO PROGRAMS FOLDER}}//{name}"):
                    pass
            except:
                os.system(f'fsutil file createnew {{PATH TO PROGRAMS FOLDER}}//{name} 0')
                print(f"{name} created")
            else:
                pass
        else:
            print("Unaccepted file extension")
    
    elif choose.isnumeric():
        try:
            print(f"Starting {programs[int(choose)-1]}...")
            os.system(f"py {{PATH TO PROGRAMS FOLDER}}/{programs[int(choose)-1]}")
        
        except ValueError:
            print("The number is not registered, please choose a registered number")
    else:
        for i in programs:
            if i == choose or i.split(".")[0] == choose.split(".")[0]:
                if i.endswith(".py"):
                    print(f"Starting {i}...")
                    os.system(f"py {{PATH TO PROGRAMS FOLDER}}//{i}")
                    break
                else:
                    os.system(f"start {{PATH TO PROGRAMS FOLDER}}//{i}")
                    break
        
        print("Please enter a valid input")
