import os
dir = input("input a directory: ")
file_all = os.listdir(dir)
for i in file_all:
    if os.popen("[ -z i ]") == 0:
        print(i)