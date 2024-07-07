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
    // Read input from user
    string text;
    int numTargets;
    cin >> text >> numTargets;

    vector<string> targets;
    for(int i = 0; i < numTargets; ++i) {
        string target;
        cin >> target;
        targets.push_back(target);
    }

    vector<int> indices;
    for(string target : targets) {
        indices = indicesOfSubstring(text, target);
        for(int index : indices) {
            cout << index << endl;
        }
    }

    return 0;
}