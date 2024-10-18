#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
	int n;                            // колич оставшихся веревочек
    cin >> n;

    vector <int> my_list(n);          // длины оставшихся веревочек
    for(int i = 0; i < n; i++) {
        cin >> my_list[i];
    }

    int full = *max_element(my_list.begin(), my_list.end());  // максимальный элемент вектора

    for(int i = 0; i < n; i++) {
        if(my_list[i] == full) {                                       // если элемент максимальный
            my_list.erase(my_list.begin()+i);                  // удаляем его из вектора
            break;
        }
    }

    int summa = reduce(my_list.begin(), my_list.end());      // сумма оставшихся длин в векторе

    if(full > summa) cout << full - summa;
    else cout << full + summa;


	return 0;
}
