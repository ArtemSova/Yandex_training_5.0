#include <iostream>

using namespace std;

int main() {
    int p, v;
    int q, m;

    cin >> p >> v;
    cin >> q >> m;

    int v1 = p - v;
    int v2 = p + v;
    int m1 = q - m;
    int m2 = q + m;

    if(min(v2, m2) < max(v1, m1)) {
        cout << (v2 - v1 + 1 + m2 - m1 + 1);
    }
    else
        cout << (max(v2, m2) - min(v1, m1) + 1);

    return 0;
}
