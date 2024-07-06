```cpp
#include <string>
#include <iostream>

using namespace std;

string decimal_to_binary(int decimal){
    string bin = "";
    if (decimal < 0) {
        bin = "-" + decimal_to_binary(-decimal);
        return bin;
    }
    while(decimal > 0){
        if((decimal & 1) == 1)
            bin = "1" + bin;
        else
            bin = "0" + bin;
        decimal >>= 1;
    }
    string resultBinary = "0b" + bin;
    return resultBinary;
}

int main() {
    int decimal;
    cout << "Enter a decimal number: ";
    cin >> decimal;
    string binary = decimal_to_binary(decimal);
    cout << "The binary representation of the entered decimal number is: " << binary << endl;
    return 0;
}