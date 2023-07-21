import shutil
import os
from convert import toGB
def show_disk_util():
    path=input("Enter the directory name to find disk utilization: ")
    if os.path.exists(path):
        stat = shutil.disk_usage(path)
        print("Disk usage statistics:")
        print("Total : {} GB".format( toGB(stat.total)))
        print("Used : {} GB".format(toGB(stat.used)))
        print("Free : {} GB".format(toGB(stat.free)))
    else:
        print('%s is not a valid path, please verify' %path)

# display all files with their size


def show_file_usage():
    path=input("Enter the directory name to find disk utilization: ")
    if os.path.exists(path):
        for dirName, subdirs, fileList in os.walk(path):
            for filename in fileList:
                path = os.path.join(dirName, filename)
                if not os.path.exists(path):
                    continue
                filesize = os.path.getsize(path)
                print('{} : {} GB'.format(path, toGB(filesize)))
    else:
        print('%s is not a valid path, please verify' %path)