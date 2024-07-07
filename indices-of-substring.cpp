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
    vector<int> indices;

    string text;
    int numTargets;

    cin >> text >> numTargets;

    for(int i=0; i<numTargets; i++) {
        string target;
        cin >> target;
        vector<int> temp = indicesOfSubstring(text, target);
        for(int j : temp) {
            cout << j << endl;
        }
    }

    return 0;
}