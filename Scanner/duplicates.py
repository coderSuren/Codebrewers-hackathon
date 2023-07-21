import os
import sys
import hashlib


def find_duplicates(folders):
    dup_size = {}
    for i in folders:
        if os.path.exists(i):
            join_dicts(dup_size, find_duplicate_size(i))
        else:
            print('%s is not a valid path, please verify' %i)
            return {}

    print('Comparing files with the same size...')
    dups = {}
    for dup_list in dup_size.values():
        if len(dup_list) > 1:
            join_dicts(dups, find_duplicate_hash(dup_list))
    print_results(dups)
    return dups


def find_duplicate_size(parent_dir):
    dups = {} # format {size:[filepaths]}
    for dirName, subdirs, fileList in os.walk(parent_dir):
        # print(dirName, subdirs, fileList)
        print('Scanning %s ' % dirName)
        for filename in fileList:
            path = os.path.join(dirName, filename)
            if not os.path.exists(path):
                continue
            filesize = os.path.getsize(path)
            if filesize in dups:
                dups[filesize].append(path)
            else:
                dups[filesize]=[path]
    return dups


def find_duplicate_hash(file_list):
    print('Comparing: ')
    for filename in file_list:
        print('    {}'.format(filename))
    dups = {}
    for path in file_list:
        file_hash = hashfile(path)
        if file_hash in dups:
            dups[file_hash].append(path)
        else:
            dups[file_hash] = [path]
    return dups


def join_dicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize=65536):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()


def print_results(dict1):
    # print(dict1)
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical.')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t{}'.format(subresult))
            print('___________________')

    else:
        print('No duplicate files found.')


def find_duplicates(dir):
    # parser = argparse.ArgumentParser(description='Find duplicate files')
    # parser.add_argument('folders', metavar='dir', type=str, nargs='+',help='A directory to parse for duplicates',)
    # args = parser.parse_args()
    # dir=input("Enter the directory names to find for duplicates: ").split(" ")
    dups = find_duplicates([dir])
    print(dups)
    return dups

def remove_duplicates(dups):
    if len(dups):
        for dup in dups:
            for i in range(1, len(dups[dup])):
                os.remove(dups[dup][i])
        print("Duplicates deleted")
    else:
        print("Duplicates not deleted")
    
    
