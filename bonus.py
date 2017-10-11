from __future__ import print_function
import os, sys, glob, subprocess




print("Total Tracks: ",end='')
sys.stdout.flush()
subprocess.call('find . -type f | grep ogg | wc -l',shell=True)

print("\nTotal Artists: ",end='')
sys.stdout.flush()
subprocess.call("find . -type f | grep ogg | cut -f3 -d '/' | sort -u | wc -l",shell=True)

print("\n")

path = "."


martists = []
malbums = []

print("Multi-Disk Albums: ")

for root, dirs, files in os.walk("."):
    for name in files:
        #os.path.join(root, name) #root prints path, name is actual song name.
        songPath = root.split('/')
        if len(songPath) > 4:
            if not songPath[2] in martists:
                martists.append(songPath[2])
                malbums.append(songPath[3])
            else:
                temp = martists.index(songPath[2])
                malbums[temp] + '\n' + songPath[3]
        else:
            continue
for i, j in zip(martists,malbums):
   # print(i,"\n" + "   " + j)
	print(i)
	print("   " + j)

   # for name in dirs1:
   #     print(os.path.join(root, name))
