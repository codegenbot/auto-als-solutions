#include <iostream>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    string apples, oranges;
    size_t found = s.find(" and ");
    if (found != string::npos) {
        apples = s.substr(0, found);
        oranges = s.substr(found + 5);
    }
    else {
        if (s.find(" apples") != string::npos)
            apples = s.substr(0, s.find(" apples"));
        if (s.find(" oranges") != string::npos)
            oranges = s.substr(s.find(" and ") == string::npos ? s.find(" oranges") : s.find(" and ")+3);
    }
    int countApples = stoi(apples.substr(0, apples.find(" ")));
    int countOranges = stoi(oranges.substr(0, oranges.find(" ")));
    
    return n - (countApples + countOranges);
}

int main() {
    cout << fruit_distribution("5 apples and 6 oranges", 19) << endl;
    cout << fruit_distribution("0 apples and 1 oranges",3) << endl;
    cout << fruit_distribution("2 apples and 3 oranges", 100) << endl;
    cout << fruit_distribution("100 apples and 1 oranges",120) << endl;
    return 0;
}