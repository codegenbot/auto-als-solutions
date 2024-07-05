#include <iostream>
#include <string>
using namespace std;

string squareDigits(int num) {
    string result = "";
    string numStr = to_string(num);
    for (char c : numStr) {
        int digit = c - '0';
        result += to_string(digit * digit);
    }
    return result;
}

int main() {
    int num;
    if (cin >> num && num > 0) {
        cout << squareDigits(num) << endl;
    } else {
        cout << "Invalid input" << endl;
    }
    return 0;
}