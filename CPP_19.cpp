#include <algorithm>
#include <string>

using namespace std;

string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};
    vector<string> numVec;
    string num;

    for (char& c : numbers) {
        if (c == ' ') {
            continue;
        }
        num += c;
        if (!numMap.count(num)) {
            num = "";
        } else {
            numVec.push_back(num);
            num = "";
        }
    }

    sort(numVec.begin(), numVec.end());

    string result = "";
    for (string& s : numVec) {
        result += s + " ";
    }

    return result;
}