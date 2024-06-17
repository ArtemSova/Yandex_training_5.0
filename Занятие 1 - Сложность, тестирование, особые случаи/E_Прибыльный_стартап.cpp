#include <iostream>

using namespace std;

int main()
{
    unsigned long long n, k;
    int d;
    cin >> n >> k >> d;

    d -= 1;
    n *= 10;
    int digit = 0;
    for (; digit < 10; digit++)
    {
        if ((n + digit) % k == 0)
        {
            // Если есть делитель для первого дня прибыли, то для остальных можно просто приписывать нули,
            // они тоже будут делиться
            n += digit;
            cout << n;
            while (d > 0)
            {
                cout << '0'; // В C++ мы просто печатаем всё подряд, это выйдет одной строкой
                d--;
            }
            return 0;
        }
    }
    cout << "-1";
    return 0;
}
