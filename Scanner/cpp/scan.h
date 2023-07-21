#pragma once

#include<iostream>
#include<string>
#include<map>
#include<list>
using namespace std;

// Processing the files


class Process
{
private:
    map<double, wchar_t*> fileduplicates;
    list<wchar_t*> list_of_duplicates;
    map<string, wchar_t*>hashes;
    map<string, wchar_t*>duplicates;
    list<wchar_t*> entries;
public:
    string generate_digest(char* location);
    int process(wchar_t* file);
    int file_size_calculator(wchar_t* file);
    bool file_duplication_detector(double size, wchar_t* location);
    void hasher();
    void display();
};

class Scan:public Process
{
public:
    bool ListDirectoryContents(const wchar_t *sDir);
};