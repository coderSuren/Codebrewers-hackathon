#include<iostream>
#include<conio.h>
#include<Windows.h>
#include<fstream>
#include"scan.h"
using namespace std;

bool Scan::ListDirectoryContents(const wchar_t *sDir)
{
    WIN32_FIND_DATA fdFile;
    HANDLE hFind = NULL;

    wchar_t sPath[2048];

    //Specify a file mask. *.* = We want everything! 
    wsprintf(sPath, L"%s\\*.*", sDir);

    if ((hFind = FindFirstFile(sPath, &fdFile)) == INVALID_HANDLE_VALUE)
    {
        wprintf(L"Path not found: [%s]\n", sDir);
        return false;
    }

    do
    {
        //Find first file will always return "."
        //    and ".." as the first two directories. 
        if (wcscmp(fdFile.cFileName, L".") != 0
            && wcscmp(fdFile.cFileName, L"..") != 0)
        {
            //Build up our file path using the passed in 
            //  [sDir] and the file/foldername we just found: 
            wsprintf(sPath, L"%s\\%s", sDir, fdFile.cFileName);

            //Is the entity a File or Folder? 
            if (fdFile.dwFileAttributes &FILE_ATTRIBUTE_DIRECTORY)
            {
                wprintf(L"Directory: %s\n", sPath);
                ListDirectoryContents(sPath); //Recursion, I love it! 

            }
            else {
                process(sPath);
            }
        }
    } while (FindNextFile(hFind, &fdFile)); //Find the next file. 

    FindClose(hFind); //Always, Always, clean things up! 

    return true;
}


int Process::process(wchar_t* file)
{
    wcout << "\nProcessing: " << file << endl;
    double size = file_size_calculator(file);
    cout << "\n\n Size of the file :" << size << "\n";
    return 0;
}

int Process::file_size_calculator(wchar_t* file)
{
    wcout << "\nComputing the size of " << file<<endl;
    ifstream in;
    in.open(file, ifstream::ate | ifstream::binary);
    double size = in.tellg();
    bool duplicate_size = file_duplication_detector(size, file);
    if (duplicate_size == true)cout << "Files with duplicate sizes have been found" << endl;
    return size;
}


// This memeber function is used to detect files with same sizes
// Note files with same sizes even in bytes is not said to be duplicates!
// It needs to be processed further
bool Process::file_duplication_detector(double size, wchar_t* file)
{
    map<double, wchar_t*>::iterator itr;
    itr = fileduplicates.find(size);
    if (itr != fileduplicates.end())
    {
        // This will create a list of files with same sizes
        list_of_duplicates.push_back(itr->second);
        list_of_duplicates.push_back(file);
        return true;
    }
    else
    {
        fileduplicates[size] = file;
    }
    return false;
}

void Process::hasher()
{
    //Half open and closed iterator implementation!
    // I know there are other ways to do this
    // But half open and closed method is standard for almost all STL stuffs like vector,deque etc.,
    list<wchar_t*>::iterator itr1 = list_of_duplicates.begin();
    list<wchar_t*>::iterator itr2 = list_of_duplicates.end();
    //Common iterator
    // I've heard from someone ++something is faster than something++ for STL iterators
    //I've forgetten why :) you may have the answer for it if yes drop some comments please!
    map<string, wchar_t*>::iterator dupe;
    for (list<wchar_t*>::iterator itr = itr1; itr != itr2; ++itr)
    {
        char hash[MAX_PATH];
        wcstombs(hash, *itr, MAX_PATH);
        string md5 = generate_digest(hash);
        //Create an iterator for map
        dupe = duplicates.find(md5);
        if (dupe != duplicates.end())
        {
            entries.push_back(dupe->second);
            entries.push_back(*itr);
        }
        else
        {
            duplicates[md5] = *itr;
        }
    }
}

void Process::display()
{
    list<wchar_t*>::iterator itr1 = entries.begin();
    list<wchar_t*>::iterator itr2 = entries.end();
    for (list<wchar_t*>::iterator itr = itr1; itr != itr2; ++itr)
    {
        cout << "\n";
        wcout << "=> Duplicates" << *itr << "\n";
    }
}