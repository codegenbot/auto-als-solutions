#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;
    size_t prev = 0, next = 0;

    while ((next = txt.find_first_of(" ,")) != string::npos) {
        if (next == 0) {
            break;
        }
        string word = txt.substr(prev, next - prev);
        result.push_back(word);
        prev = next + 1;
    }

    if (prev < txt.size()) {
        result.push_back(txt.substr(prev));
    } else if (txt.empty()) {
        int count = 0;
        for (char c : txt) {
            if ((int)c - (int)'a' % 26 == 3)
                count++;
        }
        result.push_back(to_string(count));
    }

    return result;
}

int main() {
    string txt;
    cout << "Enter a string: ";
    getline(cin, txt);
    vector<string> result = split_words(txt);
    for (string s : result) {
        cout << s << endl;
    }
    return 0;
}