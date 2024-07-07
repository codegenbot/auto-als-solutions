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
    cout << "Enter the text: ";
    cin >> text;
    
    int numTargets;
    cout << "How many targets: ";
    cin >> numTargets;

    vector<string> targets(numTargets);
    for (auto &target : targets) {
        cin >> target;
    }

    vector<int> indices = indicesOfSubstring(text, targets[0]);
    
    // Print output
    for (int index : indices) {
        cout << "Target found at index: " << index << endl;
    }

    return 0;
}