#include <algorithm>
#include <string>

using namespace std;

string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};
    vector<string> nums;
    string temp;

    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            continue;
        }
        temp += numbers[i];
        if (i == numbers.length() - 1 || numbers[i + 1] != ' ') {
            nums.push_back(temp);
            temp = "";
        }
    }

    sort(nums.begin(), nums.end(), [&](string a, string b) {
        return numMap[a] < numMap[b];
    });

    string result;
    for (const auto &num : nums) {
        result += num + " ";
    }
    return result.substr(0, result.length() - 1);
}