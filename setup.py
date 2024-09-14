import os

stream = os.popen('uname')
output = stream.read()

if output.strip() == "Linux":
    os.system("rm -rf ro && ls")
    
    gitName = str(input("Enter your git User Name : "))
    gitEmail = str(input("Enter your git Email : "))

    os.system("git config --global user.name '{}'".format(gitName))
    os.system("git config --global user.email '{}'".format(gitEmail))

    print("")
    os.system("python3 main.py")
    
else:
    print("Only works on Linux")
