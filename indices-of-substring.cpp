#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> indices_of_substring(const string& text, const string& target) {
    vector<int> indices;
    if (target.empty() || target.size() > text.size()) {
        return indices;
    }
    size_t pos = text.find(target);
    while (pos != string::npos) {
        indices.push_back(pos);
        pos = text.find(target, pos + 1 - target.size() + 1);
    }
    return indices;
}

int main() {
    string text, target;
    getline(cin, text);
    getline(cin, target);

    vector<int> result = indices_of_substring(text, target);
    cout << result.size() << endl;
    for (int index : result) {
        cout << index << " ";
    }
    cout << endl;

    return 0;
}