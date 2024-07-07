bool any_int(float a, float b, float c) {
    int ai = (int)a;
    int bi = (int)b;
    int ci = (int)c;

    return ((a == ai + bi + ci) || (b == ai + bi + ci) || (c == ai + bi + ci));
}

#include <iostream>
using namespace std;

int main() {
    float a, b, c;
    cout << "Enter three numbers: ";
    cin >> a >> b >> c;
    
    if(any_int(a, b, c))
        cout << "At least one number is an integer.\n";
    else
        cout << "None of the numbers are integers.\n";
    
    return 0;
}