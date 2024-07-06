#include <vector>
#include <string>

using namespace std;

bool issame(const vector<string>& a, const vector<string>& b) {
    return a == b;
}

vector<vector<string>> split_words(string txt) { 
    vector<vector<string>> result;
    size_t pos = 0;
    while ((pos = txt.find(' ')) != string::npos) {
        result.push_back(vector<string>{txt.substr(0, pos)});
        txt.erase(0, pos + 1);
    }
    if (txt.empty()) {
        return result;
    }
    result.push_back(vector<string>{txt});
    return result;
}

int main() {
    string user_input;
    cout << "Enter a string: ";
    getline(cin, user_input);

    vector<string> words = split_words(user_input);
    
    for (const auto& word : words) {
        cout << word << endl;
    }
    assert(issame(split_words(""), {""})); 
}