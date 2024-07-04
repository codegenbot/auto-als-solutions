#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> indices_of_substring(const string& text, const string& target) {
    vector<int> indices;
    for (size_t i = 0; i <= text.size() - target.size(); ++i) {
        if (text.substr(i, target.size()) == target) {
            indices.push_back(i);
        }
    }
    return indices;
}

int main() {
    string target, text;
    cin >> target;
    cin.ignore();
    getline(cin, text);

    vector<int> result = indices_of_substring(text, target);
    cout << result.size() << endl;
    for (int index : result) {
        cout << index << " ";
    }
    cout << endl;

    return 0;
}