#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> indices_of_substring(const string& text, const string& target) {
    vector<int> indices;
    if (target.size() > text.size()) {
        return indices;
    }
    for (size_t i = 0; i <= text.size() - target.size(); ++i) {
        if (text.substr(i, target.size()) == target) {
            indices.push_back(i);
        }
    }
    return indices;
}

int main() {
    string text, target;
    getline(cin, text);
    cin.ignore(); // Clear the buffer
    cin >> target;

    vector<int> result = indices_of_substring(text, target);
    cout << result.size() << endl;
    for (int index : result) {
        cout << index << " ";
    }
    cout << endl;

    return 0;
}