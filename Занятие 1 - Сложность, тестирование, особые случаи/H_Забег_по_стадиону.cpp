#include <iostream>
#include <cmath>

using namespace std;

int main() {

    int stadium, x1, v1, x2, v2;
    cin >> stadium >> x1 >> v1 >> x2 >> v2;

    double answer = pow(10, 30);

    int delta_x = (x2 - x1 + stadium) % stadium;
    int delta_v = v1 - v2;

    if (delta_v < 0) {
        delta_v = - delta_v;
        delta_x = (-delta_x + stadium) % stadium; // чтобы в С++ правильно считались остатки от деления отрицательного числа, прибавляем stadium
    }

    if (delta_x == 0) answer = 0;

    if (delta_v != 0) {
        double delta = (double)delta_x/delta_v; // double x = 2/4 => 0.00000 
        answer = min(answer, delta);
    }

    x2 = (-1 * x2 + stadium) % stadium;
    v2 = -v2;
    delta_x = (x2 - x1 + stadium) % stadium;
    delta_v = v1 - v2;

    if (delta_v < 0) {
        delta_v = -delta_v;
        delta_x = (-delta_x + stadium) % stadium;
    }

    if (delta_x == 0) answer = 0;

    if (delta_v != 0) {
        double delta = (double)delta_x/delta_v;
        answer = min(answer, delta);
    }

    if (answer == pow(10, 30)) cout << "NO";
    else {
        cout << "YES" << endl;
        printf("%.10f", answer);
    }

    return 0;
}
