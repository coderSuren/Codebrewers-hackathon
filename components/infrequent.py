import glob
import os
import time
from convert import convert_bytes
def infrequent_files(dir, days): 
    today = time.strftime('%m/%d/%Y', time.gmtime())
    list_of_files = filter( os.path.isfile, glob.glob(dir + '/**/*') )
    list_of_files = sorted( list_of_files, key = os.path.getatime)
    infrequent_files = []
    for file_path in list_of_files:
        timestamp_str = time.strftime(  '%m/%d/%Y', time.gmtime(os.path.getatime(file_path))) 
        if compare_dates(timestamp_str, today, days):    
            file_size = os.path.getsize(file_path)
            infrequent_files.append([file_path,convert_bytes(file_size),timestamp_str]) 
    return infrequent_files

def compare_dates(date1, date2, days):
    date1 = time.strptime(date1, '%m/%d/%Y')
    date2 = time.strptime(date2, '%m/%d/%Y')
    difference = time.mktime(date2) - time.mktime(date1)
    difference = difference / (24 * 60 * 60)
    if difference > days:
        return True
    return False

def delete_infrequent_files(files): 
    if files:
        for file in files:
            os.remove(file)
        return True
    return False