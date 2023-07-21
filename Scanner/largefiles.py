import os

def find_files():
    path=input("Enter the directory name to find large files: ")
    if os.path.exists(path):
        for foldername, subfolders, filenames in os.walk(path):
            for filename in filenames:
                size=os.path.getsize(os.path.join(foldername, filename))
                if size>3000000:
                    print(foldername + '\\' + filename + ' : ' + str(size) + ' bytes')
    else:
        print('%s is not a valid path, please verify' %path)