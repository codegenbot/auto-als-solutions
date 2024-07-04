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
    cin >> num;
    cout << squareDigits(num) << endl;
    return 0;
}