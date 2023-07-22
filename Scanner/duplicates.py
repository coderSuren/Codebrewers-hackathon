import os
import sys
# import 5 hash functions from hashlib
import timeit
from hashlib import md5, sha1, blake2b
from xxhash import xxh64, xxh128

hashfunc = 0
import_module = "import random"

def duplicates(folders):
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


def find_duplicate_size(parent_dir):
    dups = {} # format {size:[filepaths]}
    for dirName, subdirs, fileList in os.walk(parent_dir):
        print(dirName, subdirs, fileList)
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

    hasher = md5()
    # use switch case for  hash functions
    match hashfunc:
        case 0:  
            hasher = md5()
        case 1:
            hasher =  sha1()
        case 2:
            hasher= blake2b()
        case 3:
            hasher= xxh64()
        case 4:
            hasher= xxh128()
        case _:
            print("Invalid hash function")
            sys.exit(1)

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
    a= duplicates([dir])
    return a

def remove_duplicates(dups):
    if len(dups):
        for dup in dups:
            for i in range(1, len(dups[dup])):
                os.remove(dups[dup][i])
        print("Duplicates deleted")
        return True
    else:
        print("Duplicates not deleted")
        return False
    
def main():
    # dir=input("Enter the directory names to find for duplicates: ").split(" ")
    dir = "D:\\GitHub\\codebrewers-hackathon"
    dir2 = "D:\\GitHub\\climateview"
    dir3 = "D:\\GitHub\\js-samples"
    dir4 = "D:\\GitHub\\MemoryGrid"
    dir5 = "D:\\GitHub\\portfolio"
    results=[]
    for i in range(5):
        print("Hash function", i ,"is being used")
        hashfunc = i
        starttime = timeit.default_timer()
        find_duplicates(dir)
        find_duplicates(dir2)
        find_duplicates(dir3)
        find_duplicates(dir4)
        find_duplicates(dir5)
        results.append(timeit.default_timer()-starttime)
    print("\nTime taken for 5 hash functions: ")
    print("md5: ", results[0], " seconds") 
    print("sha1: ", results[1], " seconds")
    print("blake2b: ", results[2], " seconds")
    print("xxh64: ", results[3], " seconds")
    print("xxh128: ", results[4], " seconds")


if __name__ == '__main__':
    main()
