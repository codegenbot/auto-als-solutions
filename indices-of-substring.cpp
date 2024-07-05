#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> indices_of_substring(const string& text, const string& target) {
    vector<int> indices;
    size_t target_size = target.size();
    size_t text_size = text.size();

    if (target_size > text_size) {
        return indices;
    }

    for (size_t i = 0; i <= text_size - target_size; ++i) {
        if (text.compare(i, target_size, target) == 0) {
            indices.push_back(i);
        }
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