#include <iostream>
#include <vector>
using namespace std;

vector<int> indicesOfSubstring(string text, string target) {
    vector<int> result;
    int n = text.length();
    int m = target.length();

    for (int i = 0; i <= n - m; ++i) {
        if (text.substr(i, m) == target) {
            result.push_back(i);
        }
    }

    return result;
}

int main() {
    string text;
    int numTargets;

    cin >> text >> numTargets;

    vector<int> indices = indicesOfSubstring(text, "");

    for (int i = 0; i < numTargets; ++i) {
        string target;
        cin >> target;
        vector<int> result = indicesOfSubstring(text, target);
        for (int index : result) {
            cout << index << endl;
        }
    }

    return 0;
}