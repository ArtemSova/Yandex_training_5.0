#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> board(8, vector<int>(8, 0)); // Массив заполенный нулями: {0, 0, 0.......}

    for (int i = 0; i < 8; ++i) {
        string line;
        cin >> line; // получаю строчные данные, разбиваю их на символы и записываю цифры,, в соответсвии с символом
        for (int j = 0; j < 8; ++j) {
            if (line[j] == '*') board[i][j] = 0;
            if (line[j] == 'B') board[i][j] = 1;
            if (line[j] == 'R') board[i][j] = 2;
        }
    } // на выходе массив, заполненный 0, 1 и 2 в соответсвии с символами

    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
            if (board[i][j] == 2) {
                for (int k = i + 1; k < 8; ++k) {
                    if (board[k][j] == 0) board[k][j] = -1; // если ячейка не занята и не обработана, т.е. == 0, заменяем ее на -1, обработанную
                    else if (board[k][j] == 1 || board[k][j] == 2) break; // если ячейка занята фигурой, останавливаем цикл
                }
                for (int k = i - 1; k >= 0; --k) {
                    if (board[k][j] == 0) board[k][j] = -1;
                    else if (board[k][j] == 1 or board[k][j] == 2) break; // C++ понимает и английское обозначение операторов (можно писать и "||" и "or")
                }
                for (int k = j + 1; k < 8; ++k) {
                    if (board[i][k] == 0) board[i][k] = -1;
                    else if (board[i][k] == 1 || board[i][k] == 2) break;
                }
                for (int k = j - 1; k >= 0; --k) {
                    if (board[i][k] == 0) board[i][k] = -1;
                    else if (board[i][k] == 1 || board[i][k] == 2) break;
                }
            }
            if (board[i][j] == 1) {
                for (int k = i + 1, p = j + 1; k < 8 && p < 8; ++k, ++p) {
                    if (board[k][p] == 0) board[k][p] = -1;
                    else if (board[k][p] == 1 || board[k][p] == 2) break;
                }
                for (int k = i + 1, p = j - 1; k < 8 && p >= 0; ++k, --p) {
                    if (board[k][p] == 0) board[k][p] = -1;
                    else if (board[k][p] == 1 || board[k][p] == 2) break;
                }
                for (int k = i - 1, p = j + 1; k >= 0 && p < 8; --k, ++p) {
                    if (board[k][p] == 0) board[k][p] = -1;
                    else if (board[k][p] == 1 || board[k][p] == 2) break;
                }
                for (int k = i - 1, p = j - 1; k >= 0 && p >= 0; --k, --p) {
                    if (board[k][p] == 0) board[k][p] = -1;
                    else if (board[k][p] == 1 || board[k][p] == 2) break;
                }
            }
        }
    }

    int counter = 0; // считаю оставшиеся нули в массиве
    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
            if (board[i][j] == 0) counter++;
        }
    }
    cout << counter << endl;
}
