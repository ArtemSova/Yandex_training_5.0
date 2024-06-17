#include <iostream>
#include <map>
#include <vector>

using namespace std;

const string week[7] = { // список
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
};

const map <string,int> days_week = {
        {"Monday", 1},
        {"Tuesday", 2}
};


int main() {
    int n, year;
    cin >> n >> year;

    int is_leap;

    if (year%400 == 0 or year%4 == 0 and year%100 != 0) is_leap = 1;
    else is_leap = 0;

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

    int d;
    string m;

    map <int, string> holidays;

    for (int i = 0; i < n; i++) {
        cin >> d >> m;
        holidays[d] = m;
    }

    string start;
    cin >> start;


    return 0;
}

