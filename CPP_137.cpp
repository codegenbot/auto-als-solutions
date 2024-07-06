#include <iostream>
#include <string>
#include <any>

using namespace std;

any compare_one(any a, any b) {
    double da = any_cast<double>(a);
    string sa = any_cast<string>(a);
    double db = any_cast<double>(b);
    string sb = any_cast<string>(b);

    if (da > db || (sa.empty() && !sb.empty()))
        return a;
    else if (!sa.empty() && sb.empty())
        return a;
    else if (db > da)
        return b;
    else
        return "None";
}

int main() {
    any a = 10.5; 
    any b = "hello";
    any result = compare_one(a, b);
    cout << "Result: " << any_cast<string>(result) << endl;
    return 0;
}