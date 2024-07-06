#include <algorithm>
using namespace std;

string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};
    vector<string> numVec;
    string num;

    // Split the input string into individual numbers
    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            continue;
        }
        bool found = false;
        for (auto it : numMap) {
            if (it.first.length() <= i - numVec.size() && numbers.substr(i - it.first.length(), it.first.length()) == it.first) {
                num = it.first;
                found = true;
                break;
            }
        }
        if (found) {
            numVec.push_back(num);
            i += num.length() - 1;
        } else {
            num += numbers[i];
        }
    }

    // Sort the vector of numbers
    sort(numVec.begin(), numVec.end());

    // Join the sorted numbers back into a string
    string result = "";
    for (auto it : numVec) {
        result += it + " ";
    }
    return result;
}