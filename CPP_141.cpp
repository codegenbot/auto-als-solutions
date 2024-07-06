#include <string>
#include <cctype>
#include <vector>
#include <algorithm>

using namespace std;

int countDigits(const string& str) {
    int count = 0;
    for (char c : str) {
        if (isdigit(c)) {
            count++;
        }
    }
    return count;
}

string file_name_check(string file_name) {
    if (countDigits(file_name) > 3) {
        return "No";
    }

    size_t dotPos = file_name.rfind('.');
    if (dotPos == string::npos || file_name.find('.') != dotPos) {
        return "No";
    }

    string prefix = file_name.substr(0, dotPos);
    string suffix = file_name.substr(dotPos + 1);

    if (prefix.empty() || !isalpha(prefix[0])) {
        return "No";
    }

    vector<string> validSuffixes = {"txt", "exe", "dll"};
    if (find(validSuffixes.begin(), validSuffixes.end(), suffix) == validSuffixes.end()) {
        return "No";
    }

    return "Yes";
}