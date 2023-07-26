import os
from convert import convert_bytes

def find_large_files(path, file_size_limit):
    limit=file_size_limit*1024*1024
    ans=[]
    if os.path.exists(path):
        for foldername, subfolders, filenames in os.walk(path):
            for filename in filenames:
                size=os.path.getsize(os.path.join(foldername, filename))
                if size>limit: 
                    ans.append([foldername + '\\' + filename, convert_bytes(size)])
                    
        return ans
    else:
        print('%s is not a valid path, please verify' %path)
    