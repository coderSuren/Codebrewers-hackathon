import os

def find_large_files(path):
    # path=input("Enter the directory name to find large files: ")
    ans=[]
    if os.path.exists(path):
        for foldername, subfolders, filenames in os.walk(path):
            for filename in filenames:
                size=os.path.getsize(os.path.join(foldername, filename))
                if size>100000000: # 100 MB
                    ans.append([foldername + '\\' + filename, size])
                    
        return ans
    else:
        print('%s is not a valid path, please verify' %path)
    