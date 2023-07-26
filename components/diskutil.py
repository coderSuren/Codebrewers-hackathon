import wmi
import os
from convert import convert_bytes

def get_disk_usage():
    key = wmi.WMI()
    drive_name = []
    free_space = []
    total_size = []
    
    for drive in key.Win32_LogicalDisk():
        drive_name.append(drive.Caption)
        free_space.append(round(int(drive.FreeSpace)/1e+9, 2))
        total_size.append(round(int(drive.Size)/1e+9, 2))
    return [drive_name, free_space, total_size]




def get_file_usage(dir):
    typesize = {}
    typecount = {}
    try:
        for root, dirs, files in os.walk(dir):
            for file in files:
                prefix, extension = os.path.splitext(file)
                if extension not in typesize:
                    typesize[extension] = 0
                    typecount[extension] = 0
                typesize[extension] += os.stat(root + os.sep + file).st_size
                typecount[extension] += 1
    except KeyboardInterrupt:
        pass
        
    # print(typesize)
    result =list(sorted(typesize.items(), key=lambda x:-x[1]))
    
    for i in range(len(result)):
        result[i] = [result[i][0], convert_bytes(result[i][1]), typecount[result[i][0]]]

    return result
