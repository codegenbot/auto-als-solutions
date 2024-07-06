#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> select_words(string s, int n) {
    vector<char> word;
    int consonants = 0;
    vector<string> result;

    for (char c : s) {
        if (c == ' ') {
            if (consonants == n) {
                string tempWord(word.begin(), word.end());
                result.push_back(tempWord);
                word.clear();
                consonants = 0;
            }
        } else {
            bool isVowel = false;
            switch (tolower(c)) {
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u': 
                    isVowel = true;
                    break;
            }
            if (!isVowel) {
                consonants++;
            }
            word.push_back(c);
        }
    }

    if (consonants > 0) {
        string tempWord(word.begin(), word.end());
        result.push_back(tempWord);
    }

    return result;
}

int main() {
    cout << "{";
    vector<string> result = select_words("Mary had a little lamb", 4);
    for (const string& s : result) {
        cout << "\"" << s << "\", ";
    }
    cout << "}" << endl;
    return 0;
}