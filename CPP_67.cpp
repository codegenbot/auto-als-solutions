#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    string input = s;
    int total_fruits = n;
    size_t pos = 0;
    int apples = 0;
    int oranges = 0;

    while ((pos = input.find(" ")) != string::npos) {
        if (input.substr(0, pos).find("apples") != string::npos)
            apples = stoi(input.substr(0, pos).substr(input.find(" ") + 1));
        else if (input.substr(0, pos).find("oranges") != string::npos)
            oranges = stoi(input.substr(0, pos).substr(input.find(" ") + 1));
        input.erase(0, pos + 1);
    }

    return total_fruits - apples - oranges;
}