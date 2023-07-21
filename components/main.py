import os
import sys

# import python modules from 'files' folder in current directory

from . import duplicates as duplicates

# import Scanner.duplicates as duplicates
# import Scanner.diskutil as diskutil
# import Scanner.largefiles as largefiles


# create a class file that  imports functions from inported files and returns them in seperate functions

class Scanner:
    def __init__(self):
        super().__init__()

    def find_duplicates(self, folders):
        return duplicates.find_duplicates(folders)

    def remove_duplicates(self, folders):
        return duplicates.remove_duplicates(folders)
    
    # def find_large_files(self, folder, min_size):
    #     return largefiles.find_files(folder, min_size)

    # def find_disk_utilization(self, folder):
    #     return diskutil.show_disk_util(folder)
    