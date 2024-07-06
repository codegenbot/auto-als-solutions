#include <iostream>
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "";
    while(decimal > 0) {
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    string result = "db";
    result += binary;
    result += "db";
    return result;
}

int main() {
    int decimal;
    cout << "Enter a number: ";
    cin >> decimal;
    cout << decimal_to_binary(decimal) << endl;
    return 0;
}