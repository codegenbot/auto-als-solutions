#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;
    size_t pos = 0, prevPos = 0;

    while (pos != string::npos) {
        if (pos == string::npos || txt[pos] == ' ') {
            if (prevPos != pos) {
                result.push_back(txt.substr(prevPos, pos - prevPos));
            }
            pos++;
        } else if (txt[pos] == ',') {
            if (prevPos != pos) {
                result.push_back(txt.substr(prevPos, pos - prevPos));
            }
            pos++;
        } else {
            size_t nextComma = txt.find_first_of(", ", pos);
            if (nextComma == string::npos) {
                result.push_back(txt.substr(pos));
                break;
            }
            if (pos != nextComma) {
                result.push_back(txt.substr(pos, nextComma - pos));
            }
            pos = nextComma;
        }
    }

    if (result.empty()) {
        int count = 0;
        for (char c : txt) {
            if (c >= 'a' && c <= 'z' && (count & 1)) {
                result.push_back(to_string(count));
            }
            count++;
        }
    }

    return result;
}

int main() {
    string txt;
    cout << "Enter a string: ";
    getline(cin, txt);
    vector<string> result = split_words(txt);
    for (auto s : result) {
        cout << s << endl;
    }
    return 0;
}