#include <iostream>
#include <map>
#include <vector>

using namespace std;

const string week_days[7] = { // список дней недели
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
};

const map <string, int> days_week = { // "словарь" дней недели
        {"Monday", 0},
        {"Tuesday", 1},{"Wednesday", 2},
        {"Thursday", 3},
        {"Friday", 4},
        {"Saturday", 5},
        {"Sunday", 6}
};

map <string, int> months = {  // словарь количества дней в месяцах
        {"January",   1},
        {"February",  2},
        {"March",     3},
        {"April",     4},
        {"May",       5},
        {"June",      6},
        {"July",      7},
        {"August",    8},
        {"September", 9},
        {"October",   10},
        {"November",  11},
        {"December",  12},
};

map <string, vector<int>> holidays; // словарь списков праздников

int main() {
    int n, year; // колич праздников в году (3) и год (2015)
    cin >> n >> year;

    int d;      // день
    string m;   // и месяц (дата праздника)

    for (int i = 0; i < n; i++) { // заполняем список праздников
        cin >> d >> m;            // день и месяц празника (дата)
        if(holidays.find(m) != holidays.end()) {  // месяц уже есть в словаре
            holidays[m].push_back(d);                // добавляем в вектор день празника
        }
        else holidays[m] = {d};
    }

    string start;  // день недели, первого января
    cin >> start;

    int is_leap;         // пременная для високосного года
    int middle_weeks;    // колич полных недель в году
    int first_week;      // колич дней в первой неделе
    int last_week;       // колич дней в последней неделе

    if (year%400 == 0 or year%4 == 0 and year%100 != 0) {
        is_leap = 1;
        first_week = 7 - days_week.at(start); //map.at() получает знач по ключу, не добавляя новое, если такого нет в словаре
        middle_weeks = (366 - first_week) / 7;
        last_week = 366 - first_week - middle_weeks*7;
    }
    else {
        is_leap = 0;
        first_week = 7 - days_week.at(start);
        middle_weeks = (365 - first_week) / 7;
        last_week = 365 - first_week - middle_weeks*7;
    }

    map <string, int> month = {  // словарь количества дней в месяцах
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

    map <string, int> days_cnt = {                 // счетчик количества "дней недели" в году
            {"Monday", middle_weeks},        // дни из полных недель
            {"Tuesday", middle_weeks},
            {"Wednesday", middle_weeks},
            {"Thursday", middle_weeks},
            {"Friday", middle_weeks},
            {"Saturday", middle_weeks},
            {"Sunday", middle_weeks}
    };

    for (int i = 7 - first_week; i < 7; i++) {  // добавляем дни первой недели
        days_cnt[week_days[i]] += 1;
    }

    for (int i = 0; i < last_week; i++) {  // добавляем дни последней недели
        days_cnt[week_days[i]] += 1;
    }

    for (const auto &[hmonth, hday]: holidays) {   // получаем месяц и вектор дней
        for (int i = 0; i < hday.size(); i++) {                            // получаем каждый день по отдельности
            int days_from_start = 0;                                       // номер дня празника с начала года
            for (const auto &[m, num]: months) {
                if (m == hmonth) {                                         // если месяц тот же, в котором празник
                    days_from_start += hday[i];                            // берем дни с 1 по праздничный (+ дата(номер) дня)
                } else if (num < months[hmonth]) {                         // если месяц идет до праздничного месяца
                    days_from_start += month.at(m);                     // берем все его дни
                } else {
                    // ничего не делаем
                }
            }

            int marker = days_from_start % 7;           // колич дней вне полной недели (остаток дней от полных недель)
            int new_start = days_week.at(start);     // индекс дня недели 1го января
            int day_ind = new_start + marker - 1;       // индекс дня недели праздника

            if (day_ind < 0) day_ind += 7;           // если индекс получился отрицательный, добавляем неделю
            if (day_ind > 6)
                day_ind -= 7;           // если индекс больше 6, он уходит в следующую неделю, вычетаем неделю

            days_cnt[week_days[day_ind]] -= 1;      //  вычитаем один день (праздничный) у дня недели в счетчике, так как это минус халявный выходной
        }
    }

    string max_day;        // переменная для ответа наилучшего дня недели
    string min_day;        // переменная для ответа худшего дня недели
    int maximum = -10;       // маркер для поиска максимума
    int minimum = 100;     // маркер для поиска минимума

    for(const auto &[day, count]: days_cnt) {
        if(count < minimum) minimum = count, min_day = day;
        if(count > maximum) maximum = count, max_day = day;
    }

    cout << max_day << " " << min_day;

    return 0;
}
