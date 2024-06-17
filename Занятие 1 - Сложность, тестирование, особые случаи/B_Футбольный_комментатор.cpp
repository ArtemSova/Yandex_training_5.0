#include <iostream>
using namespace std;

int main() {
    int first_1, first_2, second_1, second_2;
    char colon;
    cin >> first_1 >> colon >> first_2;
    cin >> second_1 >> colon >> second_2;
    int terr;
    cin >> terr;

    int team_1 = first_1 + second_1;
    int team_2 = first_2 + second_2;

    if(team_1 > team_2) {
        cout << 0;
    }
    else if(team_1 == team_2) {
        if(terr == 1) {
            if(second_1 > first_2)
                cout << 0;
            else
                cout << 1;
        }
        else{
            if(first_1 > second_2)
                cout << 0;
            else
                cout << 1;
        }
    }
    else {
        if(terr == 1){
            if(first_2 < (second_1 + (team_2 - team_1)))
                cout << (team_2 - team_1);
            else
                cout << (team_2 - team_1 + 1);
        }
        else {
            if(second_2 < first_1)
                cout << (team_2 - team_1);
            else
                cout << (team_2 - team_1 + 1);
        }
    }

	return 0;
}
