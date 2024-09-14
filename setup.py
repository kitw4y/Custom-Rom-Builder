import os

stream = os.popen('uname')
output = stream.read()

if output.strip() == "Linux":
    os.system("df -h && lscpu && free -h && whoami && pwd")
    os.system("apt install python curl adb bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5 libncurses5-dev libsdl1.2-dev libssl-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev -y")
    os.system("mkdir -p ~/bin")
    os.system("curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo && chmod a+x ~/bin/repo")
    os.system("PATH='$HOME/bin:$PATH'")
    
else:
    print("Only works on Linux")
