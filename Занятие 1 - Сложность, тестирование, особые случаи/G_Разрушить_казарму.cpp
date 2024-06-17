#include <iostream>
#include <cmath>

using namespace std;

int calc(int t, int my_units, int bar_hp, int enemy_prod) {
    int rounds = 0;
    int enemy_units = 0;

    while (bar_hp >= t) {  // здоровье выше порга, бъем без потери юнитов
        if (enemy_units >= my_units) return pow(10, 9);

        bar_hp -= my_units - enemy_units;
        enemy_units = 0;

        if (bar_hp >= 0) enemy_units += enemy_prod;

        rounds += 1;
    }

    while (bar_hp > 0) { // смена способа (стратегии)
        if (my_units <= 0) return pow(10, 9);

        if (bar_hp >= my_units) bar_hp -= my_units;
        else {
            enemy_units -= my_units - bar_hp;
            bar_hp = 0;
        }

        my_units -= enemy_units;

        if (bar_hp > 0) enemy_units += enemy_prod;

        rounds += 1;
    }

    while (enemy_units > 0) { // добивание оставшихся юнитов противника
        if (my_units <= 0) return pow(10, 9);

        enemy_units -= my_units;

        if (enemy_units > 0) my_units -= enemy_units;

        rounds += 1;
    }

    return rounds;
}

// ограничение 5000 (max здоровье казармы), можно перебрать все возможности

int main() {
    int x, y, p;
    cin >> x >> y >> p;

    int answer = pow(10, 9);  // 10**9

    for (int t = 0; t < (y + 2); t++) {  // перебирается уро-нь здоровья казармы, при котором меняется способ нанесения урона
        answer = min(answer, calc(t, x, y, p));
    }

    if (answer != pow(10, 9)) cout << answer;
    else cout << -1;


	return 0;
}
