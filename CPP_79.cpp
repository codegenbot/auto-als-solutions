#include <string>
#include <iostream>

using namespace std;

char* decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0){
        if((decimal & 1) == 1)
            binary = "1" + binary;
        else
            binary = "0" + binary;
        decimal >>= 1;
    }
    char* str = new char[binary.length() + 3];
    strcpy(str, "0b");
    strcat(str, binary.c_str());
    return str;
}

int main() {
    int decimal;
    cout << "Enter a decimal number: ";
    cin >> decimal;
    char* binary = decimal_to_binary(decimal);
    cout << "The binary representation of the entered decimal number is: " << binary << endl;
    delete[] binary;
    return 0;
}