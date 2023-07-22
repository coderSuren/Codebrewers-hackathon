import wmi
import os


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



def convert_bytes(bytes):
   bytes = float(bytes)
   if bytes >= 1099511627776:
      terabytes = bytes / 1099511627776
      size = '%.2fTb' % terabytes
   elif bytes >= 1073741824:
      gigabytes = bytes / 1073741824
      size = '%.2fGb' % gigabytes
   elif bytes >= 1048576:
      megabytes = bytes / 1048576
      size = '%.2fMb' % megabytes
   elif bytes >= 1024:
      kilobytes = bytes / 1024
      size = '%.2fKb' % kilobytes
   else:
      size = '%.2fb' % bytes
   return size

def get_file_usage(dir):
    typesize = {}
    try:
        for root, dirs, files in os.walk(dir):
            for file in files:
                prefix, extension = os.path.splitext(file)
                if extension not in typesize:
                    typesize[extension] = 0
                typesize[extension] += os.stat(root + os.sep + file).st_size
    except KeyboardInterrupt:
        pass
        
    # print(typesize)
    result =list(sorted(typesize.items(), key=lambda x:-x[1]))

    for i in range(len(result)):
        result[i] = [result[i][0], convert_bytes(result[i][1])]

    return result
