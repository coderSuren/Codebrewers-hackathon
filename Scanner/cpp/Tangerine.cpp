
#include<iostream>
#include<fstream>
#include<Windows.h>
#include<string>
#include <openssl/ssl.h>
#include "md5.h"
#include "scan.h"
using namespace std;



string Process::generate_digest(char* location)
{
    string md5;
    md5 = CALL_MD5_Function(location);
    cout << md5 << endl;
    return md5;
}

int main()
{
    cout << "Tangerine Solutions\n";
    wchar_t array[MAX_PATH];
    cout << "enter the location" << endl;
    wcin >> array;
    Scan scanner;
    scanner.ListDirectoryContents(array);
    scanner.hasher();
    scanner.display();
    int stay;
    cin >> stay;
    return 0;
}