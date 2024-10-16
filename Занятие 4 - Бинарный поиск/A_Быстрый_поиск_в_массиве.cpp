#include <iostream>
#include <algorithm> // для сортировки

using namespace std;

int main() {
    int n;
    cin >> n; // количество элементов в массиве

    int my_list[n]; // создание массива на n элементов
    for (int i = 0; i < n; i++){  // заполнение массива  10 1 10 3 4 => [10, 1, 10, 3, 4]
        cin >> my_list[i];
    }

    sort (my_list, my_list + n); // быстрая сортировка массива

    int k;
    cin >> k; // количество запросов

    int answer[k]; // массив для записи ответов на запросы

    for (int j = 0; j < k; j++){ // обработка запросов
        int x, y;
        cin >> x >> y; // получаем правую и левую границу поиска

        int ansx, ansy;

        int left_x = 0;
        int right_x = n-1;
        int middle;

        while ((right_x - left_x) > 1) {
            middle = (right_x + left_x)/2;
            if (my_list[middle] < x) left_x = middle;
            else right_x = middle;
        }
        
        if (my_list[left_x] >= x) ansx = left_x;
        else ansx = right_x;
        
        int left_y = 0;
        int right_y = n-1;
        while((right_y - left_y) > 1){
            middle = (right_y + left_y)/2;
            if (my_list[middle] <= y) left_y = middle;
            else right_y = middle;
        }

        if (my_list[right_y] <= y) ansy = right_y;
        else ansy = left_y;

        if ((x > my_list[ansy]) || (y < my_list[ansx]))  answer[j] = 0;
        else answer[j] = (ansy - ansx + 1);
    }

    for (int a = 0; a < k; a++){ // печать ответов из массива через пробел
        if (a == k-1) cout << answer[a];
        else cout << answer[a] << ' ';
    }

    return 0;
}
