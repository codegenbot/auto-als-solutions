#include <iostream>
#include <string>

using namespace std;

string compareOne(string a, string b) {
    if (a > b)
        return a;
    else if (b > a)
        return b;
    else
        return "None";
}

int main() {
    cout << compareOne("apple", "banana") << endl; // output: None
    cout << compareOne("banana", "apple") << endl; // output: apple
    cout << compareOne("orange", "grape") << endl; // output: orange
    return 0;
}