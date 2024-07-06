#include <iostream>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    size_t pos = 0;
    string temp = "";
    for (size_t i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            pos = i;
            break;
        }
        temp += s[i];
    }
    int apples = stoi(temp);
    int oranges = stoi(s.substr(pos + 1, s.find(" oranges") - pos - 1).substr(0, s.find(" ")));
    return n - apples - oranges;
}

int main() {
    cout << fruit_distribution("5 apples and 6 oranges", 19) << endl;
    cout << fruit_distribution("0 apples and 1 oranges", 3) << endl;
    cout << fruit_distribution("2 apples and 3 oranges", 100) << endl;
    cout << fruit_distribution("100 apples and 1 oranges", 120) << endl;
    return 0;
}