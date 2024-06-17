#include <iostream>
using namespace std;

int main() {
	int n;
    cin >> n;

    long long counter = 0;

    for(int i = 0; i < n; i++) {
        int spaces;
        cin >> spaces;

        if(spaces == 1 or spaces == 4)
            counter += 1;
        else if(spaces == 0)
            counter += 0;
        else if(spaces == 2 or spaces == 3)
            counter += 2;
        else if(spaces%4 == 0)
            counter += spaces/4;
        else if(spaces%4 == 2 or spaces%4 == 3)
            counter += spaces/4 + 2;
        else if(spaces%4 == 1)
            counter += spaces/4 + 1;
    }

    cout << counter;

	return 0;
}
