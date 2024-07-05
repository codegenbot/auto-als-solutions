```cpp
#include <algorithm>
using namespace std;

string sortNumbers(string inputString) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};

    vector<string> numVector;
    string temp;

    for (int i = 0; i < inputString.length(); i++) {
        if (inputString[i] == ' ') {
            continue;
        }
        temp = "";
        while (i < inputString.length() && inputString[i] != ' ') {
            temp += inputString[i];
            i++;
        }
        numVector.push_back(temp);
    }

    sort(numVector.begin(), numVector.end(), [&numMap](string a, string b) {
        return to_string(numMap[a]) < to_string(numMap[b]);
    });

    string result = "";
    for (int i = 0; i < numVector.size(); i++) {
        if (i > 0) {
            result += " ";
        }
        result += numVector[i];
    }

    return result;
}

int main() {
    assert(sortNumbers("six five four three two one zero") == "zero one two three four five six");
    return 0;
}