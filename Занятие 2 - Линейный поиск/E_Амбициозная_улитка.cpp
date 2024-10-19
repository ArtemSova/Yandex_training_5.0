#include <iostream>
#include <vector>
#include <array>

using namespace std;

int main() {
	int n;
    cin >> n;

    // номер ягоды, up, down, difference (вектор массивов)
    vector <array<int, 4> > good_berries; // хорошие ягоды (рост высоты)
    vector <array<int, 4> > bad_berries;  // плохие ягоды (отрицательный прогресс)
    int g_berry[4]{0, 0, -1, 0}; // последняя хорошая ягода (max падение)
    int b_berry[4]{0, -1, 0, 0}; // первая плохая ягода (max рост)

    long long answer = 0;                          // max высота для ответа

    for(int i = 0; i < n; i++) {
        int up, down;
        cin >> up >> down;                   // рост и падение улитки от ягоды

        int difference = up - down;          // прогреес улитки (прирост - падение)

        if(difference >= 0) {                // если прогресс не отрицательный, ягода хорошая
            if(down > g_berry[2]) {          // и падение больше чем у последней хорошей ягоды
                if(g_berry[0] != 0){         // заменяем текущую посл хор ягоду
                    good_berries.push_back({g_berry[0], g_berry[1],g_berry[2],g_berry[3]});
                    answer += g_berry[3];    // учитываем прогресс предыдущей посл хор ягоды
                }
                g_berry[0] = i+1;
                g_berry[1] = up;
                g_berry[2] = down;
                g_berry[3] = difference;
            }
            else {                           // если паадение меньше, добавляем ягоду в вектор
                good_berries.push_back({i+1, up, down, difference});
                answer += difference;        // и учитываем ее прогресс
            }
        }
        else {                               // плохая ягода
            if (up > b_berry[1]) {           // если рост выше чем у первой плохой ягоды
                if (b_berry[0] != 0) {       // заменяем текущ первую плох ягоду
                    bad_berries.push_back({b_berry[0], b_berry[1], b_berry[2], b_berry[3]});
                }
                b_berry[0] = i+1;
                b_berry[1] = up;
                b_berry[2] = down;
                b_berry[3] = difference;
            }
            else bad_berries.push_back({i+1, up, down, difference});      // добав плохие ягоды в вектор плохих ягод
        }
    }

    // если рост первой плохой ягоды выше, чем падение последней плохой ягоды, то сначала учитываем весь прогресс посл
    if(g_berry[2] < b_berry[1]) {
        answer += (g_berry[3] + b_berry[1]);  // хор ягоды, а затем прибавляем рост перв плох ягоды
    }
    else answer += g_berry[1];                             // иначе просто прибавляем рост последней хор ягоды к ответу

    cout << answer << endl;                    // печать ответа

    if (good_berries.size() > 0) {       // если у нас есть хорошие ягоды, выводим их номера из списка(вектора)
        for (int i = 0; i < good_berries.size(); i++) {
            cout << good_berries[i][0] << " ";
        }
    }

    if (b_berry[0] != 0) {                                // если у нас есть первая плох ягода
        if (g_berry[0] != 0) cout << g_berry[0] << " ";   // выводим последнюю хорошую ягоду
        if(bad_berries.size() > 0) {                      // если у нас есть в списке плохие ягоды
            cout << b_berry[0] << " ";                    // выводим их поочередно
            for(int j = 0; j < bad_berries.size(); j++){
                if (j != bad_berries.size()-1) {
                    cout << bad_berries[j][0] << " ";
                }
                else cout << bad_berries[j][0];            // посленюю ягоду печатаем без отступа
            }
        }
        else cout << b_berry[0];    // выводим первую и единственную плохую ягоду
    }
    else cout << g_berry[0];     // иначе просто выводим последнюю хорошую ягоду

	return 0;
}
