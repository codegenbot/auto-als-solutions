#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> select_words(string s, int n) {
    vector<string> result;
    string word;
    int consonants = 0;

    for (char c : s) {
        if (c == ' ') {
            if (consonants == n) {
                result.push_back(word);
            }
            word.clear();
            consonants = 0;
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
            word += c;
        }
    }

    if (consonants == n) {
        result.push_back(word);
    }

    return result;
}

int main() {
    string s;
    int n;

    cout << "Enter a sentence: ";
    getline(cin, s);

    cout << "Number of consonants: ";
    cin >> n;

    vector<string> result = select_words(s, n);

    if (result.size() > 0) {
        cout << "{";
        for (const string& word : result) {
            cout << "\"" << word << "\", ";
        }
        cout << "}" << endl;
    } else {
        cout << "No words found." << endl;
    }

    return 0;
}