#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream file("input.txt");
    ofstream file2("output.txt", ios_base::out);

    long long counter = 0;

    if(file.is_open()) {
        int n;
        file >> n;

        for (int i = 0; i < n; i++) {
            int spaces;
            file >> spaces;

            if (spaces == 1 or spaces == 4)
                counter += 1;
            else if (spaces == 0)
                counter += 0;
            else if (spaces == 2 or spaces == 3)
                counter += 2;
            else if (spaces % 4 == 0)
                counter += spaces/4;
            else if (spaces % 4 == 2 or spaces % 4 == 3)
                counter += (spaces/4 + 2);
            else if (spaces % 4 == 1)
                counter += (spaces/4 + 1);
        }
        file.close();
    }

    if(file2.is_open()) {
        file2 << counter;
        file2.close();
    }

	return 0;
}
