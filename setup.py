import os

stream = os.popen('uname')
output = stream.read()

if output.strip() == "Linux":
    os.system("mkdir ro && cd ro")
    os.system("mkdir -p ~/bin")
    os.system("curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo && chmod a+x ~/bin/repo")
    os.system("PATH='$HOME/bin:$PATH'")
    os.system("repo init -u https://github.com/RisingTechOSS/android -b fourteen --git-lfs && repo sync -c --no-clone-bundle --optimized-fetch --prune --force-sync -j$(nproc --all)")

    gitName = str(input("Enter your git User Name : "))
    gitEmail = str(input("Enter your git Email : "))

    os.system("git config --global user.name '{}'".format(gitName))
    os.system("git config --global user.email '{}'".format(gitEmail))

    print("")
    os.system("python3 main.py")
    
else:
    print("Only works on Linux")
