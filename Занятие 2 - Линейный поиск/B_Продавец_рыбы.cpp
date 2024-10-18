#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, k;                             // количество дней и продолжительность хранения
    cin >> n >> k;

    vector <int> my_list(n);              // цены на каждый день

    for(int i = 0; i < n; i++){
        cin >> my_list[i];
    }


    int max_value = 0;                    // максимальная прибыль (ответ)

    for(int i = (n-1); i > 0; i--) {      // перебираем цены, начиная с последнего дня
        for(int j = k; j > 0; j--) {      // уменьшаем срок хранения от максимального
            if((i-j) >= 0) {              //
                if(my_list[i] - my_list[i-j] > max_value) {
                    max_value = my_list[i] - my_list[i-j];
                }
            }
        }
    }

    cout << max_value;

	return 0;
}
