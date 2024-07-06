#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int apples = 0, oranges = 0;

    // Count number of apples and oranges in string
    while ((pos = s.find(" apples", pos)) != string::npos) {
        apples +=stoi(s.substr(pos-std::to_string(0).size(),pos-(pos-std::to_string(0).size())).c_str());
        pos = s.find(" ", pos);
    }

    // Count number of oranges in string
    while ((pos = s.find(" oranges", pos)) != string::npos) {
        oranges +=stoi(s.substr(pos-std::to_string(0).size(),pos-(pos-std::to_string(0).size())).c_str());
        pos = s.find(" ", pos);
    }

    return n - apples - oranges;
}