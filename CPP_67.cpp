#include <iostream>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    int apples = 0, oranges = 0;
    string temp;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            if (temp.find("apples") != string::npos)
                apples = stoi(temp.substr(0, temp.find("and")));
            else if (temp.find("oranges") != string::npos)
                oranges = stoi(temp.substr(0, temp.find("and")));
            temp.clear();
        } else {
            temp += s[i];
        }
    }

    return n - apples - oranges;
}

int main() {
    cout << fruit_distribution("5 apples and 6 oranges", 19) << endl;
    cout << fruit_distribution("0 apples and 1 oranges", 3) << endl;
    cout << fruit_distribution("2 apples and 3 oranges", 100) << endl;
    cout << fruit_distribution("100 apples and 1 oranges", 120) << endl;
    return 0;
}