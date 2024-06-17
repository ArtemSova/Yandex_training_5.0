#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    string state = "no_odd"; // no odd - нет нечетного

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        if (state == "no_odd") {
            if (num%2 == 0) cout << '+';
            else state = "last_odd";
        }
        else if (state == "last_odd") {
            if (num%2 == 0) {
                state = "multiply_even";
                cout << '+';
            }
            else cout << 'x';
        }
        else cout << 'x';
    }

	return 0;
}

// логика другая из разбора:
// все четные до первого нечетного мы складываем
// затем все нечетные подряд перемножаем
// после окончания цикла нечетных снова складываем все оставшиеся

