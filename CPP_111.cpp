#include<stdio.h>
#include<string>
#include<map>
using namespace std;

map<char, int> histogram(string test) {
    map<char, int> result;
    if (test.empty()) return result;

    size_t count = 0;
    char currentChar = test[0];
    for (size_t i = 1; i <= test.size(); i++) {
        if (i == test.size() || test[i] != currentChar) {
            result[currentChar] = ++count;
            currentChar = test[i];
            count = 1;
        }
    }

    return result;
}