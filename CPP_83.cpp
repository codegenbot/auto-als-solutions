#include <iostream>

using namespace std;

int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (i == 1 || i % 10 == 1) count++;
        if (n > 1 && i == 1) count += pow(10, n - 1);
        if (n > 1) {
            for (int j = 0; j < i; j++) {
                if (j == 0 || j % 10 == 1) count++;
                if (n > 2 && j == 0) count += pow(10, n - 2);
            }
        }
    }
    return count;
}

int main() {
    int n;
    cout << "Enter the number of digits: ";
    cin >> n;
    cout << "The count of numbers that start or end with 1 is: " << starts_one_ends(n) << endl;
    return 0;
}