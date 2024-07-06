#include <iostream>
using namespace std;

string change_base(int x, int base) {
    char res[1000];
    string s = "";
    size_t size = 0;
    while (x > 0) {
        int rem = x % base;
        if(rem < 10)
            res[size++] = '0' + rem;
        else if(rem <= 35)
            res[size++] = 'A' + rem - 10;
        else
            break;
    }
    for(int i = size - 1; i >= 0; i--)
        s += res[i];
    return s;
}

int main() {
    int num, base;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Enter the base: ";
    cin >> base;
    cout << "The conversion result is: " << change_base(num, base);
}