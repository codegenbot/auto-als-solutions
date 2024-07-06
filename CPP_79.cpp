#include <iostream>
#include <string>

string decimal_to_binary(int decimal);
int main() {
    string result = decimal_to_binary(15);
    assert(result == "db11111db");
    return 0;
}

string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0){
        if(decimal % 2 == 1)
            binary.insert(0,"1");
        else
            binary.insert(0,"0");
        decimal /= 2;
    }
    return "db" + binary + "db";
}