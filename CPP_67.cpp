#include <iostream>
#include <sstream>
using namespace std;

int fruit_distribution(string s) {
    int total_fruits = 0;
    int apples = 0;
    int oranges = 0;

    stringstream input(s);
    string word;

    while (input >> word) {
        if (word == "apples")
            apples = stoi(next(input).skipws().ignore());
        else if (word == "oranges")
            oranges = stoi(next(input).skipws().ignore());
    }

    return total_fruits - apples - oranges;
}