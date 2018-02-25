import os,platform
import subprocess
from heapq import *

h=[]
n=[]
byteToMB=0.00000095367432

directory=[]
if(platform.system()=='Windows'):
    driveStr = subprocess.check_output("fsutil fsinfo drives")
    drives = driveStr.split()
    totalDrives=len(drives)
    for i in range(totalDrives):
        directory.append(drives[i])

def topTenFiles(size,filename):
    if (len(h) == 10 and size > h[0]):
        heapreplace(h, size)
        heapreplace(n, filename)
    if (len(h) < 10):
        heappush(h, size)
        heappush(n, filename)

def walkThroughSystem():
    skip=0
    #linux
    global directory
    if(platform.system()=='Linux'):
        directory=['/']
        start=0
    #Windows
    else:
        start=1
    for i in range(start,len(directory)):
            for root, directories, filenames in os.walk(directory[i]):
                for filename in filenames:
                    print(filename)
                    fileSource=os.path.join(root,filename)
                    try:
                        statinfo=os.path.getsize(fileSource)*byteToMB
                        topTenFiles(round(statinfo,3),filename)
                    except (os.error):
                        print("Acces Denied")
                    except(ValueError):
                        skip=skip+1

    print("\nResults---")
    print("Top Ten Large files are: (small to large)")
    for i in range(10):
        print(heappop(n),end="  ")
        print(str(heappop(h))+" MB")

