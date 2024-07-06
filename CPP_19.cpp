#include <algorithm>
using namespace std;

string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};
    vector<string> nums;
    string num;

    for (string s : split(numbers, " ")) {
        if (numMap.count(s)) {
            nums.push_back(s);
        }
    }

    sort(nums.begin(), nums.end());
    return join(nums, " ");
}

vector<string> split(const string& str, char c) {
    vector<string> tokens;
    size_t pos = 0;
    while ((pos = str.find(c)) != string::npos) {
        tokens.push_back(str.substr(0, pos));
        str.erase(0, pos + 1);
    }
    tokens.push_back(str);
    return tokens;
}

string join(vector<string> nums, char c) {
    string result;
    for (int i = 0; i < nums.size(); i++) {
        if (i > 0) {
            result += c;
        }
        result += nums[i];
    }
    return result;
}