#include<string>
#include<map>
using namespace std;

string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};

    vector<string> numVec;
    string numStr;

    for (int i = 0; i < numbers.length(); i++) {
        while (i < numbers.length() && !isdigit(numbers[i])) {
            i++;
        }
        if (i >= numbers.length()) break;
        int j = i + 1;
        while (j < numbers.length() && isdigit(numbers[j])) {
            j++;
        }
        numStr = numbers.substr(i, j - i);
        numVec.push_back(numMap[numStr]);
    }

    sort(numVec.begin(), numVec.end());
    string result;

    for (int i = 0; i < numVec.size(); i++) {
        for (auto it = numMap.begin(); it != numMap.end(); ++it) {
            if (it->second == numVec[i]) {
                result += it->first;
                break;
            }
        }
        if (i < numVec.size() - 1) {
            result += " ";
        }
    }

    return result;
}