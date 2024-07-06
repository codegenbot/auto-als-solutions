#include <algorithm>
using namespace std;

string sort_numbers(string numbers) {
    map<string, int> numMap = {
        {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
        {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
        {"eight", 8}, {"nine", 9}
    };

    vector<string> numVec;
    string num;

    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            continue;
        }
        num += numbers[i];
        if (i + 1 >= numbers.length() || numbers[i + 1] != ' ') {
            numVec.push_back(num);
            num = "";
        }
    }

    sort(numVec.begin(), numVec.end(), [&numMap](const string& a, const string& b) {
        return numMap.at(a) < numMap.at(b);
    });

    string result;
    for (string& str : numVec) {
        result += str + " ";
    }
    return result.substr(0, result.length() - 1);
}