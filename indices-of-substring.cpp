#include <iostream>
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

    cout << "Enter a text: ";
    cin >> text;
    
    cout << "Enter number of targets: ";
    cin >> numTargets;

    vector<int> indices = indicesOfSubstring(text, "");
    
    for (int index : indices) {
        cout << index << endl;
    }

    return 0;
}