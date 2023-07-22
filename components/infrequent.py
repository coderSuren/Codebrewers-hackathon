import glob
import os
import time
from convert import toGB

def infrequent_files(dir): 
    list_of_files = filter( os.path.isfile, glob.glob(dir + '/**/*') )
    list_of_files = sorted( list_of_files, key = os.path.getmtime)

    infrequent_files = []
    for file_path in list_of_files:
        timestamp_str = time.strftime(  '%m/%d/%Y',
                                    time.gmtime(os.path.getmtime(file_path))) 
        file_size = os.path.getsize(file_path)
        infrequent_files.append([file_path,file_size,timestamp_str]) 
    return infrequent_files

def delete_infrequent_files(files): 
    if files:
        for file in files:
            os.remove(file)
        return True
    return False