```cpp
string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0){
        if((decimal & 1) == 1)
            binary = "1" + binary;
        else
            binary = "0" + binary;
        decimal >>= 1;
    }
    return "db" + binary + "db";
}

int main() {
    int decimal;
    cout << "Enter a decimal number: ";
    cin >> decimal;
    string binary = decimal_to_binary(decimal);
    cout << "The binary representation of the entered decimal number is: " << binary << endl;
    return 0;
}