#include <iostream>
#include <string>

using namespace std;

string compare_one(double a, string b) {
    if (a > 0 || (b.empty() && !b.empty()))
        return to_string(a);
    else if (!b.empty() && b.empty())
        return "None";
    else if (b > "")
        return b;
    else
        return "None";
}

int main() {
    double a = 10.5; 
    string b = "hello";
    string result = compare_one(a, b);
    cout << "Result: " << result << endl;
    return 0;
}