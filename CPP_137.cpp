#include <iostream>
#include <string>

using namespace std;

string compare_one(double a, string b) {
    if (a > stod(b))
        return to_string(a);
    else
        return b;
}

int main() {
    double a = 10.5; 
    string b = "hello";
    string result = compare_one(a, b);
    cout << "Result: " << result << endl;
    return 0;
}