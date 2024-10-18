#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    short n;
    cin >> n;

    map <short, vector<short> > x_line;             // словарь иксов с их игриками
    map <short, vector<short> > y_line;             // словарь игриков с их иксами

    for(short i; i < n; i++) {
        short x, y;
        cin >> x >> y;

        if(x_line.find(x) != x_line.end()) x_line[x].push_back(y);   // x уже есть в словаре, добав y  в значения x
        else x_line[x] = {y};                                        // создаем ключ x с вектором из одного y

        if(y_line.find(y) != y_line.end()) y_line[y].push_back(x);
        else y_line[y] = {x};
    }

    short answer = 0;                                // ответ на задачу

    for(const auto &[x, x_y]: x_line) {
        short counter = 2;                                          // у каждого икса точно есть два края по игрику

        for(short j = 1; j < x_y.size(); j++){                      // перебираем игрики по текущему иксу
            try {
                if ((x_y[j] - x_y[j - 1]) != 1) counter += 2;       // если иксы не соприказаются (разделены по игрику)
            }                                                       // добавляем еще 2 грани по игрику
            catch (...) {}                                          // в противном случае 2 клетки объединяются в одну, сохраня 2 грани
        }

        answer += counter;                                          // добавляем количество получившихся граней к ответу
    }

    for(const auto &[y, y_x]: y_line) {
        short counter = 2;

        for(short j = 1; j < y_x.size(); j++){
            try {
                if ((y_x[j] - y_x[j - 1]) != 1) counter += 2;
            }
            catch (...) {}
        }
        answer += counter;
    }

    cout << answer;

	return 0;
}
