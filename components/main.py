import os
import sys

import duplicates
import largefiles
import diskutil
import infrequent

# create a class file that  imports functions from inported files and returns them in seperate functions

class Scanner:
    def __init__(self):
        super().__init__()

    def find_duplicates(self, folders):
        return duplicates.find_duplicates(folders)

    def remove_duplicates(self, folders):
        return duplicates.remove_duplicates(folders)
    
    def find_large_files(self, folder):
        return largefiles.find_large_files(folder)

    def find_disk_utilization(self):
        return diskutil.get_disk_usage()
    
    def find_file_usage(self, folder):
        return diskutil.get_file_usage(folder)
    
    def show_infrequent_files(self, folder):
        return infrequent.infrequent_files(folder)
    
    def delete_infrequent_files(self, files):
        return infrequent.delete_infrequent_files(files)