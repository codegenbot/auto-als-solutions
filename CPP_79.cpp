#include <string>
#include <iostream>

using namespace std;

char* decimal_to_binary(int decimal){
    char* binary = new char[32];
    int i = 31;
    while(decimal > 0){
        if((decimal & 1) == 1)
            binary[i--] = '1';
        else
            binary[i--] = '0';
        decimal >>= 1;
    }
    for(int j = i+1; j < 32; j++){
        binary[j] = '\0';
    }
    return binary;
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