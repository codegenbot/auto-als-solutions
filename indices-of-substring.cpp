```c++
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
    cin >> text;

    int numTargets;
    cin >> numTargets;

    vector<int> indices;

    for(int i = 0; i < numTargets; ++i){
        string target;
        cin >> target;
        indices = indicesOfSubstring(text, target);
        
        // Print output
        for (int index : indices) {
            cout << index << endl;
        }
    }

    return 0;
}