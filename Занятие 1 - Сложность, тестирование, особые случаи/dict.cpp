#include <iostream>
#include <map>
using namespace std;


int main() {

    int is_leap;

    is_leap = 2;

    map <string,int> month = {  // словарь, объявлять значения через функцию
            {"January", 31},
            {"February", 28 + is_leap},
            {"March", 31},
            {"April", 30},
            {"May", 31},
            {"June", 30},
            {"July", 31},
            {"August", 31},
            {"September", 30},
            {"October", 31},
            {"November", 30},
            {"December", 31},
    };
    
    cout << month["February"] << endl;

    return 0;
}

