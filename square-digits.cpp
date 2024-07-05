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
    if (num <= 0) {
        cout << "Please enter a positive integer." << endl;
    } else {
        cout << squareDigits(num) << endl;
    }
    return 0;
}