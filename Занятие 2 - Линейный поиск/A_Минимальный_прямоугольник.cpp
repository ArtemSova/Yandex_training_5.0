#include <iostream>
#include <set>

using namespace std;


int main() {
    int k;
    cin>>k;

    set<int>x_list;
    set<int>y_list;

    for(int i=0; i<k; ++i){
        int x;
        int y;
        cin >> x >> y;

        x_list.insert(x);
        y_list.insert(y);
    }
    // в множестве эл-ты храняться в отсортированном порядке

    int x_min;
    x_min = *x_list.begin();
    int y_min;
    y_min = *y_list.begin();
    int x_max;
    x_max = *x_list.rbegin();
    int y_max;
    y_max = *y_list.rbegin();

    cout << x_min << ' ' << y_min << ' ' << x_max << ' ' << y_max;

    return 0;
}
