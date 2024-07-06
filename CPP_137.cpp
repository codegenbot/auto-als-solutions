#include <iostream>
#include <string>

using namespace std;

string compare_one(double a, string b, double c, string d) {
    if (a > c)
        return to_string(a);
    else if (b > d)
        return "None";
    else
        return "None";
}

int main() {
    double a = 10.5; 
    string b = "hello";
    double c = 3.2;
    string d = "hi";
    string result = compare_one(a, b, c, d);
    cout << "Result: " << result << endl;
    return 0;
}