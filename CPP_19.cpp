#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

string sort_numbers(string numbers) {
    unordered_map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                          {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                          {"eight", 8}, {"nine", 9}};
    vector<string> numVec;
    string temp;

    for (int i = 0; i < numbers.size(); i++) {
        while (i + 1 < numbers.size() && !ispunct(numbers[i + 1])) {
            i++;
        }
        temp = numbers.substr(0, i + 1);
        numVec.push_back(temp);
        numbers.erase(0, i + 1);

        if (!numbers.empty()) {
            i = -1;
        }
    }

    sort(numVec.begin(), numVec.end(), [&numMap](const string& a, const string& b) {
        return numMap.at(a) < numMap.at(b);
    });

    string result;
    for (string s : numVec) {
        result += s + " ";
    }
    return result;
}