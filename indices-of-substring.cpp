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
    cout << "Enter the text: ";
    cin >> text;

    int numTargets;
    cout << "Enter the number of targets: ";
    cin >> numTargets;

    vector<string> targets(numTargets);

    for (int i = 0; i < numTargets; ++i) {
        cout << "Enter target " << i + 1 << ": ";
        cin >> targets[i];
    }

    for (const string& target : targets) {
        vector<int> indices = indicesOfSubstring(text, target);
        cout << "Indices of '" << target << "':";
        for (int index : indices) {
            cout << " " << index;
        }
        cout << endl;
    }

    return 0;
}